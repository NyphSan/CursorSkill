# API Cheatsheet

Use this as a fast reference for common UnrealSharp patterns. The first rule is always: search for an existing UnrealSharp/engine binding before writing your own helper. Most Blueprint-exposed operations are available either as instance methods, generated `*Library` static methods, or project wrappers.

## Contents

- Search and managed-module setup
- Actor, default-component, actor-component, and scene-component patterns
- Editor-assigned assets/classes and `UFunction` patterns
- Math/transforms, distance checks, enhanced input, and widgets
- Events, async/game-thread return, overlaps, traces, navigation, and physics
- Save-provider, interface/capability, Blueprint/package, and pre-edit checks

## Search Before Implementing

Common searches:

```powershell
rg "FVector\.Lerp|DistanceSquared|LineTraceByChannel|SphereTrace|ProjectPointToNavigation" -g "*.cs"
rg "CreateWidget|BindWidget|BindWidgetAnim|AddToViewport|SetRenderTranslation" -g "*.cs"
rg "MoveToLocation|AddMappingContext|BindAction|SetActorLocation|SetActorRotation" -g "*.cs"
rg "public static .*Lerp|DistanceSquared|LineTrace|ProjectPoint" "<UnrealSharpRoot>" -g "*.cs"
```

Prefer the found engine API unless a project-specific wrapper clearly owns the behavior.

## Minimal Module

```csharp
using UnrealSharp.Engine.Core.Modules;

namespace MyManagedProject;

public class FMyManagedProject : IModuleInterface
{
    public void StartupModule()
    {
    }

    public void ShutdownModule()
    {
    }
}
```

Use modules for managed startup/shutdown wiring, not per-level gameplay state.

## Actor

```csharp
using UnrealSharp.Attributes;
using UnrealSharp.Engine;

namespace MyGame;

[UClass]
public partial class AMyActor : AActor
{
    public override void BeginPlay()
    {
        base.BeginPlay();
    }

    public override void Tick(float deltaSeconds)
    {
        base.Tick(deltaSeconds);
    }
}
```

Only enable tick when the behavior truly needs per-frame work.

## Actor With Default Components

```csharp
using UnrealSharp.Attributes;
using UnrealSharp.Engine;

namespace MyGame;

[UClass]
public partial class AMyActor : AActor
{
    [UProperty(DefaultComponent = true, RootComponent = true)]
    public partial USceneComponent Root { get; set; }

    [UProperty(DefaultComponent = true, AttachmentComponent = nameof(Root))]
    public partial USceneComponent VisualRoot { get; set; }

    [UProperty(DefaultComponent = true, AttachmentComponent = nameof(VisualRoot))]
    public partial UStaticMeshComponent Mesh { get; set; }
}
```

Use declarative component properties first. Do not build a parallel hierarchy manually unless runtime construction is the actual feature.

## Actor Component

```csharp
using UnrealSharp.Attributes;
using UnrealSharp.Engine;

namespace MyGame;

[UClass]
public partial class UMyComponent : UActorComponent
{
    [UProperty(PropertyFlags.EditAnywhere | PropertyFlags.BlueprintReadWrite)]
    public partial float Radius { get; set; } = 300.0f;

    public override void BeginPlay()
    {
        base.BeginPlay();
    }
}
```

Use `USceneComponent` instead of `UActorComponent` when the component needs a transform or should be attachable in a scene hierarchy.

## Scene Component

```csharp
using UnrealSharp.Attributes;
using UnrealSharp.Engine;

namespace MyGame;

[UClass]
public partial class UMySceneComponent : USceneComponent
{
    private FVector _initialWorldLocation;

    public override void BeginPlay()
    {
        base.BeginPlay();
        _initialWorldLocation = WorldLocation;
    }
}
```

When attached to another actor, cache both component world transform and owner actor world transform if behavior depends on their relationship.

## Editor Assigned Assets And Classes

```csharp
[UProperty(PropertyFlags.EditAnywhere)]
public partial UInputMappingContext InputContext { get; set; }

[UProperty(PropertyFlags.EditAnywhere)]
public partial UInputAction InteractAction { get; set; }

[UProperty(PropertyFlags.EditAnywhere)]
public partial TSubclassOf<UMyWidget> WidgetClass { get; set; }

[UProperty(PropertyFlags.EditAnywhere)]
public partial AActor TargetActor { get; set; }
```

- Direct object refs are for specific editor-assigned objects/assets.
- `TSubclassOf<T>` is for editor-assigned classes that code instantiates later.
- Required assignments should fail clearly when missing; optional assignments should be documented as optional.

## UFunction

```csharp
[UFunction]
private void Interact()
{
}
```

If Unreal, Blueprint, input, or a delegate does not need to find the method, leave it as a normal C# method.

Blueprint event style:

```csharp
[UFunction(FunctionFlags.BlueprintEvent)]
public partial void OnSequenceStarted();
```

Use the local project's known-good syntax for Blueprint events because generated signatures can vary by UnrealSharp version.

## Common Math And Transform APIs

Use existing APIs first:

```csharp
var distanceSquared = FVector.DistanceSquared(a, b);
var distance = FVector.Distance(a, b);
var current = FVector.Lerp(start, end, alpha);
var clamped = Math.Clamp(value, 0.0f, 1.0f);
```

Common actor/component transform members:

```csharp
var actorLocation = ActorLocation;
SetActorLocation(targetLocation, false, out _, false);
SetActorRotation(targetRotation, false);

var componentLocation = SomeComponent.WorldLocation;
SomeComponent.SetWorldLocation(componentTarget, false, out _, false);
SomeComponent.RelativeLocation = FVector.Zero;
```

Before writing `LookAt`, interpolation, angle normalization, screen projection, or transform conversion code, search for `MathLibrary`, `GameplayStatics`, `WidgetLayoutLibrary`, `PlayerController` methods, and local wrappers.

## Distance Checks

```csharp
private float _radiusSquared;

public override void BeginPlay()
{
    base.BeginPlay();
    _radiusSquared = Radius * Radius;
}

private bool IsNear(FVector a, FVector b)
{
    return FVector.DistanceSquared(a, b) <= _radiusSquared;
}
```

For many objects, prefer one manager/trigger doing interval updates over every component ticking every frame.

## Enhanced Input

```csharp
using System;
using UnrealSharp.Attributes;
using UnrealSharp.EnhancedInput;
using UnrealSharp.Engine;

[UClass]
public partial class AMyPlayerController : APlayerController
{
    [UProperty(PropertyFlags.EditAnywhere)]
    public partial UInputMappingContext InputContext { get; set; }

    [UProperty(PropertyFlags.EditAnywhere)]
    public partial UInputAction MoveAction { get; set; }

    public override void OnPossess(APawn possessedPawn)
    {
        base.OnPossess(possessedPawn);

        var subsystem = GetLocalPlayerSubsystem<UEnhancedInputLocalPlayerSubsystem>(this)
            ?? throw new InvalidOperationException("Missing enhanced input subsystem.");

        subsystem.AddMappingContext(InputContext, 0);

        var enhancedInput = InputComponent as UEnhancedInputComponent
            ?? throw new InvalidOperationException("InputComponent is not enhanced input.");

        enhancedInput.BindAction(MoveAction, ETriggerEvent.Triggered, Move);
    }

    [UFunction]
    private void Move(FInputActionValue value, float elapsed, float triggered, UInputAction action)
    {
        var axis = value.GetAxis2D();
    }
}
```

If an action does not fire, compare against a known-working action in the same controller: mapping context, trigger event, function signature, input mode, UI focus, and duplicate consumers.

## Widget Binding

```csharp
using UnrealSharp.Attributes;
using UnrealSharp.Core.Attributes;
using UnrealSharp.UMG;

[UClass]
public partial class UMyWidget : UUserWidget
{
    [UProperty, BindWidget]
    public partial UTextBlock TitleText { get; set; }

    [UProperty, BindWidget]
    public partial UButton ConfirmButton { get; set; }

    [UProperty(PropertyFlags.Transient), BindWidgetAnim]
    public partial UWidgetAnimation IntroAnim { get; set; }

    public override void OnInitialized()
    {
        base.OnInitialized();
        ConfirmButton.OnClicked += Confirm;
    }

    public override void Destruct()
    {
        ConfirmButton.OnClicked -= Confirm;
        base.Destruct();
    }

    private void Confirm()
    {
    }
}
```

Required bindings should be direct. Do not add broad null-tolerant code that hides Blueprint hierarchy mistakes.

## Create And Show Widgets

```csharp
private UMyWidget _widget;

private void ShowWidget()
{
    _widget = CreateWidget<UMyWidget>(WidgetClass)
        ?? throw new InvalidOperationException("Failed to create UMyWidget.");

    _widget.AddToViewport();
}

private void HideWidget()
{
    _widget.RemoveFromParent();
}
```

For dynamic lists, create entry widgets from a `TSubclassOf<TEntryWidget>` and let C# drive per-entry data and animation when item count is runtime-defined.

## Widget Layout And Animation

```csharp
Entry.RenderOpacity = 1.0f;
Entry.SetRenderTranslation(new FVector2D(0.0f, -80.0f));
```

Search local/generated APIs before writing layout math. Useful classes often include `WidgetLayoutLibrary`, slot types such as `UCanvasPanelSlot`, and widget render transform helpers.

## Static Event Hub

```csharp
public override void BeginPlay()
{
    base.BeginPlay();
    EventCenter.OnSomething -= OnSomething;
    EventCenter.OnSomething += OnSomething;
}

public override void EndPlay(EEndPlayReason endPlayReason)
{
    EventCenter.OnSomething -= OnSomething;
    base.EndPlay(endPlayReason);
}

private void OnSomething()
{
}
```

Use matching teardown for every global/static subscription. `-=` before `+=` avoids duplicate handlers across reloads.

## Async Back To Unreal Context

```csharp
private async Task RunAsync()
{
    await Task.Delay(250).ConfigureWithUnrealContext();
    SetActorLocation(ActorLocation + FVector.UpVector * 50.0f, false, out _, false);
}
```

Do not touch actors, components, widgets, or engine objects after an `await` unless execution is back on the Unreal context.

For long async flows, keep an epoch/cancel token:

```csharp
private int _flowEpoch;

private async Task RunFlowAsync()
{
    var epoch = ++_flowEpoch;
    await Task.Delay(1000).ConfigureWithUnrealContext();
    if (epoch != _flowEpoch)
    {
        return;
    }
}

public override void EndPlay(EEndPlayReason endPlayReason)
{
    _flowEpoch++;
    base.EndPlay(endPlayReason);
}
```

## Overlap

```csharp
public override void ActorBeginOverlap(AActor otherActor)
{
    base.ActorBeginOverlap(otherActor);

    if (otherActor is AMyPlayer player)
    {
        StartForPlayer(player);
    }
}

public override void ActorEndOverlap(AActor otherActor)
{
    base.ActorEndOverlap(otherActor);
}
```

For component overlap delegates, copy the exact delegate signature from generated code or a local working example.

## Trace

```csharp
ETraceTypeQuery traceChannel = ETraceChannel.Camera.ToQuery();
var hasHit = SystemLibrary.LineTraceByChannel(
    this,
    start,
    end,
    traceChannel,
    false,
    ignoreActors,
    EDrawDebugTrace.None,
    out FHitResult hit,
    true);

if (hasHit && hit.Actor is not null)
{
    // Use hit.Actor
}
```

Trace bugs are usually channel/collision config bugs. Prefer the project's existing channel conventions.

## Navigation And AI Movement

```csharp
if (Controller is AAIController aiController)
{
    aiController.MoveToLocation(destination, acceptanceRadius, true, true, true, true, default, true);
}
```

Before custom stuck logic, search for navigation helpers:

```csharp
var onNavMesh = UNavigationSystemV1.ProjectPointToNavigation(
    ActorLocation,
    out var projected,
    null,
    default,
    new FVector(60.0f, 60.0f, 200.0f));
```

Use one movement owner/pipeline where possible. Multiple systems repeatedly issuing move commands cause stop/start jitter and hard-to-debug interruptions.

## Physics, Collision, Visibility

Search exact method names in local/generated code, then use built-ins such as:

```csharp
ActorHiddenInGame = true;
SetActorEnableCollision(false);
PrimitiveComponent.SetSimulatePhysics(true);
PrimitiveComponent.WakeAllRigidBodies();
SceneComponent.SetVisibility(false, true);
```

Prefer component/actor APIs over changing unrelated transform or tick state to fake visibility/collision.

## Save Provider Shape

Use the local save system shape if one exists. A generic split that usually works:

```csharp
public interface ISaveProvider
{
    string SaveKey { get; }
    int LoadPriority { get; }
    object CaptureSaveData();
    void ApplySaveData(JsonElement data);
}
```

Common boundary:

- Save component: generic transform, visibility, enabled/hidden state.
- Provider: gameplay booleans, counters, phases, prompts, high-level reconstruction data.
- Do not serialize live delegates, callbacks, lambdas, async tasks, or raw task/choice execution objects.

## Interface Or Capability Discovery

```csharp
private static IMyCapability? FindCapability(AActor actor)
{
    IMyCapability? result = null;

    actor.ForEachComponent(component =>
    {
        if (result is null && component is IMyCapability capability)
        {
            result = capability;
        }
    });

    return result;
}
```

Use this for interaction/perception/capability scanning when the project already treats components as reusable capabilities.

## Blueprint And Packaging Diagnostics

- Type missing in Unreal: check `[UClass]`, `partial`, namespace, project inclusion, generated Glue, editor restart, and stale binaries.
- Property missing: check `[UProperty]`, supported type, getter/setter shape, build output, and Blueprint refresh.
- `BindWidget` missing: check exact widget name and type in the Blueprint.
- Input duplicate/toggle bug: check UI key handlers, controller handlers, trigger phase, input mode, focus, and mapping context priority.
- Editor works but packaged fails: check cooked asset references, config defaults, viewport scale, initialization timing, and Blueprint overrides.
- C# source compiles but runtime uses old behavior: check hot reload cache and generated artifacts before redesigning.

## Pre-Edit Sanity Questions

- Does this need Unreal reflection, or is plain C# enough?
- Is this an object reference, asset reference, or class reference?
- Is there already a local example of the same type of actor/component/widget/input?
- Is there already an engine/UnrealSharp API for this operation?
- Will this run once, on overlap/event, on interval, or every tick?
- If async, where is cancellation/epoch and where does it return to Unreal context?
- If using global events, where is unsubscribe?
- If saving, what is stable state vs transient live behavior?
