---
name: unreal-solid
description: SOLID object-oriented design principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) applied specifically to Unreal Engine C++, to keep systems modular, extensible, and maintainable. Use this skill whenever designing, architecting, building, extending, or refactoring any Unreal or C++ system, component, actor, ability, subsystem, plugin, or class hierarchy. Trigger it even when the user does not say the word "SOLID" but is making an Unreal C++ structural decision, for example "how should I structure this weapon/ability/inventory system", "this Character class is getting huge", "I need to add a third damage type without breaking the others", "how do I decouple these two plugins", "should this be a component or a subclass", or "design a system for X". Prefer this skill proactively at design time rather than after the code is written. Not for line-level code style or formatting (that is the C++ conventions / pre-commit layer), Blueprint-only visual scripting with no C++, or general non-Unreal software design.
---

# Unreal SOLID

SOLID is five design principles for keeping object-oriented code modular and extensible. The principles tell you *why* a design will or won't absorb change. In Unreal, a small set of engine-native tools tell you *how* to act on them: ActorComponents, `UINTERFACE`/`IInterface`, `UDataAsset`/`DataTable`, `TSubclassOf`, Subsystems, and delegates plus GameplayTags. Learn the mapping once and most design decisions answer themselves.

The goal is not maximum abstraction. It is code that absorbs the changes you can actually name. Read the "When NOT to apply" section before reaching for a seam, because a proactively-applied principle with no counterweight produces over-engineered code.

## When to use this

Pull this skill in at three moments:

- **Designing** a new system: decide where the seams go before writing the class.
- **Extending** an existing system: find the seam and slot into it. If there is no seam and you are about to edit a base class or add a `switch` case, that is the signal to introduce one first.
- **Reviewing / refactoring**: walk the smell column of the cheat sheet below against the code in front of you.

## The cheat sheet

| Principle | Implement it in Unreal with | Smell that says you broke it |
|---|---|---|
| **SRP** | One concern per `UActorComponent`; a thin coordinating Actor | God Actor/Component; a `.cpp` creeping past ~1000 lines; a "Manager" that does everything |
| **OCP** | `UDataAsset`/`DataTable`, `TSubclassOf`, strategy/fragment objects, `virtual`/`BlueprintNativeEvent` seams | A `switch(EType)` you edit for every variant; a central enum that grows with content |
| **LSP** | Honor base and interface contracts; segregate capabilities into interfaces | `Cast<Concrete>` then branch on type; overrides that no-op or `ensure(false)` because the contract does not fit |
| **ISP** | Many small `UINTERFACE`s, composed per class | Empty `_Implementation` stubs; implementers returning false for half the API |
| **DIP** | `TScriptInterface<IFoo>`, Subsystems, injected `TSubclassOf`, delegates | A high-level class that `#include`s a concrete type and calls `NewObject<Concrete>`; hard references creating circular plugin deps |

## The five principles

### SRP — Single Responsibility

A class should have one reason to change. In Unreal the classic violation is the God Actor: an `ACharacter` subclass that owns movement, inventory, combat, audio, UI, and save logic. Each of those is a separate axis of change, so each belongs in its own `UActorComponent`. The Actor becomes a thin coordinator that owns components and wires them together.

```cpp
// Before: one actor accumulates every axis of change (five reasons to change)
class APlayerCharacter : public ACharacter
{
    void Attack();          // combat
    void AddItem(/*...*/);  // inventory
    void PlayFootstep();    // audio
    void SaveProgress();    // persistence
};

// After: the actor coordinates focused components, each with one reason to change
class APlayerCharacter : public ACharacter
{
    /** Drives attacks, combos, and damage application. */
    UPROPERTY(VisibleAnywhere) TObjectPtr<UCombatComponent> Combat;
    /** Owns the carried items and equip state. */
    UPROPERTY(VisibleAnywhere) TObjectPtr<UInventoryComponent> Inventory;
};
```

SRP also applies at the module level: a plugin or module should own one cohesive concern, which is exactly what keeps cross-plugin boundaries clean.

### OCP — Open for extension, closed for modification

You should add behavior without editing existing classes. The enemy is the growing `switch(EWeaponType)` or `if (Tag == ...)` ladder you reopen every time a designer wants a new variant. Unreal gives you several seams, in rough order of preference:

1. **Data-driven design**: put configuration in a `UDataAsset`/`UPrimaryDataAsset`/`DataTable`. A new variant becomes a new asset, not new code.
2. **Strategy / fragment objects** behind `TSubclassOf<UBase>`: a new behavior is a new subclass that slots in.
3. **Extension hooks**: `virtual`, `BlueprintNativeEvent`, `BlueprintImplementableEvent` so subclasses and designers extend without touching the base.

```cpp
// Before: every new weapon reopens the base class
void AWeapon::Fire()
{
    switch (WeaponType) // not closed: a new case here for every weapon
    {
        case EWeaponType::Rifle:   /* ... */ break;
        case EWeaponType::Shotgun: /* ... */ break;
    }
}

// After: behavior lives behind a seam; a new weapon is a new asset or subclass
/** Pluggable firing behavior, chosen per-weapon in data. */
UPROPERTY(EditDefaultsOnly) TObjectPtr<UFireMode> FireMode;
void AWeapon::Fire() { FireMode->Execute(this); }
```

A fragment or component registry is OCP in action: new behavior becomes a new fragment, not an edit to the owner class.

### LSP — Liskov Substitution

A subclass or interface implementer must be usable anywhere the base is, without callers checking the concrete type. The Unreal-native smell is `Cast<UConcrete>(X)` followed by branching, or an override that no-ops, `ensure(false)`s, or `check(false)`s because the subclass "does not support" that operation. That is the classic "a Penguin is a Bird but cannot Fly" problem: the base contract promised something a subclass cannot honor.

```cpp
// Before: not every bird flies, so callers must special-case
class ABird { public: virtual void Fly() PURE_VIRTUAL(ABird::Fly,); };
class APenguin : public ABird { public: virtual void Fly() override { ensure(false); } };

// After: segregate the capability; only real flyers implement it
UINTERFACE() class UFlyable : public UInterface { GENERATED_BODY() };
class IFlyable { GENERATED_BODY() public: virtual void Fly() = 0; };
// APenguin simply does not implement IFlyable, and no caller pretends it does
```

When a subset of a hierarchy cannot honor a method, that is not an LSP problem to paper over with an empty override. It is an ISP signal: split the interface.

### ISP — Interface Segregation

Prefer many small `UINTERFACE`s over one fat one, so a class implements only what it actually does. A fat interface forces implementers to stub `_Implementation` methods they ignore, which is both noise and a lie about the class's capabilities.

```cpp
// Before: one fat interface forces empty stubs everywhere
class IGameEntity { virtual void Move() = 0; virtual void Attack() = 0; virtual void Save() = 0; };

// After: small capability interfaces, composed per class
class IMovable    { virtual void Move() = 0; };
class IDamageable { virtual void ApplyDamage(const FHitData& InHit) = 0; };
class ISaveable   { virtual void Save() = 0; };
// A destructible prop implements IDamageable only; a checkpoint implements ISaveable only
```

Splitting interaction into separate capability interfaces (interactable, focusable, highlightable) is ISP: a class opts into exactly the capabilities it has.

### DIP — Dependency Inversion

High-level systems should depend on abstractions, not concrete classes. A combat component should not `#include` a concrete targeting class and `NewObject<UConcrete>` it. It should depend on an interface and let the concrete be chosen at the edge (in Blueprint, a data asset, or a spawner).

Unreal gives you three injection mechanisms:

1. **`UINTERFACE` + `TScriptInterface<IFoo>`** held as a `UPROPERTY`, set in BP or data.
2. **Subsystems** (`UGameInstanceSubsystem`, `UWorldSubsystem`) resolved via `GetSubsystem`, instead of singletons or direct construction.
3. **Delegates / GameplayTags**: the high-level broadcasts and the low-level subscribes, which inverts the compile-time dependency entirely.

```cpp
// Before: the high-level system hard-wires one concrete dependency
void UCombatComponent::AcquireTarget()
{
    UConeTargetingStrategy* Targeting = NewObject<UConeTargetingStrategy>(this); // locked to one impl
    CurrentTarget = Targeting->Find(this);
}

// After: depend on an abstraction; inject the concrete at the edge
/** Targeting strategy, assigned per-weapon in data or Blueprint. */
UPROPERTY(EditAnywhere) TScriptInterface<ITargetingStrategy> Targeting;
void UCombatComponent::AcquireTarget() { CurrentTarget = Targeting->Find(this); }
```

DIP is also your defense against circular plugin dependencies: if plugin A needs something from plugin B, depend on an interface A owns and let B implement it, rather than A taking a hard reference to B.

## Cross-cutting Unreal levers

Most SOLID wins in Unreal come from four habits:

- **Composition over inheritance.** `UActorComponent`s are the engine's primary tool for SRP and OCP. Reach for "has-a component" before "is-a deep subclass." Deep `is-a` chains are where LSP violations breed.
- **Data-driven design.** Push variation into `UDataAsset`/`DataTable`. Code defines capability; data defines the specific variant. This is OCP for content.
- **Interfaces as contracts.** `UINTERFACE` is your unit of capability for ISP and your abstraction boundary for DIP.
- **Subsystems and delegates for decoupling.** Subsystems are injectable services; delegates and GameplayTags let systems talk without compile-time knowledge of each other.

## When NOT to apply (read this)

A seam earns its place when there is a real or concretely imminent second case. Until then it is just indirection that makes the code harder to read.

- **Rule of three.** Introduce the abstraction when the second concrete implementation exists or is firmly on the roadmap, not on a hunch. One implementer behind a `UINTERFACE` is overhead with no payoff.
- **Do not data-drive a constant**, do not `TSubclassOf` something that will never vary, do not split a 60-line actor into five components.
- **Over-segregation and over-injection have real costs**: more files to navigate, more wiring boilerplate, a steeper path for the next person reading it. Modularity is the goal; abstraction is only the means.
- **Hot paths.** Interface and virtual dispatch are fine almost everywhere, but do not introduce indirection in tight inner loops (per-particle, per-vertex, per-tick on thousands of actors) without measuring first.
- **The test:** can you name the change this seam absorbs? If you cannot name the second implementation, wait for it.

## Design-time workflow

1. **New system.** List the axes of change first. Assign each to a Unreal seam: separate concerns into components (SRP), put variation behind data or a strategy (OCP), define contracts as interfaces (LSP/ISP), decide what gets injected (DIP). Name the variation points before you write the class.
2. **Extending.** Find the existing seam and add a subclass, asset, or implementer. If you are reaching to edit a base class or add a `switch` case, stop: introduce the seam first (refactor to OCP), then add your variant behind it.
3. **Reviewing.** Walk the smell column of the cheat sheet against the diff.

## Notes

- Examples here use plain Unreal type prefixes (`U`, `A`, `F`, `I`, `E`) with no studio or plugin prefix, plus `TObjectPtr` for UPROPERTY pointers, `/** */` doc comments, and `In`/`Out` parameter prefixes. In a real project, keep the type prefixes and match that project's own naming conventions for the surrounding code.
- This is **design-time** guidance. The pre-commit pipeline (where one exists) enforces style and formatting, not design, so SOLID lands at authoring time, on you. Good design here means the pipeline rejects less.
- For fuller before/after examples (real `UINTERFACE` boilerplate, a data-driven OCP build-out, DIP via Subsystem and via delegate) and a longer anti-pattern catalog, read [references/patterns.md](references/patterns.md).
