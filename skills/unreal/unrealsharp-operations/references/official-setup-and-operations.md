# Official Setup and Operations

## Scope and freshness

Use this reference for installation, managed-project setup, automatic compilation, debugging, modules, plugins, collaboration, packaging, and known issues.

This is a concise operational digest of the official UnrealSharp documentation checked on 2026-08-05. The installed UnrealSharp version and the project's existing conventions take precedence. Use [official-source-map.md](./official-source-map.md) to open the current official page when a version-sensitive detail matters.

## Product context and support boundaries

- UnrealSharp is an Unreal Engine 5 plugin for C# gameplay/editor tooling. Its central model is automatic C# bindings generated from Unreal reflection, fast managed iteration/hot reload, and access to the broader .NET ecosystem, including NuGet packages.
- The current official home page lists Windows and macOS as supported, with iOS, Android, and Linux planned. Do not treat planned platforms as build/package targets without checking the installed release and project pipeline.
- The official project is MIT-licensed and offers sample projects (Sample Defense Game, Slime Guzzler, and UnrealSharp-Cropout) as implementation references. Prefer a current local project example first, then a sample project when the repository has no comparable pattern.
- Use the official Discord for community support and the published roadmap for feature status. Do not promise dates or assume a roadmap item is released.

## Baseline setup

- Confirm the installed engine/plugin combination before changing dependencies. The current official setup page lists Unreal Engine 5.6-5.8 and .NET SDK 10.0.5+; do not upgrade an existing project merely to match that page.
- Prefer a C++ Unreal project. Install the UE C++ build tools, clone the UnrealSharp source repository into `<ProjectRoot>/Plugins/UnrealSharp`, generate project files, and build through the Unreal/IDE solution.
- Treat a source build as the normal current path unless the project deliberately uses a maintained binary build. UnrealSharp is open source under MIT, but its own FAQ still describes it as not production-ready; establish project-specific release and packaging policy before shipping.
- Do not use simply opening the `.uproject` as the plugin-compilation workflow. The official guide warns that this can leave confusing stale plugin binaries. Launching the editor normally is fine after the project/plugin has been built through its intended workflow.

## Create and place managed projects

- Create a managed project from the UnrealSharp editor toolbar when the editor offers no existing C# project. Choose the project or a plugin as owner.
- Expect authored C# under `<ProjectOrPluginRoot>/Script/<ManagedProject>` and generated interop in a sibling `*.Glue` project. Treat authored C# as source; treat Glue as generated diagnostic output.
- Support plugin-owned C# projects. For an existing plugin, use the toolbar's **Create C# Project**, select that plugin as owner, and let UnrealSharp create the normal structure.
- To change the managed source root, place `UnrealSharp.Settings.json` in `<ProjectRoot>/Config` with a `ScriptDirectoryName` value. After a directory setting change, do a clean rebuild using the project's documented cleanup procedure; the official guide specifically calls out the UnrealSharp `Intermediate` directory.
- If a C++ module is exposed as an assembly rather than source, add a direct `<Reference>` to its `Binaries/Managed/<TFM>/<Module>.dll`. Restart the editor after changing `.csproj` references because project-file reference changes do not hot reload.

## Compilation and hot reload contract

- Saving or changing authored C# causes UnrealSharp to compile/reload code while the editor is open. Let it own managed-output placement and runtime reload.
- Never manually move, copy, or deploy managed artifacts after the automatic compile as a normal development step. A manual build exists to expose syntax and compiler diagnostics, not to provide files that must be relocated.
- Run the managed project's normal build after source changes, especially reflected declarations, public signatures, project-file edits, or before UE automation. Prefer the project's established command; otherwise use the exact managed project path with `dotnet build <ManagedProject.csproj>`.
- Keep the plugin/C++ build separate from the managed validation build. C++ or plugin source changes still require the normal Unreal/IDE build, which can regenerate Glue and bindings.

### Compiler-error modal gate

- A failed UnrealSharp compile can open a modal error dialog and block the UE thread.
- Before driving editor UI, assets, PIE, console commands, or an Unreal bridge, check whether that dialog is present. Read the diagnostic, then close/dismiss the dialog before attempting further UE actions.
- Fix the source, save it to trigger the next automatic compilation, run the managed validation build, and wait for a responsive editor. Do not treat an operation failure while the modal is open as evidence that the underlying UE API or asset is broken.
- If the dialog cannot be closed with the available UI, stop UE-side operations and report the modal as the blocker rather than retrying Unreal calls.

## Generated Glue and regeneration

- Do not edit Glue projects or generated output. They are regenerated whenever the relevant Unreal build/reflection pipeline runs.
- If an engine upgrade or an enabled engine plugin changes reflection data but UnrealBuildTool does not regenerate Glue, identify the exact UnrealSharp plugin folder and remove only its `Intermediate` and `Saved` folders. Then compile through the normal project workflow. Do not delete broad project or workspace directories.
- If a type/property/function is absent after a successful compile, check the authored reflection attributes, `partial` declarations, supported signature, generated output, and stale/editor state before redesigning the feature.

## Debugging and logging

- Launch the managed C# project with the IDE's debugger command (commonly F5) to attach to the Unreal Engine instance after setup.
- Declare custom output-log categories with `[CustomLog]` on a `partial` class, usually `static`. Use the generated `Log`, `LogWarning`, `LogError`, and `LogFatal` methods instead of ad hoc logging conventions when a reusable category helps.
- Keep compilation diagnostics, UE Output Log diagnostics, and runtime stack traces distinct. A successful `dotnet build` does not prove that Blueprint binding, generated Glue, editor state, PIE behavior, or packaging is valid.

## Modules, plugins, and collaboration

- Use `[UModule]` plus `IModuleInterface` for managed module startup/shutdown. Expect both lifecycle methods to run at editor launch/close and during managed assembly reload; make startup idempotent and cleanup complete.
- Retrieve a managed module through `PluginLoader.FindModule<T>()` only when the project genuinely needs module-level ownership.
- To create a new C# plugin, use the UE Plugins window and select a C#-only or C++/C# joint template. Avoid hand-building a parallel plugin layout unless project tooling requires it.
- For teammates without build tooling, generate and distribute an installed build using UnrealSharp's `StageUnrealSharp` RunUAT script. Distribute the generated managed Glue/binaries through the team's normal content workflow; continue distributing C++ game-module binaries using the usual Unreal pipeline.
- The official simulation console variables can validate this distribution path: `UnrealSharp.SimulateNoDotNetSDK 1` and `UnrealSharp.SimulateInstalledBuild 1`. Use them only in a development/test environment.

## Packaging

- Follow the normal UE package/export workflow first. The current official packaging guide lists Windows and macOS support.
- In the editor, use the UnrealSharp toolbar's **Package Project** action and choose the root folder that contains the packaged executable.
- For CI/CD, invoke `RunUAT.bat PackageProject` with the UnrealSharp `Build/Scripts` directory, project path, archive root, UE target type, and build configuration. Add target platform/architecture or user parameters only when the pipeline needs them.
- Validate packaged behavior independently: source compilation and hot reload do not validate cooked assets, managed deployment, platform dependencies, startup order, input focus, or build configuration.

## Known official caveats

- Newtonsoft.Json can conflict with UnrealSharp's AssemblyLoadContext-based hot reload. Check the linked issue/workaround before introducing it or diagnosing reload failures.
- Blueprint and UnrealSharp share reflection limits: functionality not exposed through Unreal reflection is not automatically available to C#. Use C++ interop when the needed native API is not reflected.
- Prefer Blueprint subclasses of C# classes for asset/designer configuration where the project uses that workflow.
- Use `NewObject<T>()`, not `new T()`, to construct a UObject-backed instance.

## Official pages

- [Setup](https://www.unrealsharp.com/getting-started-and-fundamentals/quickstart), [Debugging](https://www.unrealsharp.com/getting-started-and-fundamentals/debugging), [Logging](https://www.unrealsharp.com/getting-started-and-fundamentals/logging), and [Module Lifecycle](https://www.unrealsharp.com/getting-started-and-fundamentals/module-lifecycle)
- [Packaging](https://www.unrealsharp.com/getting-started-and-fundamentals/packaging), [Editor packaging](https://www.unrealsharp.com/getting-started-and-fundamentals/packaging/packaging-via-unreal-editor), and [CI/CD packaging](https://www.unrealsharp.com/getting-started-and-fundamentals/packaging/packaging-via-ci-cd-command-line)
- [C# plugins](https://www.unrealsharp.com/getting-started-and-fundamentals/c-plugins), [collaboration](https://www.unrealsharp.com/getting-started-and-fundamentals/collaborating-with-unrealsharp), [C++ interop assemblies](https://www.unrealsharp.com/getting-started-and-fundamentals/referencing-c++-interop-assemblies), and [script-directory settings](https://www.unrealsharp.com/unrealsharp-settings/change-script-directory-name)
- [FAQ](https://www.unrealsharp.com/faq) and [Known Issues](https://www.unrealsharp.com/known-issues)
