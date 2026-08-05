# Troubleshooting

## Scope

Use this file when UnrealSharp code compiles, partially works, or fails in a way that suggests reflection, binding, generation, or runtime contract drift.

## Contents

- First-pass diagnosis and compilation/modal gate
- Reflection discovery, widget binding, and input failures
- Event/lifecycle, hot reload/stale state, and risky-edit review

## First-pass diagnosis

Classify the problem before editing:

- Build/configuration:
  - managed project does not build
  - glue project not referenced or props import wrong
- Reflection exposure:
  - Unreal cannot see a class, property, or function
- Widget or Blueprint binding:
  - `BindWidget` member is null
  - assigned class/property is missing at runtime
- Input wiring:
  - action never fires
  - mapping context missing
- Runtime orchestration:
  - events fire in wrong order
  - focus mode, state mode, or ownership conflicts
- Stale generation/hot reload:
  - code changed but Unreal still behaves like the old contract

## Compilation, automatic reload, and blocking dialogs

UnrealSharp compiles/reloads authored C# after code changes or saves. Let that automatic workflow place its managed output; do **not** manually move/copy artifacts into project, plugin, or game directories.

Still run the normal managed-project build after a change to catch syntax and compiler errors. Use the established project command, or `dotnet build <ManagedProject.csproj>` when appropriate. A successful manual build validates source; it is not a request to deploy its output manually.

If automatic compilation fails:

1. Check for the UnrealSharp compiler-error modal.
2. Read/record the diagnostic and close the dialog before calling UE APIs, operating editor UI, changing assets, or launching PIE.
3. Fix the source and save it to trigger another automatic compile.
4. Run the managed validation build and wait for a responsive editor before continuing.

The modal can block the UE thread. Do not diagnose failed UE operations while it remains open. If it cannot be dismissed with available UI, stop UE-side work and report that explicit blocker.

## Reflection and discovery failures

If Unreal cannot see a type or member:

1. Confirm the authored type/member has the required attribute.
2. Confirm the declaration follows a known working local pattern.
3. Confirm `partial` is present where UnrealSharp expects it.
4. Inspect generated output under `obj/.../UnrealSharp.GlueGenerator/...`.
5. Rebuild before assuming the design is wrong.

Typical causes:

- missing `[UClass]`
- missing `[UProperty]` or `[UFunction]`
- missing `partial`
- unsupported or inconsistent signature
- stale generated metadata

## Widget binding failures

If a bound widget or animation is null:

1. Check the C# property name against the widget blueprint object name.
2. Check the C# bound type against the actual blueprint widget type.
3. Check whether the control is actually marked and present in the widget tree.
4. Check whether the widget instance being created is the intended subclass.

Prefer fixing the contract mismatch over adding defensive null-tolerant behavior that hides the real problem.

## Input failures

If input callbacks do not fire:

1. Confirm the mapping context property is assigned.
2. Confirm the controller adds the mapping context on possession/initialization.
3. Confirm `InputComponent` is the enhanced input variant before binding.
4. Confirm the pawn/controller actually owns the relevant input path.
5. If UI mode is active, inspect whether focus/input mode is intentionally diverting the action.

## Event and lifecycle failures

If behavior duplicates, leaks, or fires after teardown:

1. Inspect every static/global event subscription.
2. Confirm each subscription has a matching unsubscribe path.
3. Check whether `Initialize`-style methods can run more than once.
4. If they can, guard against duplicate subscription before re-adding handlers.

## Hot reload and stale state

If a metadata or binding change is ignored:

- first ensure that no compilation-error modal is blocking the editor
- save the source and allow the automatic compile/reload to complete
- rebuild the managed project only to validate diagnostics; do not move its output
- inspect generated outputs
- verify the resulting binaries are the ones Unreal is loading

Treat hot reload as an optimization, not as proof that reflection state is current.

## Review checklist for risky edits

- Did a reflected signature change?
- Did a widget/control/property name change?
- Did ownership move across actor/controller/widget boundaries?
- Did an event subscription path change?
- Did a new `Tick` responsibility appear without cache or gating?
- Did this change rely on generated code updating implicitly?
