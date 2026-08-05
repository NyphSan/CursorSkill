# Gameplay Patterns

## Scope

Use this file for common UnrealSharp gameplay authoring tasks: actors, controllers, components, widgets, input, interaction, and Blueprint interop.

## Add a new Actor

1. Create a `partial` class with `[UClass]` that derives from the intended Unreal base type.
2. Add Unreal-facing properties with `[UProperty]` only when the editor, Blueprint, or serialization must see them.
3. Put setup in Unreal lifecycle methods such as `BeginPlay`, `OnPossess`, `Construct`, or `OnInitialized` according to the owner type.
4. Keep `Tick` focused on per-frame orchestration, not object discovery or heavy allocation.
5. If behavior becomes reusable, extract it into a component.

## Add a new Component

Use a component when behavior should attach to multiple actors or when an actor is already carrying too much state.

Recommended pattern:

- `[UClass] public partial class UMyComponent : UActorComponent`
- initialize cheap defaults in `BeginPlay`
- expose tuning knobs with `EditAnywhere | BlueprintReadWrite`
- keep owner resolution explicit and cache it when safe

## Add default components to an Actor

Use UnrealSharp component properties instead of constructing components ad hoc:

- root scene component first if needed
- child scene components with `AttachmentComponent`
- gameplay components as direct default components

This keeps the actor's scene hierarchy declarative and visible to Unreal.

## Add or change input behavior

1. Keep input assets on the controller or owning gameplay coordinator.
2. Add mapping contexts from the local player subsystem.
3. Bind actions in a single `BindInputActions(...)` method.
4. Keep callbacks narrow:
   - input reads raw action value
   - gameplay object applies the effect
5. If UI mode and game mode compete for focus, centralize the mode switch in the controller and reapply focus deliberately for a few frames if the project already relies on that pattern.

## Add or change a widget

1. Create a `[UClass] partial class` deriving from `UUserWidget`.
2. Bind blueprint controls with `BindWidget`.
3. Bind animations with `BindWidgetAnim`.
4. Subscribe to project events in `OnInitialized` or `Construct`.
5. Unsubscribe in `Destruct`.
6. Keep presentation logic in the widget and push gameplay decisions back to the owning actor/controller/system.

## Use events and delegates

- Prefer local events for owner-to-widget or widget-to-owner callbacks.
- Prefer the project's existing global event bus if the repository already standardizes on one.
- Always unsubscribe on teardown for long-lived static events.
- If an event fan-out crosses system boundaries, document intent in naming rather than relying on comments alone.

## Work with interfaces

- Use interfaces for interaction contracts, perception contracts, or cross-system capabilities.
- Keep the interface narrow and capability-based.
- When Unreal reflection is required, follow a working local interface example instead of inventing a new declaration style.
- For discovery, iterate owner components or actors and stop at the first capability that satisfies the use case.

## Blueprint interop rules

- Expose only what designers need.
- Use `TSubclassOf<T>` for assignable widget/actor/component class references.
- Assume editor assignment is part of the contract. Validate nulls and fail clearly when a required asset is missing.
- If a Blueprint subclass stops working after a rename, check whether the reflected property or function name changed.

## Async and streaming behavior

- If async work must hop back to Unreal context, use the established local helper pattern rather than raw `Task` assumptions.
- Avoid fire-and-forget unless failure is intentionally swallowed and logged.
- For streamed UI updates, buffer enough to avoid overly chatty repaint behavior while preserving responsiveness.

## Common review checks

- Is this Unreal-facing member actually required to be a `UProperty` or `UFunction`?
- Does ownership live at the right layer: actor, controller, component, widget, or service?
- Does teardown unsubscribe everything that subscribed?
- Does the code assume a Blueprint assignment that should be guarded with a runtime check?
- Does this introduce work in `Tick` that should be cached or event-driven?
