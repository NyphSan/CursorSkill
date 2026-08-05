---
name: niagara-json-generator
description: Author, validate, and headlessly compile Unreal Engine 5.8 Niagara System assets from strict JSON with AutoNiagara's NiagaraSkill plugin. Use when creating particle effects without the graphical Niagara editor, translating an effect design into emitter/module/input/renderer JSON, running the generator commandlet or Unreal Python bridge, or diagnosing its compile report.
---

# Niagara JSON Generator

Use NiagaraSkill as a graph authoring and compile pipeline. Never attempt to synthesize or patch VectorVM bytecode directly; Unreal must translate the generated Niagara graphs and produce CPU bytecode or GPU shaders through its canonical compiler.

## Author a specification

1. Read [references/schema.md](references/schema.md) before writing JSON.
2. Start from [the known-good template example](Examples/fountain-template.json), [the explicit-stack example](Examples/custom-sprite.json), or [the Data Channel reader example](Examples/data-channel-reader.json).
3. Use exact Unreal object paths for templates, modules, and dynamic inputs. Do not invent an asset path. Confirm `.uasset` existence under the engine or project content tree and translate it to its mounted object path.
4. Use exact stack names and input names. Prefer a template emitter when the desired behavior already exists. Use the completely empty emitter only when every required lifecycle, spawn, initialization, update, and renderer item will be supplied.
5. Keep `replace_existing` false until replacement is intentional. It deletes only the exact output asset before regenerating it.

When translating a code-simulated particle runtime, read [the HiveFeature translation](references/hive-feature.md). Preserve the source lifecycle and capacities in the C++ producer, use the JSON as the typed renderer contract, and keep inactive fixed-pool rows explicitly hidden.

## Use Niagara Data Channels

Read [references/data-channels.md](references/data-channels.md) before designing a channel-driven effect.

- Declare `data_channels` when the run should create the channel asset. Payload variable names and types are an API contract with runtime writers; keep them stable.
- Use `data_channel_read` on a particle spawn/update module when no graphical scratch-pad module exists. It generates and saves a normal Niagara module asset, maps named channel fields to particle attributes, and automatically binds its `Data Channel` input.
- Use input `mode: "data_channel"` to bind a channel to an existing Niagara reader or writer module. The generator rejects the operation if the target input is not a Data Channel data interface.
- Pair `read_current_frame: false` with `keep_previous_frame_data: true` for deterministic, one-frame-latency reads. Current-frame reads require the writer to tick before the Niagara reader.
- Provide a runtime Blueprint or C++ producer. JSON generation creates and compiles assets; it does not publish per-frame gameplay data.

## Compile headlessly

Run:

```powershell
& "D:\UnrealProjects\AutoNiagara\Plugins\NiagaraSkill\Scripts\Generate-Niagara.ps1" `
  -Spec "ABSOLUTE_SPEC.json" `
  -Report "ABSOLUTE_REPORT.json"
```

Alternatively, inside Unreal Python call:

```python
import json
import unreal

report_json = unreal.NiagaraGeneratorLibrary.generate_from_json_file(r"ABSOLUTE_SPEC.json")
report = json.loads(report_json)
assert report["success"]
```

Both entry points invoke the same C++ parser, edit operations, compiler wait, diagnostics, and save routine.

## Compile interactively with the Editor Utility Widget

Open **Tools > Niagara JSON Generator...** in the Unreal Editor. Choose the JSON specification, select an output folder under `/Game` with the Content Browser picker, and optionally enter the full output system name. Leaving the name blank derives `NS_<JsonBaseName>` and upper-cases only the base filename's first character (`smoke_burst.json` becomes `NS_Smoke_burst`). Invalid object-name characters in the derived filename are sanitized for Unreal; a custom name must be valid as entered.

The widget overrides only `root.asset.path` and `root.asset.name` in memory. Do not rewrite JSON merely to redirect one interactive generation. The original file, including Data Channel declarations and module output paths, remains unchanged. The report shown by the widget is the same acceptance gate described below.

## Treat the report as the acceptance gate

Accept the result only when all of these are true:

- `success` and `saved` are true.
- Every entry in `generated_assets` is saved, including channel and generated reader-module dependencies.
- `compile.is_compiling`, `compile.is_stale`, and `compile.has_errors` are false.
- `compile.vm_bytecode_verified` is true for all system and CPU-sim particle scripts.
- Every script status is `UpToDate`, `UpToDateWithWarnings`, or `ComputeUpToDateWithWarnings`.
- `stack.error_count` is zero when a `stack` section is present. Headless commandlets omit this UI-backed scan and emit a warning; compile-state checks remain mandatory.

If validation fails, fix the reported JSON location. If an edit fails, verify the asset, stack, module, and input names. For compile failures, inspect each script's events; change the graph specification rather than manipulating generated bytecode.
