---
name: unreal-replication
description: Design and review Unreal Engine multiplayer replication and server-authoritative architecture in C++. The design lens for networked gameplay: who is authoritative, where networked state should live (GameState vs PlayerState vs PlayerController vs GameInstance), which replication primitive fits each need (replicated variables, RepNotify, Server/Client/Multicast RPCs), ownership and RPC routing, relevancy and bandwidth tuning, net roles and authority checks, and the discipline of never trusting the client. Use this skill proactively whenever planning, building, or reviewing anything that touches multiplayer, authority, or "who is allowed to do what", and raise authority/replication concerns even when code looks single-player but will run in multiplayer, for example "how should I replicate the player's health or score", "this needs to work in multiplayer", "should this run on the server or the client", "how do I sync this across clients", "players can cheat by doing X", "how do I handle player input authoritatively", or "design a multiplayer X". Includes the Gameplay Ability System replication model (ASC replication modes, predicted abilities, attributes, GameplayCues). Equally, call out when something should NOT be replicated and can stay local or be derived. Not for non-Unreal networking, raw socket/transport programming, line-level code style, or Blueprint-only scripting. Complements unreal-solid and unreal-design-patterns: this is where "where does state live" becomes a networking decision.

---

# Unreal Replication

Unreal multiplayer is **server-authoritative**: the server holds the truth, clients send *requests*, the server validates and applies them, and the results replicate back out. Getting replication right is almost entirely a set of **design decisions**, not API trivia. The model already knows how to type a `Replicated` UPROPERTY; the value is deciding *who is authoritative, where state lives, which primitive carries each piece of data, and what should not be replicated at all*.

The prime directive runs through everything: **never trust the client.** Any logic that mutates authoritative game state runs on the server, behind a `HasAuthority()` check, after validating the request. Clients may predict for responsiveness, but the server can always override.

This is the networked extension of the "where does state live" question from `unreal-design-patterns`, and authority is a boundary in the `unreal-solid` sense. Use those skills for the structure; use this one to make it correct over the wire.

## When to use this (proactively)

Raise replication concerns without being asked whenever a design touches shared state, authority, or "who can do what", including code that looks single-player today but is meant to ship multiplayer. The restraint that keeps this useful instead of paranoid is in "When NOT to replicate." Read it.

## Decision 1: who is authoritative?

The server. Always, for anything that affects the game. A client action (move, fire, buy, open) is a *request*: the client asks, the server validates (enough ammo? in range? allowed?), then the server applies and replicates the result. Logic that changes authoritative state belongs on the server:

```cpp
void AThing::TryActivate()
{
    if (!HasAuthority()) { ServerActivate(); return; } // client: ask the server
    if (!CanActivate())  { return; }                    // server: validate, never trust the caller
    ApplyActivation();                                  // server: mutate truth, replication carries it out
}
```

Client prediction is an optimization layered on top (movement is the built-in example), never a replacement for server authority.

## Decision 2: where does the state live?

Put each piece of state on the class whose network presence matches who needs it. This single table prevents most replication design mistakes.

| The state is... | It should live on | Network presence |
|---|---|---|
| game-wide, every client needs it (match phase, wave, scoreboard) | **`AGameStateBase`** | server + all clients |
| per-player, every client needs it (a player's score, name, team) | **`APlayerState`** | server + all clients |
| per-player, only the owner needs it (owner-only UI data, input intent) | **`APlayerController`** | server + owning client |
| authoritative rules, spawning, match flow, no client copy | **`AGameModeBase`** | server only |
| local-only presentation (HUD, widgets, camera) | **HUD / UMG** | owning client only |
| persistent across level travel, not replicated | **`UGameInstance`** / subsystem | every instance, independent |

The trap to avoid: a hand-rolled "manager" that holds replicated match state. `AGameStateBase` is that, already replicated and join-in-progress safe.

## Decision 3: state or event? pick the primitive

This is the most common replication error: faking state with an event, or an event with state.

| You need... | Use | Runs where | Note |
|---|---|---|---|
| persistent truth others must see (and late-joiners get) | **Replicated UPROPERTY** | server sets, replicates down | eventually consistent; survives join-in-progress |
| to react when that value changes on clients | **RepNotify (`OnRep_`)** | clients only in C++ | call it manually on the server if the server needs the reaction too |
| owning client asks the server to do something | **Server RPC** + `_Validate` | server | caller must own the actor; validate the inputs |
| server tells one owning client something | **Client RPC** | that owning client | personal feedback ("you were hit") |
| server tells everyone a one-off cosmetic event | **Multicast RPC** | server + all relevant clients | server-only call; max ~2 per net update; unreliable for cosmetic; late-joiners miss it |

**The rule: persistent truth is a replicated variable; a one-off moment is an RPC.** If late-joiners must see it, it is state, so replicate a variable and react in `OnRep_`. Do not multicast it (they miss the broadcast). Do not replicate a bool to fake an event.

## Decision 4: ownership and RPC routing

A **Server RPC is dropped if the calling client does not own the actor.** Ownership resolves up the `GetOwner` chain to a `PlayerController` and its connection. So:

- Player-driven Server RPCs belong on an actor the client owns (the `PlayerController`, or the possessed Pawn while possessed).
- To act on a world actor the client does not own (a shared door, another player), route through an owned actor: the client calls a Server RPC on its `PlayerController`, which validates and then acts on the target server-side.
- Set ownership on the server with `SetOwner`. A Pawn is owned by its controller only while possessed.

## Decision 5: relevancy and bandwidth (only when it matters)

Replication is not free. When an actor count or update rate becomes a problem, these are the knobs, not a reason to reach for them prematurely:

- `NetUpdateFrequency`: how often the actor is considered for an update.
- `NetCullDistanceSquared`: distance beyond which it stops being relevant.
- `SetNetDormancy` (`DORM_DormantAll`): stop replicating an actor that rarely changes until it does (`FlushNetDormancy`).
- `bOnlyRelevantToOwner`, `bAlwaysRelevant`: scope who ever receives it.
- `COND_*` conditions on properties (`COND_OwnerOnly`, `COND_SkipOwner`, `COND_SimulatedOnly`): skip sends that a given client does not need.

Tune these against a measured bandwidth or CPU problem. Marking everything `bAlwaysRelevant` or replicating on tick is how you create one.

At large scale the bottleneck shifts from the *data* to the *relevancy gather itself*: the default driver tests every replicated actor against every connection each update, which holds into the hundreds of actors but not the thousands-with-many-players range (battle royale, large survival). That is the ceiling where **Replication Graph** (actors organized into spatial and always-relevant nodes so gathering is cheap) or UE5's newer **Iris** system earns its place. Both are major builds, so treat them as a measured-ceiling escalation, never a default. The standard relevancy path above is the right choice for the large majority of games (details in references).

## Roles and authority checks

`Role`/`RemoteRole` flip by perspective: on the server an owned pawn is `ROLE_Authority` with a remote `ROLE_AutonomousProxy`; on the owning client it is `ROLE_AutonomousProxy` with a remote `ROLE_Authority`; other clients see it as `ROLE_SimulatedProxy`. Three distinct questions, three checks, do not conflate them:

- **Do I own the truth?** `HasAuthority()` (`Role == ROLE_Authority`). Gate state mutation on this.
- **Is this the controlling player's machine?** `IsLocallyControlled()`. Gate input and local prediction on this.
- **Autonomous vs simulated proxy?** Drives prediction (real input) vs interpolation (last velocity).

Authority is not ownership, and neither is "locally controlled."

## GAS and replication

If a system is built on the Ability System Component, let GAS own replication where it already does, and set its mode deliberately:

- **Attributes** replicate through the ASC. Do not hand-roll replicated floats for them.
- **ASC replication mode:** `Full` for single-player or few actors, `Mixed` for player-controlled actors (gameplay effects to the owner, cues to everyone), `Minimal` for AI and NPCs (cues only). Picking `Full` for a crowd of AI is a common bandwidth mistake.
- **Abilities** run predicted on the owning client with server reconciliation; author them server-authoritative and let prediction keys handle the rest.
- **GameplayCues** are cosmetic and fan out across clients. Keep gameplay logic out of them.

Full detail is in references/networking.md.

## When NOT to replicate (read this)

Every replicated property is bandwidth, a consistency surface, and a thing that can desync. Replicate the **minimum authoritative truth and derive the rest locally.**

- **Derive, do not replicate.** Replicate health; let each client color the health bar and play the low-health animation locally. Replicate the target and intent; let clients interpolate the motion.
- **Cosmetic and locally reproducible state stays local:** footstep VFX, UI, camera, materials driven by already-replicated values.
- **Do not replicate high-frequency data you can reconstruct.** Replicate the decision, not every frame of its consequence.
- **Do not fake state with repeated multicasts** (late-joiners miss them) **or events with replicated bools.**
- The test for any candidate: does a remote machine actually need this to stay correct, and can it already derive it from something replicated? If it can derive it, do not send it.

## Notes

- Examples use plain Unreal type prefixes (`U`, `A`, `F`, `I`, `E`) with no studio or plugin prefix, plus `TObjectPtr`, `/** */` doc comments, and `In`/`Out` parameter prefixes. Match the local project's naming when applying them.
- **Relationship to the sibling skills:** `unreal-design-patterns` decides where state lives in-process; this skill decides how that state behaves across the network. `unreal-solid` keeps the authority boundary clean (the server-side validator is a single responsibility, the request path a dependency inversion).
- For the full framework-by-role breakdown, primitive recipes (with `GetLifetimeReplicatedProps`/`DOREPLIFETIME`), the ownership routing pattern, the relevancy knob reference, scaling beyond the default driver (Replication Graph and Iris), the complete GAS replication model, dedicated vs listen server and travel notes, and a pitfalls catalog, see [references/networking.md](references/networking.md).
