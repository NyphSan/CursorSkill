---
name: unrealsharp-operations
description: Build, debug, review, set up, package, and extend Unreal Engine projects that use UnrealSharp and C#. Use when working on UnrealSharp setup, automatic C# compilation/hot reload, compiler-error editor dialogs, generated Glue projects, UClass/UProperty/UFunction usage, actor or component authoring, widgets/UMG binding, Enhanced Input, interfaces, Blueprint interop, C# gameplay code, assets, networking, UnrealSharp hot reload issues, packaged-build differences, or UnrealSharp project architecture.
---

# UnrealSharp Operations

Use this skill for UnrealSharp work in Unreal Engine projects.

## Core Rule

Assume most Blueprint nodes and Unreal C++ helpers already have C# bindings. Before writing a math helper, lifecycle workaround, reflection wrapper, UI utility, or engine-like abstraction:

1. Search local code for the same operation.
2. Search generated Glue or UnrealSharp extensions for the native binding.
3. Prefer the engine/UnrealSharp API over reimplementing it.
4. Only write a helper when the project already has no suitable API and the helper adds project-specific behavior.

Examples: prefer `FVector.DistanceSquared`, `FVector.Lerp`, component `WorldLocation`, actor `SetActorLocation`, `SystemLibrary.GetObjectName`, trace/navigation helpers, widget APIs, and existing project services over hand-rolled duplicates.

## Compilation, Hot Reload, and Editor Modal Gate

- Treat authored C# changes and saves as an UnrealSharp-triggered compile/reload event. Let UnrealSharp update its managed output; do **not** manually copy or move compiled managed artifacts into the project, plugin, or packaged-game directories during normal iteration.
- Still run the project's normal managed build after a source change, especially after reflection, signature, or project-file changes, to validate syntax and diagnostics. That build is a validation step, not a deployment step, and does not require moving its output afterward.
- Distinguish user-script compilation from Unreal C++/plugin compilation. Build C++ through the project's normal IDE/Unreal build workflow when C++ or plugin sources change; do not attempt to replace that workflow by copying C# outputs.
- Treat a failed UnrealSharp compilation as an editor-operation gate. It can open a modal error dialog that blocks the Unreal Engine thread. Before invoking any editor, asset, PIE, or Unreal-bridge operation: read the error, close/dismiss the dialog, then confirm the editor is responsive. Do not continue UE automation while the dialog remains open.
- After closing a compilation-error dialog, fix the source, save to trigger the next automatic compile, run the manual validation build, and only then resume Unreal operations. If the dialog cannot be closed through the available UI, stop UE-side work and report that it is blocked.

## Quick Workflow

1. Before any UE-side action, check for an UnrealSharp compiler-error modal; read and close it if present.
2. Identify the Unreal-side type being changed: actor, component, widget, controller, subsystem, interface, module, data asset, networking type, or pure C# helper.
3. Read the relevant authored C# file and one nearby known-good example of the same category.
4. If API availability is uncertain, search before implementing:
   - local usage: `rg "MethodName|TypeName" <project>`
   - generated Glue: `rg "MethodName" <UnrealSharp>/Generated -g "*.cs"`
   - UnrealSharp extensions: `rg "MethodName" <UnrealSharp>/Extensions -g "*.cs"`
5. Distinguish framework rules from project rules:
   - Framework rules: attributes, `partial`, generated Glue, Blueprint-visible signatures, component declarations.
   - Project rules: event buses, naming, save systems, UI flow, AI/gameplay protocols, hot reload expectations.
6. Make the smallest source change that fits the existing architecture, then save and allow UnrealSharp to automatically compile/reload it.
7. Run the normal managed build manually to surface syntax/compiler errors. Do not move the resulting artifacts.
8. If compilation fails, close any blocking UE dialog before inspecting logs, editing assets, running PIE, or making another UE call. Inspect generated code only when reflection/binding is suspicious.

## Read The Right Reference

- For reflection syntax and binding constraints, read [references/framework-basics.md](./references/framework-basics.md).
- For actors, components, widgets, input, and interfaces, read [references/gameplay-patterns.md](./references/gameplay-patterns.md).
- For common APIs, snippets, and "do not reimplement this" checks, read [references/api-cheatsheet.md](./references/api-cheatsheet.md).
- For repository-specific conventions, read [references/project-patterns.md](./references/project-patterns.md).
- For hot reload, generated Glue, and packaging diagnosis, read [references/troubleshooting.md](./references/troubleshooting.md).
- For setup, automated compilation, tooling, modules, C# plugins, collaboration, packaging, and known issues, read [references/official-setup-and-operations.md](./references/official-setup-and-operations.md).
- For official reflection, component, delegate, subsystem, metadata, and helper-method details, read [references/official-framework.md](./references/official-framework.md).
- For official collections, assets, networking, static state, tags, trace channels, async, UI, and extension-method details, read [references/official-data-and-gameplay.md](./references/official-data-and-gameplay.md).
- For the complete official-page coverage map and live source links, read [references/official-source-map.md](./references/official-source-map.md).

## UnrealSharp Authoring Rules

- Add `[UClass]` to Unreal-exposed classes and make them `partial`.
- Add `[UProperty]` only for editor assignment, Blueprint access, binding, serialization, or default component declarations.
- Add `[UFunction]` only when Unreal/Blueprint/input/delegates must discover the method.
- For Blueprint-overrideable C# methods, declare the exported method as `partial` with `BlueprintEvent`, and put the managed default behavior in the matching `_Implementation` partial method. Do not place the normal method body on the exported declaration.
- Keep pure implementation details as normal C# members.
- Use `TSubclassOf<T>` for assignable classes and direct `UObject` refs for assignable instances/assets.
- Use `DefaultComponent`, `RootComponent`, and `AttachmentComponent` for C#-declared component hierarchies.
- Match callback signatures to known-good local examples before inventing new delegate/input signatures.
- Treat generated Glue as diagnostic output, not source.

## Engine API First

Before hand-writing helpers, check these common UnrealSharp/engine equivalents:

- Vectors/math: `FVector.Lerp`, `FVector.Distance`, `FVector.DistanceSquared`, `Math.Clamp`, `MathLibrary.*` if present locally.
- Transforms: `ActorLocation`, `ActorRotation`, `ActorScale3D`, `SetActorLocation`, `SetActorRotation`, `USceneComponent.WorldLocation`, `RelativeLocation`, `RelativeRotation`, `RelativeScale3D`.
- Object identity: `SystemLibrary.GetObjectName`, `SystemLibrary.GetObjectPathString`, `GetType().Name` only for managed type identity.
- Traces: `SystemLibrary.LineTraceByChannel`, `SphereTrace...`, project-standard trace channels.
- Navigation: `AAIController.MoveToLocation`, `UNavigationSystemV1.ProjectPointToNavigation`, local AI move pipelines.
- Widgets: `CreateWidget<T>`, `AddToViewport`, `BindWidget`, `BindWidgetAnim`, panel `AddChild`/`RemoveChild`.
- Timers/async: project timer APIs if present; otherwise resume to Unreal context with `ConfigureWithUnrealContext()` before touching engine objects.
- Visibility/collision: `SetVisibility`, `ActorHiddenInGame`, `ActorEnableCollision`, primitive collision profile helpers.

If a Blueprint node exists, assume there may be a generated static method under a `*Library` class or an instance method on the corresponding type.

## Actor And Component Patterns

- Actor owns scene hierarchy and actor-level state.
- Component owns reusable behavior attached to one actor.
- Controller owns input mode, UI orchestration, possession-related input wiring.
- Widget owns presentation and UI events; gameplay decisions should flow back to a controller/actor/service.
- Subsystem or manager owns global lifetime when the engine/project already has that pattern.
- Use event-driven or interval-driven logic for many distance checks; do not add many independent high-frequency ticks unless required.
- For distance checks, cache stable references and use squared distance when comparing to a radius.
- For overlap-triggered state, store enough state for load/rebuild if the project has a save system.

## UMG And Blueprint Binding

- `BindWidget` names must match the widget Blueprint hierarchy exactly.
- `BindWidgetAnim` usually needs `Transient`.
- If a required binding is missing, fail clearly; do not hide contract errors behind broad fallback code.
- For dynamic lists, create entries from `TSubclassOf<TEntryWidget>` and drive layout/animation in C# only when the list is runtime-sized.
- If keyboard/gamepad focus matters, centralize input mode and focus restoration in the controller or UI owner.
- If behavior differs in packaged builds, suspect input mode, focus, viewport scale, timing, or stale Blueprint bindings before redesigning.

## Async, Events, And Lifetime

- Subscribe in `BeginPlay`, `OnPossess`, `OnInitialized`, or `Construct` according to owner lifetime.
- Unsubscribe in the matching `EndPlay` or `Destruct`.
- For static/global events, use `-=` before `+=` when rebinding to avoid duplicate handlers.
- Avoid fire-and-forget unless errors are intentionally non-fatal and logged.
- After any `await`, assume the continuation may not be on the game thread unless the awaited operation preserved Unreal context.
- Apply `ConfigureWithUnrealContext()` to the real asynchronous operation whose continuation needs Unreal access, such as `await Task.Delay(ms).ConfigureWithUnrealContext()`. Avoid `await Task.Delay(0).ConfigureWithUnrealContext()` as a hard "switch to game thread" after `ConfigureAwait(false)`; a completed task may not reliably schedule a new game-thread continuation.
- If code has already resumed on a pool/background thread and must touch UObjects, use or add an explicit project helper that posts to `UnrealSynchronizationContext(NamedThread.GameThread)` and completes a `TaskCompletionSource` from that callback. Prefer `RunOnGameThreadAsync(Action)` / `SwitchToGameThreadAsync()` style helpers over ad hoc zero-delay awaits.
- Treat `IsValid()` and null checks as lifetime checks, not thread-safety checks. A valid actor/component can still crash or trip data-race detection when accessed off the game thread.
- Keep external I/O, HTTP, hardware polling, file scanning, and process enumeration off-thread, but copy only plain data across the boundary; apply results to actors, components, widgets, materials, Niagara, collision, transforms, or text on the game thread.
- In async loops, stop using an epoch/version/cancellation pattern tied to `EndPlay`/`Destruct`.
- In delayed actor/component work, combine cancellation/epoch guards, runtime-shutdown checks, object validity checks, and game-thread switching before the first UObject access.
- Avoid calling render-, physics-, collision-, material-, Niagara-, widget-, or transform-related APIs from task continuations that used `ConfigureAwait(false)` until they have explicitly returned to the game thread.

## Save/Load And Persistent State

- Keep generic actor state in reusable save components when the project provides them.
- Keep business state in narrow provider interfaces or subsystem save hooks.
- Restore in an order that respects dependencies: base systems, actor transform/visibility, then behavior-specific reconstruction.
- Do not serialize callbacks, delegates, lambdas, transient async operations, or in-flight navigation unless the project explicitly supports that.
- On load, rebuild tasks/prompts/choices from saved high-level state rather than saving live task/choice execution objects.

## Common Diagnostics

- If Unreal cannot see a type/member: check `[UClass]`, `[UProperty]`, `[UFunction]`, `partial`, namespace, supported signature, generated Glue output, and stale binaries.
- If Blueprint binding is null: check Blueprint control name, C# property name, widget type, and whether the Blueprint actually contains the control.
- If input works in editor but not packaged: check focus, input mode, trigger phase, mapping context priority, duplicate handlers, and UI consuming the key.
- If an UnrealSharp compilation fails: first close its blocking modal dialog; it can prevent further UE operations from executing correctly. Fix the source, save to trigger automatic compilation, then run the managed build for diagnostics without moving artifacts.
- If hot reload behaves strangely: after ensuring no modal is open, run the managed validation build, inspect generated Glue, and restart the editor before making architectural changes.
- If C# compilation succeeds but Unreal still uses old metadata: suspect stale generated artifacts or editor hot reload cache.
- If packaged behavior differs from PIE: verify initialization order, viewport/screen scale, asset references, cooked assets, and config defaults.
- If the editor crashes later while idle or during shutdown, inspect earlier PIE/editor log lines too. A prior handled ensure can corrupt or leave native state unstable before the final access violation appears.
- If logs show `NiagaraShared.cpp` `IsInGameThread`, `MTAccessDetector` data-race messages, `PrimitiveComponent.SetCollisionProfileName`, `ActorComponent.Activate`, or `UnrealSharpCore EvaluateInvokePath`, suspect a C# continuation or callback touched engine objects off the game thread.
- If crashes appear as `Engine`/`RenderCore` access violations with little managed stack, correlate with earlier script stacks, ensures, material/Niagara/collision warnings, and recent async or editor-callable code rather than assuming the final call stack is the root cause.
- If material or component setup emits repeated invalid slot warnings, use engine metadata/count APIs or explicit assigned references instead of probing many possible slots through native calls.

## Completion Checklist

- Confirm the change follows local UnrealSharp patterns for the same type category.
- Confirm no engine helper was reimplemented unnecessarily.
- Confirm required Blueprint/widget/component names still match code contracts.
- Confirm event subscriptions have matching teardown.
- Confirm async code touches Unreal objects only after a real Unreal-context continuation or explicit game-thread switch, not merely after a zero-delay task.
- Confirm delayed/fire-and-forget work cannot outlive its actor/component, PIE session, map, or hot reload lifecycle.
- Save C# changes and allow UnrealSharp to compile/reload them automatically; do not manually move managed build artifacts.
- Run the managed build to validate syntax/compiler errors after the source change.
- Confirm no UnrealSharp compiler-error modal remains open before any UE/editor automation.
- Report whether the result is source-safe, compile-validated, editor-validated, or runtime/package-validated.
