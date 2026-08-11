# SOURCE — quodsoler-unreal-engine-skills

- **原仓**: https://github.com/quodsoler/unreal-engine-skills
- **SKILL.md 路径**: `skills/<skill-name>/SKILL.md`（27 个子目录）
- **许可证**: MIT
- **初始发布**: 2026-03-02 (1 commit, `231c857`)
- **作者**: quodsoler + claude

## 收录说明

本 SKILL.md 为索引摘录，列出了 27 个技能的分类和关键特性。每个技能的完整 SKILL.md 和 references/ 未复制，使用时请到原仓查看。

## 为什么收录

1. **源码审计** — 每条 API 对照 UE5 引擎头文件验证，修正 160+ 处不准确
2. **与 kevinpbuckley/unreal-engine-skills 互补** — kevinpbuckley 有 61 SKILL 覆盖面广，quodsoler 有 27 SKILL 但每条经过源码审计
3. **MIT** — 宽松许可
4. **跨引用机制** — ue-project-context 作为基础技能被所有其他技能首先读取，减少上下文冲突
5. **Agent Skills 标准兼容** — 支持 Claude Code / Cursor / Windsurf 等

## 与本仓已有技能的关系

| 维度 | kevinpbuckley (已收) | quodsoler (本轮新收) |
|------|---------------------|---------------------|
| 技能数 | 61 | 27 |
| 重点 | 覆盖面广（C++/BP/动画/关卡/VFX/UMG/工具） | C++ 专精，源码审计 |
| UE 版本 | 5.8 重定向 | 5.x (源码级验证) |
| 审计 | 未明示 | 160+ 处修正 |
| LICENSE | 未明示 | MIT |
