# VERIFY 2026-08-24

- ref: `origin/CursorSkillSearch` @ `aa2d7074e7ad`
- 技能数: **322**（SKILL/SOURCE 成对）
- 阻断: **8**  警告: **179**
- 方向分布: 2d=28, 3d=30, game-design=119, ui-design=25, unreal=95, workflow=25
- DIGEST 建议引入: schepetkov-ue-ui, schepetkov-ue-assets, fagemx-game-direction, rundesk-designing-game-levels, rundesk-playtesting-games

## 一屏结论

未通过：8 条结构阻断。

## 阻断项

- `skills/2d/omer-concept-art`: yaml-unquoted-colon：description 含未加引号的冒号，标准 YAML 失败；Cursor 加载该 skill 也可能失败
- `skills/2d/omer-weapon-design`: yaml-unquoted-colon：description 含未加引号的冒号，标准 YAML 失败；Cursor 加载该 skill 也可能失败
- `skills/game-design/omer-ai-world-building`: yaml-unquoted-colon：description 含未加引号的冒号，标准 YAML 失败；Cursor 加载该 skill 也可能失败
- `skills/game-design/omer-narrative-design`: yaml-unquoted-colon：description 含未加引号的冒号，标准 YAML 失败；Cursor 加载该 skill 也可能失败
- `skills/game-design/omer-procedural-generation`: yaml-unquoted-colon：description 含未加引号的冒号，标准 YAML 失败；Cursor 加载该 skill 也可能失败
- `skills/ui-design/nextlevelbuilder-ui-ux-pro-max`: yaml-unquoted-colon：description 含未加引号的冒号，标准 YAML 失败；Cursor 加载该 skill 也可能失败
- `skills/unreal/unreal-design-patterns`: yaml-unquoted-colon：description 含未加引号的冒号，标准 YAML 失败；Cursor 加载该 skill 也可能失败
- `skills/unreal/unreal-replication`: yaml-unquoted-colon：description 含未加引号的冒号，标准 YAML 失败；Cursor 加载该 skill 也可能失败

## 警告

- `skills/2d/gamedev-create-game-assets`: name=create-game-assets 与目录 gamedev-create-game-assets 不一致
- `skills/2d/heycat-animated-sprite-generation`: name=animated-sprite-generation 与目录 heycat-animated-sprite-generation 不一致
- `skills/2d/heycat-asset-pipeline-automation`: name=asset-pipeline-automation 与目录 heycat-asset-pipeline-automation 不一致
- `skills/2d/heycat-autotiling-transitions`: name=autotiling-transitions 与目录 heycat-autotiling-transitions 不一致
- `skills/2d/heycat-camera-pan-zoom-controls`: name=camera-pan-zoom-controls 与目录 heycat-camera-pan-zoom-controls 不一致
- `skills/2d/heycat-canvas-performance-optimization`: name=canvas-performance-optimization 与目录 heycat-canvas-performance-optimization 不一致
- `skills/2d/heycat-canvas2d-isometric-renderer`: name=canvas2d-isometric-renderer 与目录 heycat-canvas2d-isometric-renderer 不一致
- `skills/2d/heycat-comfyui-lowvram-setup`: name=comfyui-lowvram-setup 与目录 heycat-comfyui-lowvram-setup 不一致
- `skills/2d/heycat-depth-sorting-occlusion`: name=depth-sorting-occlusion 与目录 heycat-depth-sorting-occlusion 不一致
- `skills/2d/heycat-godot4-isometric-tilemap`: name=godot4-isometric-tilemap 与目录 heycat-godot4-isometric-tilemap 不一致
- `skills/2d/heycat-isometric-art-direction`: name=isometric-art-direction 与目录 heycat-isometric-art-direction 不一致
- `skills/2d/heycat-isometric-building-sprites`: name=isometric-building-sprites 与目录 heycat-isometric-building-sprites 不一致
- `skills/2d/heycat-isometric-character-sprites`: name=isometric-character-sprites 与目录 heycat-isometric-character-sprites 不一致
- `skills/2d/heycat-isometric-grid-math`: name=isometric-grid-math 与目录 heycat-isometric-grid-math 不一致
- `skills/2d/heycat-isometric-object-sprites`: name=isometric-object-sprites 与目录 heycat-isometric-object-sprites 不一致
- `skills/2d/heycat-isometric-pathfinding`: name=isometric-pathfinding 与目录 heycat-isometric-pathfinding 不一致
- `skills/2d/heycat-seamless-isometric-terrain`: name=seamless-isometric-terrain 与目录 heycat-seamless-isometric-terrain 不一致
- `skills/2d/heycat-spritesheet-atlas-packing`: name=spritesheet-atlas-packing 与目录 heycat-spritesheet-atlas-packing 不一致
- `skills/2d/heycat-tile-picking-interaction`: name=tile-picking-interaction 与目录 heycat-tile-picking-interaction 不一致
- `skills/2d/heycat-tilemap-data-format`: name=tilemap-data-format 与目录 heycat-tilemap-data-format 不一致
- `skills/2d/heycat-transparent-cutout-cleanup`: name=transparent-cutout-cleanup 与目录 heycat-transparent-cutout-cleanup 不一致
- `skills/2d/omer-ai-game-art-generation`: name=ai-game-art-generation 与目录 omer-ai-game-art-generation 不一致
- `skills/2d/omer-art-consistency`: name=art-consistency 与目录 omer-art-consistency 不一致
- `skills/2d/omer-character-design`: name=character-design 与目录 omer-character-design 不一致
- `skills/2d/omer-creature-design`: name=creature-design 与目录 omer-creature-design 不一致
- `skills/2d/omer-pixel-art-sprites`: name=pixel-art-sprites 与目录 omer-pixel-art-sprites 不一致
- `skills/3d/blender-unreal-export`: name=unreal-export 与目录 blender-unreal-export 不一致
- `skills/3d/omer-3d-modeling`: name=3d-modeling 与目录 omer-3d-modeling 不一致
- `skills/3d/omer-environment-art`: name=environment-art 与目录 omer-environment-art 不一致
- `skills/3d/omer-lighting-design`: name=lighting-design 与目录 omer-lighting-design 不一致
- `skills/3d/omer-rigging-animation`: name=rigging-animation 与目录 omer-rigging-animation 不一致
- `skills/3d/omer-shader-programming`: name=shader-programming 与目录 omer-shader-programming 不一致
- `skills/3d/omer-texture-art`: name=texture-art 与目录 omer-texture-art 不一致
- `skills/3d/omer-vehicle-design`: name=vehicle-design 与目录 omer-vehicle-design 不一致
- `skills/3d/omer-vfx-realtime`: name=vfx-realtime 与目录 omer-vfx-realtime 不一致
- `skills/3d/omer-voxel-art`: name=voxel-art 与目录 omer-voxel-art 不一致
- `skills/game-design/donchitos-art-bible`: name=art-bible 与目录 donchitos-art-bible 不一致
- `skills/game-design/fagemx-balance-review`: name=balance-review 与目录 fagemx-balance-review 不一致
- `skills/game-design/fagemx-build-playability-review`: name=build-playability-review 与目录 fagemx-build-playability-review 不一致
- `skills/game-design/fagemx-feel-pass`: name=feel-pass 与目录 fagemx-feel-pass 不一致
- …另有 139 条警告未展开

## 许可分布

- MIT: 150
- Apache-2.0: 80
- 见原仓 LICENSE: 78
- 未声明/待核: 14
未声明/待核 14 条已写入 `records/verify/ESCALATION.md`，升格前先核原仓 LICENSE。

## 许可原仓探测

- `fenggezaici/dcc-python-skills`：原仓无 GitHub 可识别 LICENSE（404）
- `w-zhian/game-design-skills`：原仓无 GitHub 可识别 LICENSE（404）
- `ityes22/game-design-document`：文件是 Apache-2.0，GitHub SPDX=NOASSERTION
- `makesupply/lodestar-skill`：文件是 MIT，GitHub SPDX=NOASSERTION
- `kevinpbuckley/unreal-engine-skills`：原仓无 GitHub 可识别 LICENSE（404）
- `dstn2000/claude-unreal-engine-skill`：原仓无 GitHub 可识别 LICENSE（404）

## DIGEST 引入是否在库里

建议引入项都能在 `skills/` 下找到同名目录。

## 相对上次差量

新增阻断 0：无；消失 0：无。

## 来源抽检（HTTP HEAD，独立仓库）

独立来源 61，可访问 61，失效 0。
- `heycat-animated-sprite-generation` https://github.com/0xheycat/isometric-game-skills → **200**
- `hlsl-shader` https://github.com/18163623522/ue-shader-skills → **200**
- `design-game-ui` https://github.com/888wing/game-ui-skill → **200**
- `epic-unreal-mcp` https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin → **200**
- `unrealsharp-operations` https://github.com/Extreme11111/unrealsharp-syntax-skill → **200**
- `ue-build` https://github.com/GuangminJu/UnrealSkills → **200**
- `blender-cinematic-scene` https://github.com/HabrielStark/brilliant-blender-skill → **200**
- `roguelike-game-designer` https://github.com/Hanjo92/roguelike-game-designer-skill → **200**
- `unreal-client-protocol` https://github.com/Italink/UnrealClientProtocol → **200**
- `ue-af-blueprint-authoring` https://github.com/JanVogelsang/UE-AgentFramework → **200**
- `jetbrains-ue-code-authoring` https://github.com/JetBrains/rider-skills → **200**
- `leonxlnx-taste-skill` https://github.com/Leonxlnx/taste-skill → **200**
- …其余 49 条均为 2xx/3xx

## 重复 name

- `shader-programming`: `skills/3d/omer-shader-programming`, `skills/game-design/gamedev-shader-programming`
- `combat-design`: `skills/game-design/combat-design`, `skills/game-design/omer-combat-design`, `skills/game-design/wzhian-combat-design`
- `level-design`: `skills/game-design/gamedev-level-design`, `skills/game-design/level-design`, `skills/game-design/omer-level-design`
- `narrative-design`: `skills/game-design/narrative-design`, `skills/game-design/omer-narrative-design`
- `game-ui-design`: `skills/ui-design/game-ui-design-principles`, `skills/ui-design/omer-game-ui-design`
- `unreal-blueprints`: `skills/unreal/dcc-unreal-blueprints`, `skills/unreal/unreal-blueprints`
- `unreal-niagara`: `skills/unreal/dcc-unreal-niagara`, `skills/unreal/unreal-niagara`
- `unreal-engine`: `skills/unreal/omer-unreal-engine`, `skills/unreal/ue-project-discovery`

## 升级给昴

这 8 条 skill 的 description 没加引号又含冒号，YAML 非法。修复：把 description 改成 `|` 或多行引号。
不在验证环里直接改侦察分支，避免和 SkillSearch 抢写。
- `skills/2d/omer-concept-art`
- `skills/2d/omer-weapon-design`
- `skills/game-design/omer-ai-world-building`
- `skills/game-design/omer-narrative-design`
- `skills/game-design/omer-procedural-generation`
- `skills/ui-design/nextlevelbuilder-ui-ux-pro-max`
- `skills/unreal/unreal-design-patterns`
- `skills/unreal/unreal-replication`

## 未覆盖

- 不执行 skill 内脚本，不做运行时功能测试。
- 不把 CursorSkillSearch 合进 main。
- 来源 URL 对独立 github 仓库做 HEAD；同一仓下多条 skill 不重复打。

