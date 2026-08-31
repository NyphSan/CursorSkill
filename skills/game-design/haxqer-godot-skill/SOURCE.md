# SOURCE — haxqer-godot-skill

- **原仓**: https://github.com/haxqer/godot-skill
- **披露**: https://www.v2ex.com/t/1233494
- **路径**: `skill/godot/SKILL.md`（独立子目录，与 README 解耦）
- **作者**: haxqer (https://github.com/haxqer)
- **LICENSE**: MIT（在 2026-08-11 commit `47ad12b` 时添加，本轮收录前已就绪）
- **最后 commit**: 2026-08-11 `b4d0e38` "Merge feat/godot-authoring-ops into main"
- **实质性提交**: 2026-07-14 `feat: Add 3D/theme/navmesh authoring ops and inline-builder codec` (9 个 test suite 全绿)
- **目标版本**: Godot 4.7（兼容 4.x）
- **结构**: SKILL.md + references/ (9 份长文档) + scripts/ (dispatcher + run_tests + scenario_runner + chroma_key + import + package_skill 等)
- **总 commit 数**: 12 commits

## 收录说明

本 SKILL.md 为摘录 + 索引 + 用法 + 与本仓既有技能的关联说明。原仓 `skill/godot/references/` 下 9 份长文档未复制，使用时通过 `git clone` 或 `dist/godot.zip` 拉取最新。

## 为什么收录

1. **方向命中**：游戏设计 + 3D 设计。覆盖 2D（TileSet / TileMapLayer / SpriteFrames / AnimationPlayer）+ 3D（GridMap / navmesh / CSG / glTF）+ 调试 + 测试 + 导出，是 Godot 4.7 当前最完整的 portable Godot 自动化技能
2. **实质性 LICENSE 变更**：08-11 添加 MIT（之前缺失），不再有 LICENSE 风险
3. **实质性功能 commit**：08-11 merge `feat/godot-authoring-ops`（含 paint_gridmap / bake_collision / bake_csg / build_theme / gltf_export / build_replication_config + batch bake_navmesh + project_batch set/clear shader_global），不是简单 star churn
4. **测试信号真实**：9 个 test suite 全部 PASS against Godot 4.7
5. **可定位到 SKILL.md**：清晰位于 `skill/godot/SKILL.md`，不依赖额外约定
6. **与既有的 heycat-* 互补**：heycat 是 isometric pipeline；本仓是 Godot-native 工程 / 内容 / 调试 / 导出

## 关联

- `skills/2d/heycat-*` (本仓既有) — isometric game 渲染 / tilemap / sprite / 镜头控制，与 godot-skill 同向（Godot 项目也用），但分工明确
- `skills/game-design/gamedev-create-game-assets` — Godot / Unity / UE 通用 asset creation（方向一致）
- `skills/workflow/dcc-mcp` — 跨 DCC 工具控制层，不限于 Godot，但 Godot Engine 可借 AssetPostImport → 资产管线协作
- `skills/3d/dcc-mcp-blender` / `skills/3d/qwen-mm-plugins-blender` — 美术生成器；godot-skill 提供落地自动化

## 收录入库过程的风险记录

- 2026-08-11 之前的 commit **没有 LICENSE**；本轮收录时已 08-13，LICENSE 已就位。无版权风险
- 08-11 之前的 commit 信息（如 "refactor dispatcher"）跳跃较大，使用本仓收录的 SKILL.md 时，应基于 v0 + 07-14 + 08-11 三个关键点去取代码，不要从某个不稳定中间 commit checkout
