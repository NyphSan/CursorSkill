# Unreal Replication — Reference and Pitfalls

Depth for the `unreal-replication` skill. Read the relevant section when the SKILL.md summary is not enough. Synthesized from the Multiplayer Network Compendium (Cedric Neukirchen), Epic's networking documentation, and standard UE practice. All examples use plain UE type prefixes; match your project's naming.

## Contents
- [Framework classes by network role](#framework-classes-by-network-role)
- [Replication primitive recipes](#replication-primitive-recipes)
- [RPC rules in full](#rpc-rules-in-full)
- [Ownership and routing](#ownership-and-routing)
- [Relevancy, priority, dormancy](#relevancy-priority-dormancy)
- [Scaling beyond the default: Replication Graph and Iris](#scaling-beyond-the-default-replication-graph-and-iris)
- [Net roles in full](#net-roles-in-full)
- [GAS replication model](#gas-replication-model)
- [Dedicated vs listen server, and travel](#dedicated-vs-listen-server-and-travel)
- [Pitfalls catalog](#pitfalls-catalog)

---

## Framework classes by network role

Where each framework object exists, and what that means for the state you put on it.

| Class | Exists on | Use it for |
|---|---|---|
| `AGameModeBase` | **server only** | authoritative rules, spawning, match flow. Clients never see it, so never put client-readable state here |
| `AGameStateBase` | server + all clients | game-wide replicated state every client reads (phase, wave, shared scores) |
| `APlayerState` | server + all clients | per-player replicated state every client reads (score, name, team) |
| `APlayerController` | server + **owning** client | the player's command path and owner-only data; the home for player-issued Server RPCs |
| `APawn`/`ACharacter` | server + all clients | the replicated avatar; movement replicates with the Character movement component |
| `AHUD`, UMG widgets | **owning client only** | presentation; never authoritative |
| `UGameInstance` | every instance, independent, not replicated | data that must survive level travel (set it per-instance, sync over the network separately if clients need it) |

Reasoning to apply: choose the class whose presence matches the audience of the data. Score every client must display goes on `PlayerState` (replicated everywhere), not `PlayerController` (only the owner would see it).

## Replication primitive recipes

### Replicated variable

```cpp
// .h
UPROPERTY(Replicated)
float Health;

// .cpp
void AThing::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    DOREPLIFETIME(AThing, Health);
    DOREPLIFETIME_CONDITION(AThing, Ammo, COND_OwnerOnly); // only the owner needs to see ammo
}
```
The actor must have `bReplicates = true`. An actor replicates only if **spawned by the server**; a client-spawned actor exists only on that client.

Conditions: `COND_InitialOnly`, `COND_OwnerOnly`, `COND_SkipOwner`, `COND_SimulatedOnly`, `COND_AutonomousOnly`, `COND_SimulatedOrPhysics`, `COND_InitialOrOwner`, `COND_Custom` (toggled via `SetCustomIsActiveOverride`). Use them to avoid sending data a given client cannot use.

### RepNotify

```cpp
UPROPERTY(ReplicatedUsing=OnRep_Health)
float Health;

UFUNCTION()
void OnRep_Health(); // reacts to the new value on clients
```
In C++ `OnRep_` fires **only on clients**. If the server changes the value and needs the same reaction, set the value then call `OnRep_Health()` manually server-side. (In Blueprint the RepNotify fires on server and client, which is a different contract.) Use RepNotify for "react to the current value," not for events that must happen exactly once.

### The three RPCs

```cpp
UFUNCTION(Server, Reliable, WithValidation)   void ServerDoThing(int32 InArg);
UFUNCTION(Client, Unreliable)                 void ClientNotify();
UFUNCTION(NetMulticast, Unreliable)           void MulticastCosmetic();
```
Each needs an `_Implementation`. `WithValidation` adds a `bool ServerDoThing_Validate(int32 InArg)`; returning false disconnects the caller (treat malformed input as hostile). Server RPCs are reliable by default for must-arrive requests; mark cosmetic multicasts unreliable.

## RPC rules in full

- RPCs must be called on a **replicated** actor or a **replicated subobject** (for example a replicated component).
- **Server RPC:** client to server. Dropped if the client does not own the actor. Validate inputs.
- **Client RPC:** server to the **owning** client only.
- **NetMulticast:** server to server + all relevant clients. **Called from a client it runs only locally**, not on the server or others. Capped at roughly two executions per actor net update period, so it is for occasional cosmetic events, not a stream.
- **Reliability:** do not mark everything `Reliable`. Reliable RPCs on tick fill the reliable buffer and can stall other properties and RPCs. Reserve reliable for infrequent must-arrive calls.

## Ownership and routing

Ownership resolves recursively up `GetOwner` until the outermost owner; if that is a `PlayerController`, the owning connection owns the actor. Ownership governs Server RPC validity, relevancy, and `COND_OwnerOnly`.

Routing pattern for acting on an unowned actor:

```cpp
// On the client, called on the player's OWN PlayerController:
void APlayerController::ServerInteract_Implementation(AActor* InTarget)
{
    if (!IsValid(InTarget) || !CanInteractWith(InTarget)) return; // validate server-side
    IInteractable::Execute_Interact(InTarget, GetPawn());          // act on the unowned target
}
```
Set ownership with `SetOwner` on the server. A Pawn is owned by its controller only while possessed; unpossessing revokes it.

## Relevancy, priority, dormancy

Relevancy (`AActor::IsNetRelevantFor`) decides who receives an actor, roughly in order: always-relevant or owned-by-the-viewer actors pass; `bNetUseOwnerRelevancy` inherits the owner's status; `bOnlyRelevantToOwner` restricts to the owner; attachments inherit their base; hidden-without-collision is culled; then distance via `NetCullDistanceSquared`.

Priority (`GetNetPriority`) shares bandwidth proportionally: `NetPriority` 2.0 updates twice as often as 1.0, weighted by time-since-last-update and distance.

Optimization knobs: `NetUpdateFrequency`, `NetCullDistanceSquared`, `bAlwaysRelevant`, `bOnlyRelevantToOwner`, and dormancy (`SetNetDormancy(DORM_DormantAll)` for actors that rarely change, `FlushNetDormancy()` when one does). Reach for these against a measured problem.

## Scaling beyond the default: Replication Graph and Iris

The default replication driver evaluates relevancy per actor per connection every update. That is simple and correct, and it holds for most games (into the hundreds of actors at modest player counts). It stops scaling when that per-actor-per-connection iteration itself becomes the server CPU bottleneck: very high actor counts, high player counts, or both (battle royale, large survival or MMO-like games).

**Replication Graph** (`UReplicationGraph`, installed as the `ReplicationDriverClass`) replaces that iteration. Actors are placed into nodes: a spatial grid relevant by location, always-relevant lists, per-connection nodes, and class routing policies. Each connection's relevant set is gathered by walking a few nodes instead of testing every actor, moving the cost from roughly O(actors x connections) toward O(relevant actors). It is what large-player-count Epic titles run on.

**Iris** (UE5's newer, data-oriented replication system, experimental moving toward production) is the successor direction, built to scale further and cut per-property overhead.

Decision rule: **do not reach for either pre-emptively.** Both are significant engineering investments justified only against a *measured* server-relevancy bottleneck. Exhaust the cheap levers first (vision and relevancy scoping, dormancy, update frequency, quantization, `COND_*`, replicating decisions not consequences). Keep actor network state as compact structs early so the option stays open, but switch only when profiling shows the default driver is the ceiling.

## Net roles in full

`ENetRole`: `ROLE_None`, `ROLE_SimulatedProxy`, `ROLE_AutonomousProxy`, `ROLE_Authority`. The authority instance is in charge of the actor whether or not it replicates. A simulated proxy interpolates toward updates and extrapolates by last velocity between them; an autonomous proxy (a player-possessed actor on its owning client) fills the gaps with real input.

Checks:
- `HasAuthority()` (`Role == ROLE_Authority`): gate state mutation.
- `IsLocallyControlled()`: gate input and local prediction.
- Autonomous vs simulated: prediction vs interpolation.

Authority, ownership, and locally-controlled are three different things. A dedicated server has authority over a pawn it neither owns by connection nor controls locally.

## GAS replication model

- **Attributes** replicate via the ASC and its `FGameplayAttributeData`. Do not add parallel replicated floats.
- **Replication mode** (`EGameplayEffectReplicationMode`): `Full` (every effect replicated to everyone, fine for single-player or small counts), `Mixed` (effects replicated to the owning client, cues to everyone, the right choice for player-controlled actors), `Minimal` (no effect replication, cues only, for AI/NPCs). Set it on the ASC during setup.
- **Abilities** predict on the owning client with prediction keys and reconcile against the server. Author them server-authoritative; let prediction handle responsiveness.
- **GameplayCues** are cosmetic and execute across clients (often via the cue manager). Never put authoritative gameplay logic in a cue.
- **GameplayEffects** are the authoritative state-change unit; prefer them over manual attribute writes so prediction and replication stay consistent.

## Dedicated vs listen server, and travel

A **dedicated server** is headless: no local player, no PlayerController index 0, no HUD. A **listen server** is a server that is also a client, so `GetPlayerController(0)` returns the host's controller. Code that assumes a headless server breaks on a listen server's host player and vice versa; guard with role and locally-controlled checks rather than assuming.

**Travel:** seamless travel preserves certain actors (the PlayerController, and actors moved to the transition level) across a level change; non-seamless travel tears down and recreates. Mark actors to carry over deliberately; do not assume references survive a travel.

## Pitfalls catalog

| Symptom | Cause | Fix |
|---|---|---|
| Actor exists only on one client | spawned by a client | spawn replicated actors on the server |
| Replicated variable never updates | missing `GetLifetimeReplicatedProps`/`DOREPLIFETIME` or `bReplicates` false | register the property and enable replication |
| `OnRep_` reaction missing on the server | C++ RepNotify fires client-only | set the value then call `OnRep_` manually server-side |
| Server RPC does nothing | caller does not own the actor | call it on an owned actor (PlayerController) and route to the target |
| Multicast does nothing for others | called from a client | call multicasts from the server only |
| Late joiners miss an effect | cosmetic sent as a one-off multicast | make it replicated state with an `OnRep_` reaction |
| Hitches and dropped updates under load | reliable RPCs on tick filling the buffer | make high-frequency RPCs unreliable, or use replicated state |
| Bandwidth spikes with many AI | GAS ASC in `Full` mode on NPCs | use `Minimal` for AI, `Mixed` for players |
| Client can trigger illegal actions | trusting client input | validate every Server RPC; mutate state only with authority |
