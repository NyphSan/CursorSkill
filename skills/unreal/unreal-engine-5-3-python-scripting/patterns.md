# Unreal Engine Python Patterns

## Iterate and Modify Static Mesh Assets

```python
import unreal

assets = unreal.EditorUtilityLibrary.get_selected_assets()
for asset in assets:
    if isinstance(asset, unreal.StaticMesh):
        # Access static mesh build settings, sockets, etc.
        print(asset.get_name())
```

## Spawn Actor in Level

```python
import unreal

location = unreal.Vector(0, 0, 100)
rotation = unreal.Rotator(0, 0, 0)
actor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor, location, rotation)
```

## Run an Editor Utility Blueprint

```python
import unreal

# Load a Blutility class and execute its "Run" function
bp = unreal.EditorAssetLibrary.load_blueprint_class("/Game/MyUtility")
obj = unreal.get_default_object(bp)
obj.call_method("Run", tuple())
```

## Geometry Script Example

```python
import unreal

mesh = unreal.StaticMesh()
# Use GeometryScriptLibrary functions to create/edit mesh data
# See ch05-mesh-geometry for available methods.
```
