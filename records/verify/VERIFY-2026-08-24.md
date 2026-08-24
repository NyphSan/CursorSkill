# VERIFY 2026-08-24

- ref: `origin/CursorSkillSearch` @ `aa2d7074e7ad`
- 技能数: **322**（SKILL/SOURCE 成对）
- 阻断: **8**  警告: **178**
- 方向分布: 2d=28, 3d=30, game-design=119, ui-design=25, unreal=95, workflow=25
- DIGEST 建议引入: schepetkov-ue-ui, schepetkov-ue-assets, fagemx-game-direction, rundesk-designing-game-levels, rundesk-playtesting-games

## 一屏结论

未通过：存在结构阻断或失效来源，需人工看阻断项。

## 阻断项

- `skills/2d/omer-concept-art`: frontmatter YAML 无法解析: mapping values are not allowed here
  in "<unicode string>", line 2, column 298:
     ... ethodologies of industry masters: Feng Zhu's efficient design pr ... 
                                         ^; frontmatter 缺 name; description 过短或缺失
- `skills/2d/omer-weapon-design`: frontmatter YAML 无法解析: mapping values are not allowed here
  in "<unicode string>", line 2, column 489:
     ...  and proportion tells the player: what this weapon does, how pow ... 
                                         ^; frontmatter 缺 name; description 过短或缺失
- `skills/game-design/omer-ai-world-building`: frontmatter YAML 无法解析: mapping values are not allowed here
  in "<unicode string>", line 2, column 38:
     ... iption: The ultimate brand asset: a consistent, explorable unive ... 
                                         ^; frontmatter 缺 name; description 过短或缺失
- `skills/game-design/omer-narrative-design`: frontmatter YAML 无法解析: mapping values are not allowed here
  in "<unicode string>", line 2, column 169:
     ... que challenges of game narrative: branching structures that resp ... 
                                         ^; frontmatter 缺 name; description 过短或缺失
- `skills/game-design/omer-procedural-generation`: frontmatter YAML 无法解析: mapping values are not allowed here
  in "<unicode string>", line 2, column 415:
     ... m academic papers.  Core insight: The best PCG systems are heavi ... 
                                         ^; frontmatter 缺 name; description 过短或缺失
- `skills/ui-design/nextlevelbuilder-ui-ux-pro-max`: frontmatter YAML 无法解析: mapping values are not allowed here
  in "<unicode string>", line 2, column 556:
     ...  asks for any visual design task: pages, components, palettes, t ... 
                                         ^; frontmatter 缺 name; description 过短或缺失
- `skills/unreal/unreal-design-patterns`: frontmatter YAML 无法解析: mapping values are not allowed here
  in "<unicode string>", line 2, column 1463:
     ... mplements the unreal-solid skill: patterns are how you realize t ... 
                                         ^; frontmatter 缺 name; description 过短或缺失
- `skills/unreal/unreal-replication`: frontmatter YAML 无法解析: mapping values are not allowed here
  in "<unicode string>", line 2, column 154:
     ... sign lens for networked gameplay: who is authoritative, where ne ... 
                                         ^; frontmatter 缺 name; description 过短或缺失

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
- …另有 138 条警告未展开

## 来源抽检（HTTP HEAD）

- `gamedev-create-game-assets` https://github.com/gamedev-skills/awesome-gamedev-agent-skills → **200**
- `heycat-animated-sprite-generation` https://github.com/0xheycat/isometric-game-skills → **200**
- `heycat-asset-pipeline-automation` https://github.com/0xheycat/isometric-game-skills → **200**
- `heycat-autotiling-transitions` https://github.com/0xheycat/isometric-game-skills → **200**
- `heycat-camera-pan-zoom-controls` https://github.com/0xheycat/isometric-game-skills → **200**
- `heycat-canvas-performance-optimization` https://github.com/0xheycat/isometric-game-skills → **200**
- `heycat-canvas2d-isometric-renderer` https://github.com/0xheycat/isometric-game-skills → **200**
- `fagemx-game-direction` https://github.com/fagemx/gstack-game → **200**
- `rundesk-designing-game-levels` https://github.com/rundesk-ai/rundesk-skills-gamedev → **200**
- `rundesk-playtesting-games` https://github.com/rundesk-ai/rundesk-skills-gamedev → **200**
- `schepetkov-ue-assets` https://github.com/Schepetkov/claude-skills-game-UE → **200**
- `schepetkov-ue-ui` https://github.com/Schepetkov/claude-skills-game-UE → **200**

## 重复 name

- `shader-programming`: `skills/3d/omer-shader-programming`, `skills/game-design/gamedev-shader-programming`
- `combat-design`: `skills/game-design/combat-design`, `skills/game-design/omer-combat-design`, `skills/game-design/wzhian-combat-design`
- `level-design`: `skills/game-design/gamedev-level-design`, `skills/game-design/level-design`, `skills/game-design/omer-level-design`
- `game-ui-design`: `skills/ui-design/game-ui-design-principles`, `skills/ui-design/omer-game-ui-design`
- `unreal-blueprints`: `skills/unreal/dcc-unreal-blueprints`, `skills/unreal/unreal-blueprints`
- `unreal-niagara`: `skills/unreal/dcc-unreal-niagara`, `skills/unreal/unreal-niagara`
- `unreal-engine`: `skills/unreal/omer-unreal-engine`, `skills/unreal/ue-project-discovery`

## 未覆盖

- 不执行 skill 内脚本，不做运行时功能测试。
- 不把 CursorSkillSearch 合进 main。
- 来源 URL 只抽检 DIGEST 引入 + 随机样本。

