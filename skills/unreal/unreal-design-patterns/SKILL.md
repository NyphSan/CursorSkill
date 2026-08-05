---
name: unreal-design-patterns
description: Identify and apply software design patterns (the Gang of Four creational, structural, and behavioral patterns, plus game-programming patterns like Object Pool, Type Object, Component, Service Locator, and Dirty Flag) specifically in Unreal Engine 5 C++. Two jobs. First, recognize when the engine already implements a pattern so you use its system instead of reinventing it (delegates = Observer, Subsystems = Service Locator/Singleton, ActorComponents = Component, GameplayTags = Type Object, soft pointers = Proxy, SaveGame = Memento, and more). Second, hand-roll the idiomatic UE version when the engine does not give it to you (Strategy, State, Object Pool, Command). Use this skill proactively whenever planning, architecting, or building any Unreal C++ system, and proactively name the pattern that fits and explain why even when the user has not asked for a pattern by name, for example "how should I structure spawning of many enemy types", "I need undo for player actions", "objects keep getting created and destroyed every frame", "how do I let systems react to an event without coupling them", "this needs a state machine", or "design a system for X". Equally, call out when NO pattern is warranted and a plain implementation is better. Not for line-level code style or formatting (that is the conventions layer), general non-Unreal pattern theory with no UE context, or Blueprint-only visual scripting. Complements the unreal-solid skill: patterns are how you realize the SOLID principles.

---

# Unreal Design Patterns

Design patterns are named, proven solutions to recurring design problems. In Unreal the job has two halves, and getting the first one right matters more than the second:

1. **Recognize the pattern the engine already implements, and use it.** Most patterns you reach for, UE has already built and battle-tested. Reaching for a hand-rolled Observer when dynamic delegates exist, or a custom Singleton when Subsystems exist, is the most common mistake. Recognize it, use the engine's version, move on.
2. **Hand-roll the idiomatic UE version only when the engine does not give it to you.** A small set (Strategy, State, Object Pool, Command) you genuinely implement yourself, and there is a right UE way to do each.

Patterns are the *named solutions*; the SOLID principles (sibling skill `unreal-solid`) are the *why* they work. Strategy realizes OCP, Observer enables DIP, Component is SRP plus composition. When the question is "is this modular," that is `unreal-solid`. When it is "what proven structure fits here," that is this skill.

This skill is meant to be used **proactively**: while planning or architecting, name the fitting pattern and justify it even when nobody asked for one by name. The discipline that keeps that useful instead of noisy is in "When NOT to reach for a pattern." Read it.

## Move 1: recognize what the engine already gives you

Before designing anything custom, check whether the problem is one the engine already solved. If the right column exists, use it and do not hand-roll the pattern.

| You are about to build... | That is the pattern | Use the engine's version |
|---|---|---|
| a global manager / `static GetInstance()` | Singleton / Service Locator | a **Subsystem** (`UGameInstanceSubsystem`, `UWorldSubsystem`, `ULocalPlayerSubsystem`): managed lifetime, no global |
| objects reacting to an event without coupling | Observer | **dynamic multicast delegates** (`DECLARE_DYNAMIC_MULTICAST_DELEGATE`, `BlueprintAssignable`) |
| creating objects whose type varies by data | Factory Method / Abstract Factory | `TSubclassOf<>` + `SpawnActor`/`NewObject`; the class slots on `GameMode` are an abstract factory |
| cloning a configured object | Prototype | archetypes, the **Class Default Object**, Blueprint defaults, `DuplicateObject` |
| a simple API over a complex subsystem | Facade | a `UBlueprintFunctionLibrary` or a Subsystem (`UGameplayStatics` is exactly this) |
| thousands of similar objects eating RAM | Flyweight | shared `UDataAsset`, interned `FName`, **Instanced Static Mesh** (ISM/HISM), Mass |
| a part-whole tree of objects | Composite | the **SceneComponent attachment tree**, the UMG widget tree, a Behavior Tree |
| traversing a collection | Iterator | `TActorIterator`, `TObjectIterator`, range-for over `TArray`. Never hand-roll |
| behavior that changes by mode, with transitions | State | **Animation State Machine**, **StateTree**, Behavior Tree |
| a fixed lifecycle with overridable steps | Template Method | `virtual` + `BlueprintNativeEvent`; `BeginPlay`/`Tick`/`EndPlay` already are this |
| queueable or rebindable player actions | Command | **Enhanced Input** actions; `FScopedTransaction` for editor undo |
| snapshot and restore object state | Memento | the **SaveGame** system (`USaveGame`, the `SaveGame` UPROPERTY specifier), `FArchive` |
| a lazy-loaded or access-controlled stand-in | Proxy | **soft pointers** (`TSoftObjectPtr`/`TSoftClassPtr`) + `FStreamableManager`; network role proxies |
| many designer-authored "types" of a thing | Type Object | `UDataAsset`/`DataTable` rows + **GameplayTags** (see `unreal-solid` on tags) |
| layering optional behavior onto a node | Decorator | **Behavior Tree decorators**, Slate/rich-text decorators, GAS effect modifiers |
| recompute only when something changed | Dirty Flag | `MarkRenderStateDirty`, `MarkPackageDirty`, replication dirtying |
| per-frame work | Update Method | `Tick`/`TickComponent`. Prefer timers or async when you do not truly need every frame |
| spatial queries at scale | Spatial Partition | **World Partition**, the collision broadphase, octrees, HISM |

The takeaway: in gameplay code the honest answer is usually "the engine already has this." The rest of the skill is the minority of cases where it does not.

## Move 2: the patterns you actually hand-roll

These are the ones worth implementing yourself, each with the force it resolves and the idiomatic UE shape.

### Strategy — interchangeable behavior chosen by data

Use when one operation has several interchangeable implementations and you are tempted to `switch` on a type. This is the direct realization of OCP. New behavior becomes a new subclass or asset, never an edit to the caller.

```cpp
UCLASS(Abstract, EditInlineNew, DefaultToInstanced)
class UFireMode : public UObject
{
    GENERATED_BODY()
public:
    virtual void Execute(AActor* InInstigator) PURE_VIRTUAL(UFireMode::Execute,);
};
// UHitscanFireMode, UProjectileFireMode... selected on the weapon's data asset; the weapon calls FireMode->Execute(this).
```
Engine echo: movement modes on `UCharacterMovementComponent`, EQS generators, pathfinding query filters. **Skip it** when there is only ever one implementation.

### State — per-mode behavior with explicit transitions

Use when an object's behavior *and* its legal transitions vary by mode, and the engine's state tools do not fit. Prefer **StateTree** or the **Animation State Machine** first; hand-roll only when neither applies.

```cpp
UCLASS(Abstract)
class UEnemyState : public UObject
{
    GENERATED_BODY()
public:
    virtual void Enter(AActor* InOwner) {}
    /** Returns the next state class, or null to stay. */
    virtual TSubclassOf<UEnemyState> Tick(AActor* InOwner, float InDelta) { return nullptr; }
    virtual void Exit(AActor* InOwner) {}
};
```
The smell that calls for it: a thicket of `bIsAttacking`/`bIsFleeing`/`bIsStunned` booleans gating every function.

### Object Pool — recycle churny short-lived actors

Use when you spawn and destroy the same kind of actor constantly (projectiles, impact FX, audio one-shots). Pooling deactivates and reuses instead of paying `SpawnActor`/`Destroy` and GC churn, which is a common source of frame hitches.

```cpp
AProjectile* UProjectilePool::Acquire()
{
    AProjectile* P = Free.Num() ? Free.Pop() : GetWorld()->SpawnActor<AProjectile>(ProjectileClass);
    P->SetActorHiddenInGame(false);
    P->SetActorEnableCollision(true);
    return P;
}
void UProjectilePool::Release(AProjectile* InProjectile)
{
    InProjectile->SetActorHiddenInGame(true);
    InProjectile->SetActorEnableCollision(false);
    Free.Push(InProjectile);
}
```
Engine echo: Niagara system pooling, audio voice pools. **Skip it** when spawns are infrequent; the bookkeeping is not free.

### Command — an action as an object

Use when an action must be queued, buffered, replayed, logged, or undone rather than executed inline: input buffering, combo queues, networked input, turn-based moves, editor undo.

```cpp
UCLASS(Abstract)
class UPlayerCommand : public UObject
{
    GENERATED_BODY()
public:
    virtual void Execute(APawn* InPawn) {}
    virtual void Undo(APawn* InPawn) {}
};
```
Engine echo: Enhanced Input actions, editor `FScopedTransaction`, GAS ability activation. **Skip it** for immediate actions with no queue, replay, or undo need.

### Observer — the one you hand-apply constantly

Even though delegates are Move 1, applying them well is on you. The emitter declares a dynamic multicast delegate, broadcasts, and knows nothing about its listeners; listeners `AddDynamic`/`RemoveDynamic` and expose it `BlueprintAssignable`. That ignorance is the DIP inversion from `unreal-solid`: the compile dependency points one way, and it is how you break a would-be circular dependency between two systems.

## Proactively recommending a pattern

When planning or architecting, do this without being asked:

1. **Name the force.** What varies, what is tightly coupled, what is churning, what needs to be queued, undone, or notified.
2. **Check Move 1 first.** If the engine already implements the matching pattern, recommend that system and stop. Suggesting a hand-rolled version of something the engine ships is a downgrade.
3. **State the why in one line** (the force it resolves) and point to the engine analogue, so the recommendation is concrete rather than abstract.
4. **Apply the restraint.** If nothing actually varies, repeats, or churns, recommend the plain implementation and say why a pattern would cost more than it returns.

## When NOT to reach for a pattern (read this)

A proactively-suggesting skill fails by pattern-ifying everything. Each pattern must pay for the indirection it adds.

- **The engine already does it.** This is the number one mistake. A custom Singleton instead of a Subsystem, a hand-rolled event list instead of a delegate, your own iterator instead of `TActorIterator`. Use Move 1.
- **One case, no second in sight.** Rule of three. A Strategy with one strategy, a Factory that makes one type, a State machine with one state are all just indirection.
- **Pattern tax is real.** More files, more boilerplate, more for the next reader to trace. Modularity is the goal; the pattern is only a means.
- **Do not stack patterns for elegance.** Each one in a design must resolve a force you can name out loud.
- **A pattern that fights the engine's grain is worse than none.** If your custom solution duplicates or works around a Subsystem, a component, or a delegate, stop and use the engine.

## Notes

- Examples use plain Unreal type prefixes (`U`, `A`, `F`, `I`, `E`) with no studio or plugin prefix, plus `TObjectPtr`, `/** */` doc comments, and `In`/`Out` parameter prefixes. In a real project, keep the type prefixes and match that project's own naming.
- **Relationship to `unreal-solid`:** that skill evaluates a design against principles; this one supplies named structures. They are meant to fire together on architecture work. If both are relevant, use the principle to decide *whether* to add a seam and the pattern to decide *which* seam.
- For the full Gang of Four catalog mapped to Unreal (every creational, structural, and behavioral pattern), the game-programming patterns, fuller hand-roll code, and where to read each in the engine and the Lyra sample, see [references/catalog.md](references/catalog.md).
