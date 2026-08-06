# Framework Basics

## Scope

Use this file for UnrealSharp language rules, project layout expectations, and reflection-binding constraints.

## Contents

- Project structure and reflection model
- Properties, functions, modules, subsystems, and ownership
- Structs/enums, delegates/events, and asset/class/object references
- Components, UMG, enhanced input, and generated Glue
- Build/regeneration, lifecycle, and safe default decisions

## Project structure

- Typical UnrealSharp layout:
  - `ProjectRoot/Plugins/UnrealSharp...`
  - `ProjectRoot/Script/<ManagedProject>`
  - `ProjectRoot/Script/<Project>.Glue`
- Managed project files usually:
  - target the .NET version required by the installed UnrealSharp release (the current official setup page lists .NET 10.0.5+)
  - import `UnrealSharp.Shared.props`
  - reference the generated `*.Glue.csproj`
- Treat the managed project as authored code and the glue project as generated interop.
- Do not upgrade an existing project merely because the public documentation lists a newer engine/.NET version; first inspect the installed plugin and local project files.

## Reflection model

- Expose Unreal classes with `[UClass]`.
- Expose Unreal interfaces with the UnrealSharp interface pattern and place Unreal-callable members on the interface contract.
- Expose Unreal structs and enums with the corresponding UnrealSharp attribute pattern used by the local codebase or official docs when the type must cross the Unreal boundary.
- Expose Unreal-visible properties with `[UProperty(...)]`.
- Expose Blueprint or Unreal-callable methods with `[UFunction(...)]`.
- Unreal-facing types commonly need `partial` so code generation can complete the type or member.
- If an authored type looks correct but Unreal cannot see it, suspect one of:
  - missing attribute
  - missing `partial`
  - unsupported signature
  - stale generated output
  - build/import misconfiguration

## Property patterns

- Prefer auto-properties declared as `public partial <Type> Name { get; set; }`.
- Use explicit property flags instead of relying on ambiguity.
- Common Unreal-facing property shapes include:
  - object refs: `UMyType`
  - class refs: `TSubclassOf<UMyType>`
  - arrays: `TArray<T>`
  - transient runtime-only refs that Unreal still needs to bind: `Transient`
- Common patterns:
  - editor-set asset/class refs: `EditAnywhere`
  - widget-facing values: `BlueprintReadWrite`
  - transient runtime refs: `Transient`
- Default components are still declared via `[UProperty(DefaultComponent = true)]`.
- Attachment hierarchies are expressed with `AttachmentComponent = nameof(...)`.

## Function patterns

- Use `[UFunction]` for methods Unreal or Blueprint must discover.
- Keep signatures conservative and aligned with known working local examples.
- If binding input or delegates, prefer existing local method shapes over novel signatures.
- If a function never needs Unreal reflection, leave it as a normal C# method.

## Modules, subsystems, and ownership

- Use `IModuleInterface` for managed module startup/shutdown code when the project exposes a managed module entry point.
- Keep module startup minimal: registration, one-time wiring, diagnostics, not gameplay state.
- Use Unreal subsystems when the lifetime should follow engine, game instance, world, or local player ownership rather than a hand-rolled singleton.
- When a subsystem already exists in the project, prefer retrieving it rather than creating a parallel static manager.

## Structs, enums, and data containers

- Use Unreal-exposed structs for small data passed across reflection boundaries or edited in Unreal tools.
- Use enums when the state must be designer-visible, serialized, or Blueprint-readable.
- Keep pure implementation-only helper data as normal C# types if Unreal does not need to see it.
- When in doubt, avoid exposing a type to Unreal unless editor use, serialization, Blueprint access, or generated interop actually requires it.

## Delegates and events

- Use normal C# events for local managed ownership.
- Use Unreal-exposed delegate patterns only when Unreal-side binding or Blueprint participation is required.
- For static/global managed events, design teardown first. Long-lived subscriptions are a common source of duplicate execution.

## Asset, class, and object references

- Prefer `TSubclassOf<T>` when the editor should assign a class and C# will instantiate or create an instance later.
- Prefer direct object references when the editor should assign a specific asset/object instance.
- Validate required assignments near startup, possession, or widget construction so failures are immediate and obvious.
- Keep nullable handling honest. Do not hide a required editor contract behind broad null-tolerant code.

## Component declarations

- Declare built-in scene hierarchies from C# using `DefaultComponent`, `RootComponent`, and `AttachmentComponent`.
- Keep ownership obvious:
  - actor owns components
  - controller owns UI/input orchestration
  - component owns isolated reusable behavior
- For complex actor behavior, prefer a reusable component before expanding a monolithic actor unless the behavior is inherently actor-specific.

## Widgets and UMG

- Bind designer widgets with `[UProperty, BindWidget]`.
- Bind widget animations with `[UProperty(PropertyFlags.Transient), BindWidgetAnim]`.
- Create widget instances with `CreateWidget<T>()`.
- Add them to the viewport from the correct owner, commonly a player controller or HUD-like coordinator.
- If a widget binding is null at runtime, inspect:
  - the widget blueprint control name
  - the C# property name
  - whether the widget exists in the blueprint hierarchy
  - whether the bound type matches the actual widget class

## Enhanced Input

- Store `UInputAction` and `UInputMappingContext` as Unreal properties so designers can assign them.
- Add the mapping context from the local player subsystem during possession or initialization.
- Bind actions through `UEnhancedInputComponent`.
- Keep input callbacks thin; delegate stateful gameplay to the pawn, components, or dedicated systems.

## Generated code and glue

- Generated outputs often live under `obj/<Configuration>/<TFM>/UnrealSharp.GlueGenerator/...`.
- Use generated files for diagnosis only:
  - confirm the type was discovered
  - confirm the generated name matches expectation
  - confirm interface/class exposure happened
- Do not patch generated files as the source of truth.

## Build and regeneration heuristics

- Saving authored C# lets UnrealSharp compile/reload the managed code automatically. Do not manually copy or move managed build artifacts into an Unreal target directory.
- Run the normal managed build manually after a source change to surface syntax/compiler diagnostics; it is a validation step, not a deployment step.
- After changing reflected types, wait for the automatic compile/reload and run the manual validation build before deciding Unreal cannot see the new shape.
- If the build succeeds but Unreal behaves as if the old contract still exists, inspect generated output and stale binaries before redesigning code.
- Hot reload is useful but not authoritative when metadata shape changes significantly.
- A failed automatic compile can leave a blocking UE modal error dialog open. Close that dialog before any editor/asset/PIE/bridge operation; otherwise UE-side operations may fail or appear unresponsive.

## Lifecycle heuristics

- Use Unreal lifecycle methods that match ownership:
  - module: `StartupModule`, `ShutdownModule`
  - actor/component: `BeginPlay`, `Tick`, `EndPlay`
  - controller: `OnPossess`
  - widget: `OnInitialized`, `Construct`, `Destruct`
- Subscribe as late as practical and unsubscribe on the matching teardown path.
- Cache expensive owner or subsystem lookups once the lifetime is known to be stable.

## Safe default decisions

- Prefer explicit attributes over implicit behavior.
- Prefer existing local UnrealSharp idioms over speculative patterns.
- Prefer changing authored C# plus regeneration over editing generated artifacts.
