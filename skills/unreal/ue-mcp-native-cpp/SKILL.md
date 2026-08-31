---
name: ue-mcp-native-cpp
description: Use when writing or modifying native C++ that integrates with the ue-mcp C++ Bridge plugin. Covers module setup, header / source conventions, dependency injection of bridge services, posting back to the editor over JSON, and the conventions for adding a new bridge-callable handler. Auto-loads when the user wants to extend ue-mcp surface area or fix bridge-side compilation.
---

# ue-mcp native-cpp author guide

When `ue-mcp` doesn't yet cover a UE subsystem you need to drive, you extend it **on the C++ side**: add a new handler module that lives inside the editor process and posts results back through the bridge. This skill captures the conventions.

## Where the bridge lives

```text
YourProject/
  Plugins/ue-mcp/
    Source/ue-mcpEditor/           # editor-only C++ module
      Public/Handlers/             # your new handlers live here
      Private/Handlers/
      ue-mcpEditorModule.cpp       # module startup + handler registration
```

Add the plugin folder as a project plugin, enable in `.uproject`:

```json
"Plugins": [{ "Name": "ue-mcp", "Enabled": true }]
```

## The minimal new handler

Bridge handlers implement a single interface (`IUE-mcpHandler`) and register themselves in module startup. The pattern:

```cpp
// Public/Handlers/MyHandler.h
#pragma once
#include "CoreMinimal.h"
#include "IUE-mcpHandler.h"

class FMyHandler : public IUE-mcpHandler
{
public:
    virtual FString GetName() const override { return TEXT("my_subsystem"); }
    virtual FString GetDescription() const override { return TEXT("Read/write X subsystem objects"); }
    virtual TSharedPtr<FJsonObject> GetInputSchema() const override;
    virtual FUE-mcpResult Execute(const TSharedPtr<FJsonObject>& Params) override;
};
```

```cpp
// Private/Handlers/MyHandler.cpp
#include "Handlers/MyHandler.h"
#include "Modules/ModuleManager.h"

void FMyHandler::Register()
{
    // called from module startup; concrete implementation lives in the bridge
    // subsystem — typically a static RegisterHandler lambda at module startup.
}

FUE-mcpResult FMyHandler::Execute(const TSharedPtr<FJsonObject>& Params)
{
    FString AssetPath = Params->GetStringField(TEXT("asset_path"));
    // perform UE operation using EditorSubsystem APIs
    // return success / error with structured payload
}
```

## Post-back contract

When the editor finishes work for a request, the bridge posts back over the local WebSocket / JSON-RPC channel. Always:

- Return a structured payload (success / failure + data) — never a string-only message
- Surface `EditorIsInitializing` as a retryable error code so the caller can back off
- Wrap mutations in `FScopedTransaction` so the user can undo them in the editor
- Save only the dirty packages you actually touched — `UEditorAssetLibrary::SaveLoadedAsset` per asset, not `SaveAll`

## Build pipeline

The bridge is **editor-only**. It must never be linked into a packaged build. Two ways to enforce this:

1. Put all handler code under `Source/<Plugin>Editor/` and let `Build.cs` only build that module in editor targets
2. In each handler `.cpp`, wrap with `#if WITH_EDITOR ... #endif`

On Windows: `Build.bat YourProjectEditor Win64 Development -Project="..."`
On macOS: the same via Xcode or `RunUAT.sh BuildEditor`

## Conventions ue-mcp enforces

- **One handler per UE subsystem** — keep the surface orthogonal
- **Action-dispatch style** — `Execute(params)` parses a JSON `action` field and routes internally
- **Structured errors** — return JSON with `error_code` (string), `error_message` (string), `retryable` (bool)
- **Idempotency hints** — declare which actions are safe to retry
- **Time / cost budgets** — declare synchronous vs asynchronous; surface a `progress` channel for long ops

## Add a tool without touching the wrapper

A new handler only touches C++. The npm wrapper auto-discovers tools via `GET /api/tools` and converts JSON Schema to zod, so no wrapper rebuild is needed when you add a handler. Just restart the editor (or wait for hot reload if your project supports it) and run `ModelContextProtocol.RefreshTools` from the host.

## Cross-reference

- For blueprint-side authoring through the bridge: see `ue-mcp-blueprint` skill
- For the editor lifecycle: see `ue-mcp-workflow` skill
- For Epic Toolset alternative when UE 5.8+: see `ue-mcp-epic-routing` skill
- For general UE 5.8 C++ knowledge (UPROPERTY, UCLASS, modules): see `kevinpbuckley-unreal-engine-skills` and `ue-cpp-foundations`
