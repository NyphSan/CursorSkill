# Unreal SOLID — Patterns and Anti-Pattern Catalog

Deeper material for the `unreal-solid` skill. Read the relevant section when the SKILL.md summary is not enough for the design in front of you. All examples use plain Unreal type prefixes with no studio prefix; match your project's own naming when you apply them.

## Contents
- [The real UINTERFACE pattern](#the-real-uinterface-pattern)
- [OCP: a data-driven build-out](#ocp-a-data-driven-build-out)
- [DIP via Subsystem](#dip-via-subsystem)
- [DIP via delegate inversion](#dip-via-delegate-inversion)
- [Refactoring a switch ladder into a seam](#refactoring-a-switch-ladder-into-a-seam)
- [Anti-pattern catalog](#anti-pattern-catalog)
- [Worked examples in Unreal itself](#worked-examples-in-unreal-itself)

---

## The real UINTERFACE pattern

The SKILL.md examples abbreviate interface boilerplate. The full Unreal form has two types: a `U`-prefixed `UInterface` for the reflection system and an `I`-prefixed pure interface for the actual methods.

```cpp
// ITargetingStrategy.h
#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "ITargetingStrategy.generated.h"

class AActor;

/** Reflection stub. Never add methods here. */
UINTERFACE(MinimalAPI, BlueprintType)
class UTargetingStrategy : public UInterface
{
    GENERATED_BODY()
};

/** Finds a target for a combat instigator. Implementers choose the search shape. */
class ITargetingStrategy
{
    GENERATED_BODY()

public:
    /** Returns the best target for InInstigator, or nullptr if none. */
    virtual AActor* Find(const AActor* InInstigator) const = 0;
};
```

Hold it with `TScriptInterface<ITargetingStrategy>` so both the `UObject` and the interface pointer stay valid and the reference is visible to the reflection system and garbage collector. Call a `BlueprintNativeEvent` interface method through its generated `Execute_` thunk (`ITargetingStrategy::Execute_Find(Obj, Instigator)`), never by calling the `_Implementation` directly.

---

## OCP: a data-driven build-out

The strongest OCP seam in Unreal is usually data, not code. Define capability once; let content define each variant.

```cpp
/** One weapon archetype, authored as an asset. New weapon = new asset, no code. */
UCLASS(BlueprintType)
class UWeaponDefinition : public UPrimaryDataAsset
{
    GENERATED_BODY()

public:
    /** Rounds per minute. */
    UPROPERTY(EditDefaultsOnly) float FireRate;

    /** Damage applied per hit. */
    UPROPERTY(EditDefaultsOnly) float Damage;

    /** Pluggable firing behavior; swap without touching the weapon actor. */
    UPROPERTY(EditDefaultsOnly) TObjectPtr<UFireMode> FireMode;
};
```

When variation is behavioral rather than numeric, back the data with a small strategy hierarchy (`UFireMode` with `UHitscanFireMode`, `UProjectileFireMode`, `UBeamFireMode` subclasses). The actor calls `FireMode->Execute(this)` and never knows which one it has. Adding a beam weapon is a new `UFireMode` subclass plus a new asset, with zero edits to `AWeapon`.

---

## DIP via Subsystem

Subsystems are Unreal's built-in service locator with a managed lifetime. Depend on the subsystem instead of constructing or singleton-ing a concrete manager.

```cpp
// High-level code resolves the service; it does not own or construct it.
if (UScoringSubsystem* Scoring = GetWorld()->GetSubsystem<UScoringSubsystem>())
{
    Scoring->AddScore(Points);
}
```

For full inversion, make the subsystem itself implement an interface and resolve by interface where a test double or alternate implementation matters. For most gameplay a concrete subsystem is the pragmatic stopping point: it is already decoupled from construction and lifetime.

---

## DIP via delegate inversion

Delegates remove the compile-time dependency in the awkward direction. The low-level emitter owns the event; the high-level (or sibling) listener subscribes. Neither needs the other's concrete header at the call site.

```cpp
// Emitter (low-level): declares and broadcasts, knows nothing about listeners.
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnDamaged, const FHitData&, Hit);

UPROPERTY(BlueprintAssignable) FOnDamaged OnDamaged;
// ... OnDamaged.Broadcast(Hit);

// Listener: binds at init, reacts, no hard reference back into the emitter's internals.
Health->OnDamaged.AddDynamic(this, &UFeedbackComponent::HandleDamaged);
```

This is how to break a would-be circular dependency between two plugins: the owner of the data broadcasts, the consumer subscribes, and the dependency arrow points only one way.

---

## Refactoring a switch ladder into a seam

When you meet an existing `switch(EType)` and need to add a case, convert rather than extend:

1. Define the seam: an interface or abstract `UCLASS` with one method per branch's behavior.
2. Move each existing `case` body into a concrete implementer.
3. Replace the `switch` with a single polymorphic call (`Behavior->Execute(...)`), resolving the implementer from data or `TSubclassOf`.
4. Add your new variant as a new implementer. The original site never changes again.

Do this at the third case, not the first. Two cases in a `switch` are fine; a ladder that grows with content is the OCP debt to pay down.

---

## Anti-pattern catalog

| Smell in the code | Principle | Fix |
|---|---|---|
| `ACharacter` subclass past ~1000 lines doing combat, inventory, audio, save | SRP | Extract one `UActorComponent` per concern; actor coordinates |
| `switch(EType)` / `if(Tag==...)` ladder reopened per variant | OCP | Data asset, strategy object, or `TSubclassOf` seam |
| Central enum that grows every time content is added | OCP | Replace enum-driven branching with polymorphism or data rows |
| `Cast<UConcrete>(X)` then branch on the result | LSP / DIP | Call through a base/interface contract instead of testing type |
| Override that is empty, `ensure(false)`, or `check(false)` | LSP | Segregate the capability into its own interface |
| `UINTERFACE` whose implementers stub half the methods | ISP | Split into smaller capability interfaces |
| High-level class `#include`s a concrete service and `NewObject<Concrete>`s it | DIP | Depend on `TScriptInterface<IFoo>`, inject at the edge |
| Two plugins with hard references to each other | DIP | One owns an interface, the other implements it; or invert via delegate |
| A `UINTERFACE` with exactly one implementer that will never have another | over-abstraction | Delete the interface, use the concrete type until a second case exists |

---

## Worked examples in Unreal itself

Point at engine-standard systems as recognizable references when explaining a design:

- **Composition (SRP/OCP):** the Gameplay Ability System builds behavior from an `UAbilitySystemComponent`, `UAttributeSet`s, and discrete abilities rather than a monolithic character. ActorComponents in general are the engine's SRP tool.
- **OCP via data:** GameplayEffects, DataTables, and Enhanced Input actions and mappings add behavior by authoring data, not by editing code.
- **ISP / DIP via interfaces:** engine interfaces such as `IAbilitySystemInterface` or `IGameplayTagAssetInterface` let callers depend on a capability instead of a concrete class.
- **Services via Subsystems:** `UGameInstanceSubsystem` and `UWorldSubsystem` provide managed, injectable services without singletons.

When a new system resembles one of these, point at the engine example rather than re-deriving the pattern.
