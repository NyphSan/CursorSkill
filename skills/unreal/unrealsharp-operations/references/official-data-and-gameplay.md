# Official Data, Gameplay, UI, and Interop Reference

## Scope and freshness

Use this reference for UnrealSharp collections, data assets, developer settings, soft loading, networking, static state, gameplay tags, trace channels, async Blueprint actions, console cheats, widgets, and C++ extension methods.

This is a distilled guide from official documentation checked on 2026-08-05. Verify the installed bindings and local conventions before using an API name in new code.

## Collections

- Use `TArray<T>` for an Unreal-owned reflected array. A UFunction can normally represent a C# list parameter as `IList<T>`.
- Use `TSet<T>` for reflected unique values; use `ISet<T>` in a compatible UFunction signature.
- Use `TMap<TKey, TValue>` for reflected key/value data; use `IDictionary<TKey, TValue>` in a compatible UFunction signature.
- Use `TNativeArray<T>` only where measured copying/marshalling cost makes it worthwhile. It supports numerical primitive types in the current guide and can copy to/from spans or expose a span for in-place access. Keep span lifetimes local; do not retain native-memory spans across Unreal lifetime boundaries.
- Do not call `new TArray<...>()` or `new TMap<...>()` for an Unreal property. Let engine/interop create it, or use a fully managed collection.

## Developer settings and assets

- Create project-settings data by deriving from `UDeveloperSettings`, applying `[UClass(config: "Game")]` (or the appropriate config category), and marking editable persisted values with `PropertyFlags.Config`.
- Do not place hard object references in config settings. Use `TSoftObjectPtr<T>` or `TSoftClassPtr<T>` and resolve them deliberately.
- Read settings through `GetDefault<TSettings>()` rather than creating a settings UObject manually.
- Create a C# primary data asset from `UCSPrimaryDataAsset`. Ensure its `AssetName` agrees with the type registered in Asset Manager settings.
- Load registered primary assets through `UAssetManager` plus the generated `AssetTypes` and `AssetIds` bindings. Allow bundle lists and the async completion path to be explicit in feature code.
- Load `TSoftObjectPtr<T>` / `TSoftClassPtr<T>` using `LoadAsync()`. Expect a null soft reference to fail, an already-loaded reference to complete immediately, and a nonresident asset to load asynchronously. Switch to Unreal context before applying an asynchronously loaded asset to UObjects or widgets.

## Networking

- Replicate a property with `[UProperty(PropertyFlags.Replicated)]`.
- Use `ReplicatedUsing = nameof(OnRep_Name)` when UI or derived state must react to an update. An OnRep method can receive the old value where the binding supports it.
- Set a lifetime condition such as owner-only only when it matches the authority/visibility design.
- Implement RPC behavior with `[UFunction]` plus the appropriate server/client/multicast and optional reliable flags. Follow the installed version's exact enum spelling and use the generated `_Implementation` partial method pattern for the body.
- Leave an RPC unreliable by omitting the reliable flag only when gameplay tolerates loss.
- To replicate a UObject, derive it from `UCSReplicatedObject`, create it on authority with `NewObject<T>()`, store it in a replicated property, and register it with its owning actor or component via `AddReplicatedSubObject`.
- Treat replication validation as a networked test task. Compile success and PIE single-player behavior do not prove authority, ownership, RPC routing, or replication conditions.

## Static state

- Avoid ordinary static references for world-specific state. They can hold UObjects past world teardown or collide across worlds.
- Add the `UnrealSharp.StaticVars` assembly reference only if the project uses it.
- Use `FWorldStaticVar<T>` for data scoped to a `UWorld`; it clears with the world, such as during level transitions.
- Use `FGameStaticVar<T>` for a game-session value. In the editor it resets at PIE boundaries and on managed hot reload.

## Gameplay tags and trace channels

- Read project-defined tags from the generated `GameplayTags` static class. Its members regenerate as project tags change.
- Construct/append `FGameplayTagContainer` from tags, lists, or other containers rather than maintaining parallel string lists.
- For C#-declared tags, keep the returned `FGameplayTag` in the declaring static type. Register that type early, normally from module startup; custom tags may not appear in the global `GameplayTags` class because of initialization timing.
- Use generated `ETraceChannel` names instead of guessing numeric trace-query IDs, then convert with `ToQuery()` for Blueprint-style trace APIs.
- Expect trace-channel bindings to regenerate after collision-settings changes. Removing a channel may require an editor restart due to an engine-side stale-entry issue.

## Async Blueprint actions

- A public reflected method returning `Task`, `Task<T>`, `ValueTask`, or `ValueTask<T>` can become a latent Blueprint action when its result type is reflection-supported.
- Apply `ConfigureWithUnrealContext()` to the actual awaited operation before touching UObjects afterward. Pass a cancellation token when the operation must stop on teardown.
- Validate cancellation, object validity, authority, and relevant world/PIE lifetime after the await. Do not use a zero-delay await as an assumed thread switch.
- Keep expensive I/O or parsing off-thread, but apply actor/component/widget/material/Niagara state on the game thread.

## Cheats and debug commands

- Extend `UCSCheatManagerExtension` for console cheats/debug commands.
- Mark each intended console action with `[UFunction(FunctionFlags.Exec)]`. Keep validation and authority checks appropriate to the development environment; never assume an exec command is safe to expose in a shipping workflow.

## Widgets

- Derive a UI layout from `UUserWidget` or extend a concrete widget type where appropriate.
- Bind a Widget Blueprint child only with both `[UProperty]` and `[BindWidget]`. The Blueprint hierarchy name must exactly equal the C# property name.
- Expose a widget Blueprint class with `TSubclassOf<TWidget>`, create it with `CreateWidget`, and choose a UI owner that matches project input/focus policy.
- `AddToViewport` is a quick path for simple UI. Prefer a project UI stack or CommonUI-style architecture for complex scalable UI if the project already uses one.

## C++ extension/mixin methods

- Expose a C++ method as a C# extension only from a public static method in a `UBlueprintFunctionLibrary`.
- Mark the UFunction with `meta=(ExtensionMethod)` and a callable/script-method form recognized by the installed version. Make its first parameter the native type to extend.
- Search generated extensions before writing a wrapper; call the generated extension from C# rather than duplicating native behavior.

## Official pages

- [Collections](https://www.unrealsharp.com/data-and-asset-management/collections), [TArray](https://www.unrealsharp.com/data-and-asset-management/collections/tarray), [TNativeArray](https://www.unrealsharp.com/data-and-asset-management/collections/tnativearray), [TSet](https://www.unrealsharp.com/data-and-asset-management/collections/tset), and [TMap](https://www.unrealsharp.com/data-and-asset-management/collections/tmap)
- [Developer Settings](https://www.unrealsharp.com/data-and-asset-management/developer-settings), [Primary Data Assets](https://www.unrealsharp.com/data-and-asset-management/primary-data-assets), [Loading Primary Data Assets](https://www.unrealsharp.com/data-and-asset-management/primary-data-assets/loading-assets), and [Loading Soft References](https://www.unrealsharp.com/data-and-asset-management/loading-soft-references)
- [Multiplayer](https://www.unrealsharp.com/gameplay-systems/multiplayer), [Replicated Properties](https://www.unrealsharp.com/gameplay-systems/multiplayer/replicated-properties), [RPCs](https://www.unrealsharp.com/gameplay-systems/multiplayer/rpcs-remote-procedure-calls), and [Replicated UObjects](https://www.unrealsharp.com/gameplay-systems/multiplayer/replicated-uobjects)
- [Static Variables](https://www.unrealsharp.com/gameplay-systems/static-variables), [FWorldStaticVar](https://www.unrealsharp.com/gameplay-systems/static-variables/fworldstaticvar-less-than-t-greater-than), [FGameStaticVar](https://www.unrealsharp.com/gameplay-systems/static-variables/fgamestaticvar-less-than-t-greater-than), [Gameplay Tags](https://www.unrealsharp.com/gameplay-systems/gameplay-tags), [Tag Containers](https://www.unrealsharp.com/gameplay-systems/gameplay-tags/gameplay-tag-container), [C# Tags](https://www.unrealsharp.com/gameplay-systems/gameplay-tags/c-created-gameplay-tags), [Trace Channels](https://www.unrealsharp.com/gameplay-systems/trace-channels), [Async](https://www.unrealsharp.com/gameplay-systems/async), and [Cheats](https://www.unrealsharp.com/gameplay-systems/cheats-debug-commands)
- [Widgets](https://www.unrealsharp.com/ui/widgets), [Create/Compose Widgets](https://www.unrealsharp.com/ui/widgets/create-compose-widgets), [Show Widget On Screen](https://www.unrealsharp.com/ui/widgets/show-widget-on-screen), and [Extension/Mixin Methods](https://www.unrealsharp.com/glue-generation/extension-methods)
