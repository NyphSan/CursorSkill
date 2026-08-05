# 技能侦察 DIGEST — 2026-08-05（08:00Z）

- 侦察时间：2026-08-05T08:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T07:00Z（同日上一轮，PR#7）
- 本仓入库：精选 **93** 个 `SKILL.md`（较上轮 +5；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-08`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓（kevinpbuckley / dcc-python / VibeUE / db-lyon 等）无新实质提交。**实质增量来自 code search 补漏 + 今日新建**：① [Italink/UnrealClientProtocol](https://github.com/Italink/UnrealClientProtocol)（120★ MIT，24 个 UE 编辑器桥 skill，精选传输层）；② [maystudios/claude-skills](https://github.com/maystudios/claude-skills) 的 UE 最佳实践与 PCG Python；③ [ityes22/game-design-document](https://github.com/ityes22/game-design-document) GDD 生成器（skills.sh ~830）；④ **今日 06:31Z 新建** [Extreme11111/unrealsharp-syntax-skill](https://github.com/Extreme11111/unrealsharp-syntax-skill)（UnrealSharp/C#）。`path:.cursor/skills` code search 本轮后期 **429**；今日 `skill` 新建噪声 ≥100。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| unreal-client-protocol | UE·工作流 | 经 TCP+JSON 调用运行中 UE 编辑器任意 UFunction（UCP 传输层） | https://github.com/Italink/UnrealClientProtocol | 120★ MIT；24 个配套领域 skill；含 `UCP.py`；与 db-lyon/ue-mcp 路径互补 | **引入** |
| unreal-best-practices | UE | UE 5.x 现代系统选型（GAS/EIS/StateTree/PCG/CommonUI…）与 research-first | https://github.com/maystudios/claude-skills | MIT；UE 5.7 状态表清晰；含 references/；适合开新功能前选型 | **引入** |
| unreal-pcg-python | UE·3D | PCG Python 互通（PCGPythonInterop / Execute Python Script） | https://github.com/maystudios/claude-skills | 稀缺的 PCG+Python 指南；与已入库 dcc UE Python 互补 | **引入** |
| game-design-document | 游戏设计 | 从概念生成 publisher-grade GDD / pitch（docx/pdf/pptx） | https://github.com/ityes22/game-design-document | skills.sh ~830 installs；可执行脚本+模板；策划向强 | **引入** |
| unrealsharp-operations | UE | UnrealSharp / UE C# 编译热重载、Glue、UMG/EIS 绑定与排错 | https://github.com/Extreme11111/unrealsharp-syntax-skill | **今日新建** MIT；references 完整；补齐 C# 工作流空白 | **引入** |

本仓已摘录：

- `skills/unreal/unreal-client-protocol/`（+ `scripts/UCP.py`）
- `skills/unreal/unreal-best-practices/`（+ references）
- `skills/unreal/unreal-pcg-python/`
- `skills/game-design/game-design-document/`（+ scripts/templates/example）
- `skills/unreal/unrealsharp-operations/`（+ references）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| fenggezaici/dcc-python-skills | 仍停 06:53Z；无后续 commit；★2；无 SPDX | https://github.com/fenggezaici/dcc-python-skills | 继续引入（已入库三件套） |
| kevinpbuckley/unreal-engine-skills | 仍为 08-04 UE 5.8 retarget | https://github.com/kevinpbuckley/unreal-engine-skills | 继续引入 |
| kevinpbuckley/VibeUE | 仍 08-04 | https://github.com/kevinpbuckley/VibeUE | 继续引入 |
| db-lyon/ue-mcp | 仍 08-04 晚 bump | https://github.com/db-lyon/ue-mcp | 继续引入 |
| 4lian/skills_collector | 06:58Z 仅 frontend-dev + README | https://github.com/4lian/skills_collector | 仍观望 |
| ch1109/portable-agent-skills | 仍 06:01Z；★10 | https://github.com/ch1109/portable-agent-skills | 仍观望（方向弱） |
| EpicGames / hkuds / freshtechbro | 仅星标微调 | 各原仓 | 维持上轮档位 |

### 累计建议引入（仍有效）

1–33. 维持上轮清单（含 gamedev-skills、kevinpbuckley、Epic、dcc-python、omer-metin game-ui、freshtechbro blender-web 等）  
34. **+ 本轮** https://github.com/Italink/UnrealClientProtocol（精选 `unreal-client-protocol`）  
35. **+ 本轮** https://github.com/maystudios/claude-skills（精选 `unreal-best-practices` + `unreal-pcg-python`）  
36. **+ 本轮** https://github.com/ityes22/game-design-document  
37. **+ 本轮** https://github.com/Extreme11111/unrealsharp-syntax-skill  

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| Italink 其余 23 领域 skill | UE | modeling/niagara/widget/PIE 等 UCP 领域包 | https://github.com/Italink/UnrealClientProtocol | 入口已引入；按需再精选 modeling/niagara | 观望 |
| maystudios unreal-gas / blueprint-codegen / thirdparty | UE | GAS C++ 深指南、BP 代码生成、第三方库链接 | https://github.com/maystudios/claude-skills | 与已有 `ue-gameplay-ability-system` 重叠；GAS 可下轮对比 | 观望 |
| fairypark/unreal-editor-skills-for-codex | UE·工作流 | Codex + Unreal MCP 编辑器控制 | https://github.com/fairypark/unreal-editor-skills-for-codex | 1★ MIT；5 SKILL；与 db-lyon/NAJEMWEHBE 同类 | 观望 |
| oliver-io/unreal-harness | UE·工作流 | ~300 Editor Actions + 22 skills 全家桶 | https://github.com/oliver-io/unreal-harness | 5★；体量大、许可 NOASSERTION；先抽样 | 观望 |
| frabcd/codex-ai-game-studio | 游戏设计·3D·工作流 | 95 skills：Unity/Godot/Unreal/Blender 工作室 | https://github.com/frabcd/codex-ai-game-studio | 2★ MIT；今日有推送；偏多引擎脚手架 | 观望 |
| NAJEMWEHBE/unreal-ai-connection（driving-unreal） | UE·工作流 | MCP 驱动 UE 5.7 关卡/材质/Sequencer | https://github.com/NAJEMWEHBE/unreal-ai-connection | 9★ MIT；强依赖自有 MCP | 观望 |
| Randroids-Dojo/skills（unreal） | UE·工作流 | PlayUnreal Remote Control 自动化（WIP） | https://github.com/Randroids-Dojo/skills | 43★ MIT；标注 WIP | 观望 |
| TerminalSkills/skills（unreal/blender/houdini/3dsmax） | UE·3D | 巨型 skill 库中的 DCC/UE 条目 | https://github.com/TerminalSkills/skills | 121★ Apache-2.0；需精选防镜像 | 观望 |
| pluginagentmarketplace/…/game-design-theory | 游戏设计 | MDA/Bartle/Flow 理论（~1837 installs） | https://github.com/pluginagentmarketplace/custom-plugin-game-developer | 与已有策划 skills 重叠；marketplace bond 格式 | 观望 |
| omer-metin unreal-engine / game-design-core | UE·游戏设计 | 人设型 UE/策划 skill + patterns | https://github.com/omer-metin/skills-for-antigravity | 已引入 game-ui；其余按需 | 观望 |
| opusgamelabs/game-creator | 2D·3D·游戏设计 | Phaser/ThreeJS 游戏制作插件 skills | https://github.com/opusgamelabs/game-creator | 305★ 无 SPDX；Web 游戏向 | 观望 |
| SFKislev/Flue（blender/houdini） | 3D·工作流 | 无 MCP 的桌面 CLI 桥（installs 很高） | https://github.com/SFKislev/Flue | 需本机 Flue；上轮已观望 | 观望 |
| hkuds/cli-anything（blender/unrealinsights/…） | 3D·UE·工作流 | CLI 桥接桌面软件 harness | https://github.com/hkuds/cli-anything | 46639★；单体巨大 | 观望 |
| xingtongovo/ui-ux-skill-suite | UI | 今日新建 GSAP/impeccable UX 套件 | https://github.com/xingtongovo/ui-ux-skill-suite | 0★ 无 license；偏 Web 动效非游戏 HUD | 观望 |
| cowork-os unreal-development | UE | 薄路由型 UE skill | https://github.com/cowork-os/cowork-os | 实质内容在 JSON runtime；弱于专用仓 | 观望 |

其余观望（w-zhian 剩余 3、omer-metin 3d-modeling、freshtechbro 其余、davincidreams、ceorkm、zhangxiao6776、4lian、ch1109、affaan blender-motion、mechfaber、babysitter UE 切片等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 仍仅 08-03 star chore；mouadja02 近提交仍为 Qdrant / Terraform / K8s（无关）  
- `created:>=2026-08-05` 今日新建噪声 **≥100**（Copilot 练习题、简历、SEO、App Store 运营、金融风控 skill 等）  
- alvinunreal/oh-my-opencode-slim：skills.sh「cartography」实为通用 agent 套件，非 UE  
- modbender/skill-library-mcp、majiayu000/claude-skill-registry-data：巨型镜像/注册表，不入库  

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 08-04：Qdrant / Terraform（无关）；无游戏/UE/设计向 |

## 本仓入库变化（+5 → 93）

- 新增 `skills/unreal/unreal-client-protocol/`  
- 新增 `skills/unreal/unreal-best-practices/`  
- 新增 `skills/unreal/unreal-pcg-python/`  
- 新增 `skills/unreal/unrealsharp-operations/`  
- 新增 `skills/game-design/game-design-document/`  
- 各含 `SOURCE.md`；承接上轮 88 条精选内容  

## 今天可行动

1. **UCP 试跑**：在已开 UCP 插件的 UE 编辑器里装 `unreal-client-protocol`，用 `UCP.py` 跑一次 `FindObjectInstances` / 简单 `ExecutePythonScript`；若常用建模，下轮再引入 `unreal-modeling*`。  
2. **选型+落地**：新功能先问 `unreal-best-practices`「该用 StateTree 还是 BT / CommonUI 还是裸 UMG」，再用已有 kevinpbuckley / Epic skills 写实现。  
3. **个人 skill 候选**：若你走 UnrealSharp，把 `unrealsharp-operations` 的 hot-reload/modal-gate 规则裁进个人 `/ue-csharp`；或把 `game-design-document` 的 discovery 访谈阶段改成「手游/UE 项目」专用 checklist。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02）  
2. 跟踪仓 `pushed_at`（dcc-python、kevinpbuckley、VibeUE、db-lyon、w-zhian、hkuds、flue、omer-metin、freshtechbro、UE-AgentFramework、NiagaraSkill、4lian、ch1109 等）  
3. `gh search repos`：`skill created:>=2026-08-05`；`unreal skill in:name,description`；关键词 unreal/gamedev/blender created≥08-04  
4. `gh search code`：`Unreal filename:SKILL.md`（成功发现 Italink/maystudios/…）；`path:.cursor/skills` / `.agents/skills` → **HTTP 429**  
5. skills.sh/api/search：unreal、gamedev、blender、game ui、game design、houdini、niagara、3d modeling、flue、sequencer  
6. 候选 raw `SKILL.md` + git trees 抽样；CursorSkill 入库 / push / PR  
