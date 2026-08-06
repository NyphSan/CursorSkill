# Project Patterns

## Scope

Use this file after inspecting an UnrealSharp repository. It intentionally contains no assumptions about a particular game, company, project name, directory layout, event bus, or UI framework.

## Discover local ground truth first

Before changing code, locate:

- The managed `.csproj` files, Glue-project references, and `UnrealSharp.Shared.props` import.
- The project's global usings, base classes, and one known-good example for the type being changed.
- Existing ownership boundaries for actors, components, controllers, widgets, subsystems, managers, and save systems.
- The established input, UI/focus, event, async/game-thread, logging, and packaging patterns.
- Any project-specific conventions for Blueprint asset names, collision channels, networking, and designer-assigned properties.

Use targeted search rather than assuming a generic sample applies:

~~~powershell
rg --files -g "*.cs" -g "*.csproj"
rg "UClass|UProperty|UFunction|ConfigureWithUnrealContext" -g "*.cs"
rg "BeginPlay|EndPlay|OnPossess|OnInitialized|Destruct" -g "*.cs"
~~~

## Preserve ownership boundaries

- Let actors own actor-level state and scene hierarchy.
- Let components own reusable behavior attached to one actor.
- Let controllers/HUD coordinators own input-mode and player-UI orchestration when that is the local pattern.
- Let widgets own presentation and immediate UI events; return gameplay decisions to their owner/service.
- Prefer an existing subsystem, service, or event bus over introducing a parallel static manager.
- Keep save/load, networking authority, and async cancellation ownership explicit.

## Apply a feature safely

1. Find a nearby working implementation of the same category.
2. Reuse the repository's naming, lifecycle, and asset-assignment conventions.
3. Make the smallest change that preserves the existing owner and data flow.
4. Save so UnrealSharp can automatically compile/reload the code.
5. Run the managed build for diagnostics without moving its output artifacts.
6. Close any blocking UnrealSharp compilation-error dialog before performing UE/editor automation.
7. Validate in the editor and package path that matches the feature's risk.

## Avoid common project-integration mistakes

- Do not duplicate global state when a project already has a single source of truth.
- Do not move world/gameplay decisions into widgets solely because the widget initiated an event.
- Do not edit generated Glue to force a runtime outcome.
- Do not scatter input/focus repair across unrelated controllers and widgets.
- Do not introduce a new high-frequency tick when an existing event, timer, manager, overlap, or interval loop owns the same responsibility.
- Do not copy project-specific names, paths, internal event contracts, or unpublished game mechanics into public documentation.
