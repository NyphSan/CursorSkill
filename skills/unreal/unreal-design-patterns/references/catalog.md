# Unreal Design Patterns — Full Catalog and Hand-Roll Recipes

The complete Gang of Four set plus the game-programming patterns, each mapped to its Unreal realization, with a verdict on whether to use the engine's version or hand-roll. Read a row when you want the full map; read the recipes when you are implementing one yourself. Synthesized from the GoF catalog, Nystrom's *Game Programming Patterns*, the "recognize patterns already in the engine" thesis of *Game Development Patterns with Unreal Engine 5* (Stuart Butler, Packt), and standard UE idioms.

## Contents
- [Creational](#creational)
- [Structural](#structural)
- [Behavioral](#behavioral)
- [Game-programming patterns](#game-programming-patterns)
- [Hand-roll recipes](#hand-roll-recipes)
- [Where to read these in the engine and Lyra](#where-to-read-these-in-the-engine-and-lyra)

---

## Creational

| Pattern | Intent | Unreal realization | Verdict |
|---|---|---|---|
| **Factory Method** | Defer which concrete type is created to a subclass/config | `TSubclassOf<>` + `NewObject`/`SpawnActor`; overridable `Create...` virtuals | Use engine + thin custom |
| **Abstract Factory** | Create families of related objects | `GameMode` class slots (`DefaultPawnClass`, `HUDClass`, `PlayerControllerClass`, `GameStateClass`) as a coherent family | Use engine |
| **Builder** | Construct a complex object step by step | Slate declarative syntax (`SNew`/`SAssignNew`), `FActorSpawnParameters`, `FMassEntityTemplateBuildContext` | Use engine; hand-roll for fluent config |
| **Prototype** | Clone a configured object without coupling to its class | The Class Default Object, archetypes, Blueprint-as-prototype, `DuplicateObject` | Use engine |
| **Singleton** | One instance, global access | **Avoid the classic form.** Use a **Subsystem** for managed lifetime and access | Use engine (Subsystem) |

The Singleton row is the most important: a raw `static GetInstance()` has no managed lifetime, no clean shutdown, and hides dependencies. Subsystems give you the one-instance access point with a defined lifetime tied to Engine/GameInstance/World/LocalPlayer.

## Structural

| Pattern | Intent | Unreal realization | Verdict |
|---|---|---|---|
| **Adapter** | Make incompatible interfaces work together | A `UINTERFACE` or wrapper component over a third-party SDK; `IOnlineSubsystem` adapts Steam/EOS/etc. | Hand-roll at the boundary |
| **Bridge** | Split abstraction from implementation so both vary | The RHI (render hardware interface), audio mixer backends. Rare in gameplay | Use engine; rarely hand-roll |
| **Composite** | Treat part-whole trees uniformly | SceneComponent attachment tree, UMG widget tree, Behavior Tree | Use engine |
| **Decorator** | Add behavior by wrapping | Behavior Tree decorators, Slate rich-text decorators, GAS `GameplayEffect` modifiers | Use engine |
| **Facade** | Simple front over a complex subsystem | `UGameplayStatics`, `UKismetSystemLibrary`, your own `UBlueprintFunctionLibrary` or Subsystem | Use engine + hand-roll a library |
| **Flyweight** | Share intrinsic state across many objects | Instanced Static Mesh (ISM/HISM), interned `FName`, shared `UDataAsset`/`UStaticMesh`/`UMaterial`, Mass fragments | Use engine |
| **Proxy** | A stand-in that controls access | Soft pointers (`TSoftObjectPtr`/`TSoftClassPtr`) for lazy load, `TWeakObjectPtr`, network role proxies (`ROLE_SimulatedProxy`/`ROLE_AutonomousProxy`) | Use engine |

## Behavioral

| Pattern | Intent | Unreal realization | Verdict |
|---|---|---|---|
| **Chain of Responsibility** | Pass a request along handlers | Input routing (`PlayerController` to `Pawn` to components), Slate input bubbling, GAS gameplay-cue routing | Use engine |
| **Command** | An action as an object: queue, replay, undo | Enhanced Input actions, `FScopedTransaction`, GAS ability activation | Use engine + hand-roll |
| **Interpreter** | Define a grammar and evaluate sentences in it | Rare in gameplay. `FGameplayTagQuery` evaluates tag expressions; Blueprint and material graphs are interpreted. Use these before hand-rolling a grammar | Rarely hand-roll |
| **Iterator** | Traverse without exposing structure | `TActorIterator`, `TObjectIterator`, `TArray` range-for | Use engine; never hand-roll |
| **Mediator** | Centralize many-to-many communication | A coordinating Subsystem or `GameMode`; an event-bus Subsystem | Hand-roll on engine primitives |
| **Memento** | Capture and restore state | SaveGame (`USaveGame`, `SaveGame` UPROPERTY), `FArchive` serialization | Use engine |
| **Observer** | Subscribe to state-change notifications | Dynamic multicast delegates, `BlueprintAssignable` events | Use engine |
| **State** | Behavior changes with internal state | Animation State Machine, StateTree, Behavior Tree; hand-roll a state object when none fit | Use engine first |
| **Strategy** | Interchangeable algorithms | Abstract `UObject`/`UINTERFACE` behind `TSubclassOf`/data | Hand-roll |
| **Template Method** | Fixed skeleton, overridable steps | `virtual` + `BlueprintNativeEvent`; actor and ability lifecycles | Use engine |
| **Visitor** | Add operations to a hierarchy without changing it | `FArchive` visiting properties, property editors. Rare in gameplay | Rarely hand-roll |

## Game-programming patterns

From Nystrom, the ones that earn their place in UE beyond the GoF set:

| Pattern | Intent | Unreal realization |
|---|---|---|
| **Component** | Compose behavior from parts instead of deep inheritance | `UActorComponent`/`USceneComponent`. The engine's core extensibility model |
| **Type Object** | Represent a "type" as data, not a subclass | `UDataAsset`/`DataTable` rows + GameplayTags |
| **Object Pool** | Reuse churny short-lived objects | A pool component/subsystem; Niagara and audio pooling |
| **Service Locator** | Provide global services with lifetime | Subsystems |
| **Update Method** | Per-element per-frame update | `Tick`/`TickComponent` (prefer timers/async when possible) |
| **Dirty Flag** | Defer expensive recompute until inputs change | `MarkRenderStateDirty`, replication dirtying, cached aggregates |
| **Spatial Partition** | Fast spatial queries | World Partition, octree, collision broadphase, HISM |
| **Event Queue** | Decouple when an event is sent from when it is handled | A Subsystem queue draining on tick; GAS gameplay events |
| **Double Buffer** | Present a consistent snapshot while the next is built | Render thread double buffering; rarely hand-rolled in gameplay |
| **Subclass Sandbox** | Define a subclass's behavior using protected operations the base provides | A base `UObject`/`AActor`/`UGameplayAbility` exposes protected helpers plus a `BlueprintImplementableEvent` or virtual the subclass or designer fills; behavior is composed from the sandbox without reaching outside |
| **Data Locality** | Lay out data for cache-friendly access | The Mass Entity framework (ECS), instanced static meshes; favor packed POD arrays over scattered `UObject`s on hot paths |
| **Game Loop** | The master loop driving progression independent of input and CPU speed | The engine owns it outright. You never implement it; hook `Tick`, timers, or async tasks instead |
| **Bytecode** | Encode behavior as data executed by a virtual machine | That is the Blueprint VM. Author Blueprints or data-driven config rather than hand-rolling a VM |

The last two (Game Loop, Bytecode) are listed for recognition only: the engine fully implements both, so you identify them rather than build them.

## Hand-roll recipes

The patterns from Move 2 of the skill, in fuller form.

### Strategy with a data asset selecting the concrete

```cpp
UCLASS(Abstract, EditInlineNew, DefaultToInstanced)
class UFireMode : public UObject
{
    GENERATED_BODY()
public:
    virtual void Execute(AActor* InInstigator) PURE_VIRTUAL(UFireMode::Execute,);
};

UCLASS(BlueprintType)
class UWeaponDefinition : public UPrimaryDataAsset
{
    GENERATED_BODY()
public:
    /** New firing behavior is a new subclass dropped into an asset, never an edit here. */
    UPROPERTY(EditDefaultsOnly, Instanced) TObjectPtr<UFireMode> FireMode;
};
```

### State machine with state objects

```cpp
UCLASS(Abstract)
class UEnemyState : public UObject
{
    GENERATED_BODY()
public:
    virtual void Enter(AActor* InOwner) {}
    virtual TSubclassOf<UEnemyState> Tick(AActor* InOwner, float InDelta) { return nullptr; }
    virtual void Exit(AActor* InOwner) {}
};

// The driver swaps states when Tick returns a non-null next-state class.
void UEnemyBrainComponent::TickComponent(float InDelta, ELevelTick, FActorComponentTickFunction*)
{
    if (!Current) return;
    if (TSubclassOf<UEnemyState> Next = Current->Tick(GetOwner(), InDelta))
    {
        Current->Exit(GetOwner());
        Current = NewObject<UEnemyState>(this, Next);
        Current->Enter(GetOwner());
    }
}
```
Reach for StateTree before this. Hand-roll only when StateTree and the Animation State Machine genuinely do not fit the problem.

### Object pool as a world subsystem

```cpp
UCLASS()
class UProjectilePoolSubsystem : public UWorldSubsystem
{
    GENERATED_BODY()
public:
    AProjectile* Acquire(TSubclassOf<AProjectile> InClass);
    void Release(AProjectile* InProjectile);
private:
    UPROPERTY() TArray<TObjectPtr<AProjectile>> Free;
};
```
A Subsystem is a natural home: world lifetime, single access point, no global. Release hides, disables collision, and stops the projectile; Acquire reverses that or spawns if the free list is empty.

### Command with undo

```cpp
UCLASS(Abstract)
class UPlayerCommand : public UObject
{
    GENERATED_BODY()
public:
    virtual void Execute(APawn* InPawn) {}
    virtual void Undo(APawn* InPawn) {}
};
// Keep a TArray<TObjectPtr<UPlayerCommand>> history; push on Execute, pop and Undo to reverse.
```

## Where to read these in the engine and Lyra

Concrete places to point at when justifying a recommendation:

- **Subsystems (Singleton/Service Locator):** any `U...Subsystem` in the engine; `UAssetManager`.
- **Observer:** `OnActorBeginOverlap`, `OnClicked`, GAS attribute-change delegates.
- **State:** the Animation State Machine in any AnimBP; `StateTree`; AI Behavior Trees.
- **Strategy / Type Object / Factory (data-driven):** Epic's **Lyra** sample is the best single read for data-driven design, GAS abilities as interchangeable behavior, Enhanced Input as Command, and Modular Gameplay (`GameFeatureAction`) as a factory/registry.
- **Flyweight:** `UInstancedStaticMeshComponent`/HISM, the Mass framework.
- **Composite:** the component hierarchy on any actor; the Slate/UMG widget tree.
- **Command:** the Enhanced Input plugin; the editor transaction system.

When a design resembles one of these, cite the engine or Lyra example rather than re-deriving the pattern from first principles.
