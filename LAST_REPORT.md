# LAST_REPORT — 增量基线

- date: 2026-08-14T09:55+08:00
- branch: CursorSkillSearch
- introduced_this_round:
  - nvidia-omniverse-cad-to-simready                # NVIDIA 官方，Apache-2.0+CC-BY-4.0，v0.2.0，CAD→SimReady USD 端到端编排，与 UE 5.2+ Datasmith USD / Interchange USD 直接对接
  - nvidia-omniverse-usd-performance-tuning         # NVIDIA 官方，Apache-2.0+CC-BY-4.0，v0.1.0，USD 性能诊断与优化编排，与上一条互为「产出 / 优化」两半
  - thrixel-goal-to-game                            # MIT（源头），5 commits，08-12 重构为 Claude Code plugin；Thrixel 三路径决策 + 强制 group_parts + Cube 预算驱动资产列表
- known_good_prior: dcc-mcp, dcc-mcp-blender, qwen-mm-plugins-blender, quodsoler-unreal-engine-skills, kevinpbuckley UE5.8 (61 SKILL), loomle SAL MCP, db-lyon ue-mcp ×3, nextlevelbuilder ui-ux-pro-max, fagemx stack, gamedev-skills UE 主链, mengto game skills, heycat isometric, arg-games cqtest, jetbrains ue-test, UnrealMotionGraphicsMCP, leonxlnx-taste-skill, haxqer-godot-skill
- carry_watch: abagames (08-09 增量小游戏/Godot), educlopez/ui-craft, MengTo threejs, Yuki (no license), SummerEngine, Randroids, NAJEM, mike007jd, alfaris, Shellishack, OpenGame, affaan-m blender-motion-state-inspection, dcc-mcp-skills-creator, addyyosmani/agent-skills (76k★ / 08-11 hooks, 含 frontend-ui-engineering 但与 nextlevelbuilder/taste-skill 重叠定位 — 不直接入库), MCPBlender/blender-mcp (25.6k★, mcp server 非 SKILL), EpicLolia/UnrealPythonMCP (08-09 TypeScript UE Python MCP), virgiliojr94/book-to-skill, Matt Pocock skills, reverse-skill, awesome-gamedev-agent-skills (08-11 docs 后无实质更新; 本仓已基本覆盖), NVIDIA/skills (560+ commit, 08-14 仍活跃; 剩 omniverse-realtime-viewer / cuopt-routing-api-python / physical-ai-neural-reconstruction 等 8+ 条计划在 08-15~08-17 摘取)
- missed_or_pending: awesome-gamedev-agent-skills 剩余 15 Godot / 8 Unity / 6 Web / 5 Other-Engine 技能未单独入库; NVIDIA Skills 剩余 ~8 方向相关技能 (omniverse / cuopt / physical-ai); kevinpbuckley/VibeUE 还剩 ~32 SKILL.md; dcc-mcp-creator / dcc-mcp-skills-creator 维持观望; addyyosmani/agent-skills 重叠定位暂不直接入库; Qwen-MM-Plugins freecad 能力未单独入库
- push_status: 08-13 commit 56db0c8 已 push; 本轮 commit (3 新增 SKILL/SOURCE pair + DIGEST + LAST_REPORT 更新) 待 push (selector fix 已稳定, 沿用 `git -c credential.helper= -c credential.helper=manager push origin CursorSkillSearch`)
- pr_status: PR #31 维持打开, 标题/正文将由本轮 commit 后刷新
