# Unreal Engine Python Cheatsheet

## Common Snippets

```python
import unreal

# Get selected assets in Content Browser
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

# Get selected actors in current level
selected_actors = unreal.EditorUtilityLibrary.get_selected_level_actors()

# Load an asset
asset = unreal.EditorAssetLibrary.load_asset("/Game/MyAsset")

# Get a class default object
lib = unreal.EditorUtilityLibrary.get_default_object()

# Iterate static mesh actors in current level
actors = unreal.EditorLevelLibrary.get_all_level_actors()
for actor in actors:
    if isinstance(actor, unreal.StaticMeshActor):
        smc = actor.static_mesh_component
        print(smc.static_mesh)

# Create a cube static mesh actor in the current level
actor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor, unreal.Vector(0, 0, 0))
```

## Decision Rules

1. **Need to query or modify the Content Browser?** Use `unreal.EditorAssetLibrary` or `unreal.EditorUtilityLibrary`.
2. **Need to work with level actors?** Use `unreal.EditorLevelLibrary` or `unreal.EditorActorSubsystem`.
3. **Need mesh editing or procedural geometry?** Use `unreal.StaticMeshEditorSubsystem`, `unreal.MeshEditingLibrary`, or `unreal.GeometryScriptLibrary`.
4. **Need to import/export assets?** Use `unreal.DatasmithScene`, `unreal.GLTFExporter`, or `unreal.USDStage`.
5. **Need a runtime/gameplay helper?** Use `unreal.GameplayStatics` or `unreal.KismetSystemLibrary`.
6. **Need to build an editor UI?** Use `unreal.EditorUtilityWidget` or `unreal.WidgetBlueprint`.
