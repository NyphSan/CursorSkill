# Official Reflection and Framework Reference

## Scope and freshness

Use this reference for official UnrealSharp rules around reflection, classes, properties, functions, components, helper APIs, structs, enums, interfaces, delegates, subsystems, and metadata.

The details below are a compact, version-aware digest of official documentation checked on 2026-08-05. Follow the installed UnrealSharp binding names and a known-good local declaration if they differ from the current public examples.

## Reflection boundary

- Make a class Unreal-visible by deriving from a valid `UObject`-based type, applying `[UClass]`, and declaring it `partial`.
- Expose only members that need reflection, editor access, Blueprint access, serialization, delegates, input, replication, or generated binding. Keep implementation-only members as normal C#.
- Treat reflection as the shared constraint of Blueprints and UnrealSharp. If a native C++ API is not reflected, C# cannot assume it is callable; search generated bindings or add intentional C++ interop.

## Properties and native getter/setter behavior

- Declare ordinary generated properties as `[UProperty(...)] public partial T Name { get; set; }`. Use only supported property types and flags.
- The source generator produces C# properties for suitable C++ `Get*` and `Set*` UFunctions, including common world-context/out-parameter getter patterns. Prefer the generated property rather than wrapping the native function manually.
- UnrealSharp also honors C++ native getter/setter metadata and routes generated property access through those native methods. Do not bypass that contract by writing directly to unmanaged memory or recreating a backing state.
- A reflected `UProperty` can use a custom ordinary C# getter/setter when its type is supported; such a manually implemented property does not require a `partial` member declaration.
- Do not allocate `TArray<T>` or `TMap<TKey, TValue>` with `new` for an Unreal-exposed property. The engine/interop layer provides the instance. Use `IList<T>` or `IDictionary<TKey, TValue>` for purely managed collections that the code owns.

## Functions and flags

- Use `[UFunction]` only where Unreal must discover the method.
- Use a callable/pure flag for Blueprint-callable functions. Keep pure functions cheap and side-effect-free; Blueprint may reevaluate them often.
- For Blueprint-overridable behavior, declare a `partial` method with `BlueprintEvent` and implement the default behavior in the generated-name `<Method>_Implementation` partial method. Do not place the body on the exported event declaration.
- Use the exact function-flag enum names in the installed version. The current official documentation uses server/client/multicast behavior in both a flag reference and RPC examples; verify the generated API before assuming whether it spells these as `Server`/`Client`/`NetMulticast` or `RunOnServer`/`RunOnClient`/`Multicast`.
- Relevant behavior flags include Blueprint authority-only, callable, cosmetic, event, pure, console-exec, client, server, multicast, and reliable. Use reliability only where the gameplay contract justifies its cost.

## Declarative component hierarchies

- Declare a default component with `DefaultComponent = true`. Mark exactly one appropriate scene component as `RootComponent = true`.
- Attach child default components by naming the parent through `AttachmentComponent = nameof(...)`; use `AttachmentSocket` when the parent socket is part of the contract.
- Override a native actor component only through the supported `[OverrideComponent]` pattern, specifying the replacement type and native property name. Prefer the generated direct accessor instead of repeated casts.
- Use generated helper APIs when runtime construction is truly necessary: actor `Spawn(...)`, component `Get(actor)`, and `Construct(...)`. Do not replace declarative default components with runtime construction without a feature reason.
- For custom helper/mixin generation, enable the installed version's extension source generator in the managed project only when the project actually needs generated helpers.

## Structs and enums

- Expose a struct with `[UStruct]` and `partial`. Use reflected fields/properties only for data that must cross the Unreal boundary; record structs are supported by the current official guide.
- Expose an enum with `[UEnum]` and `byte` as its underlying type when it is used in Unreal properties or function parameters. Treat the byte underlying type as an Unreal constraint, not a stylistic preference.

## Interfaces

- Declare an Unreal interface with `[UInterface] public partial interface I...`. Keep Unreal-callable `[UFunction]` declarations on the interface contract, not on its implementing method.
- Cast directly for an interface implemented by C++ or C#.
- For an interface implemented only in Blueprint, use `AsInterface<T>()` to create the callable wrapper. A normal C# cast cannot discover Blueprint-only implementation.

## Delegates

- Expose delegate types with `[UMultiDelegate]` or `[USingleDelegate]` and reflection-supported parameters.
- Expose multicast properties as `TMulticastDelegate<T>` with the appropriate property flag, commonly `BlueprintAssignable`. Use `TDelegate<T>` for single delegates where reflection is needed.
- Mark callbacks for Unreal-exposed delegates with `[UFunction]`, then subscribe/unsubscribe with the delegate API. Pair every subscription with lifecycle teardown.
- Remember the engine limitation: a single-delegate property cannot be Blueprint-exposed in the same way as a multicast property.

## Subsystems

- Use an engine-managed subsystem rather than a hand-rolled global singleton when its lifetime should belong to engine, game instance, world, or local player. Subsystems are not replicated.
- Inherit from the C# wrapper types required by UnrealSharp: `UCSWorldSubsystem`, `UCSGameInstanceSubsystem`, `UCSEngineSubsystem`, or `UCSLocalPlayerSubsystem`.
- Retrieve them through the matching `GetWorldSubsystem<T>()`, `GetGameInstanceSubsystem<T>()`, `GetEngineSubsystem<T>()`, or `GetLocalPlayerSubsystem<T>(controller)` helper.
- Gate a world subsystem with `DoesSupportWorldType` where PIE/game/editor worlds need different behavior, and initialize/teardown according to the engine-managed lifecycle.

## Metadata

- Apply known metadata through dedicated attributes such as `[Category("...")]` where available.
- Use `[UMetaData("Key", "Value")]` for a supported key that has no dedicated attribute.
- Create custom metadata by decorating a custom attribute class with `[CustomMetaData]`. The generator derives the metadata key from the attribute name (without the `Attribute` suffix) and uses its first constructor argument as the value.

## Official pages

- [Classes](https://www.unrealsharp.com/unreal-framework/classes), [Properties](https://www.unrealsharp.com/unreal-framework/classes/properties), [C++ function properties](https://www.unrealsharp.com/unreal-framework/classes/properties/c++-functions-as-c-properties), [native getter/setter properties](https://www.unrealsharp.com/unreal-framework/classes/properties/c++-properties-with-getters-setters), and [custom C# getters/setters](https://www.unrealsharp.com/unreal-framework/classes/properties/custom-c-getter-setter)
- [Functions](https://www.unrealsharp.com/unreal-framework/classes/functions), [function flags](https://www.unrealsharp.com/unreal-framework/classes/functions/specifiers), [default components](https://www.unrealsharp.com/unreal-framework/classes/default-actor-components), and [helper methods](https://www.unrealsharp.com/unreal-framework/classes/helper-methods)
- [Structs](https://www.unrealsharp.com/unreal-framework/structs), [Enums](https://www.unrealsharp.com/unreal-framework/enums), [Interfaces](https://www.unrealsharp.com/unreal-framework/interfaces), [Delegates](https://www.unrealsharp.com/unreal-framework/delegates), [Subsystems](https://www.unrealsharp.com/unreal-framework/subsystems), and [Metadata](https://www.unrealsharp.com/unreal-framework/metadata)
