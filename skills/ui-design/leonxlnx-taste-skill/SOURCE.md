# SOURCE — leonxlnx-taste-skill

- **原仓**: https://github.com/Leonxlnx/taste-skill
- **披露页**: https://www.aura.build/skills/b7692462-271d-4882-995a-baa59a66abc5/research
- **安装 CLI**: `npx skills add`
- **作者站点**: Leonxlnx / @lexnlin / @blueemi99
- **LICENSE**: MIT (Copyright (c) 2026 Leonxlnx)
- **Stars / Forks**: ~73.9k★ / ~5.06k forks (今日 +720 stars)，截至 2026-08-13
- **最近 commit（v2 重写）**: 2026-08-07（`design-taste-frontend` v2 experimental 发布）
- **结构**: 13 个 SKILL.md（10 个代码实现类 + 3 个 image-gen 类），每个是一个独立文件夹

## 收录说明

本 SKILL.md 为摘录 + 索引 + 用法，列出了 13 个子技能的 install name / folder name / 用途。原仓 13 个 SKILL.md 的实际 frontmatter 与内容未复制，使用时通过 `npx skills add` 拉取最新。

## 为什么收录

1. **方向命中**：UI 设计（前端 / Web / 移动），对游戏 UI 间接相关（HUD / 风格约束）
2. **质量信号强**：73.9k★ / 5.06k forks / 单日 +720（GitHub 08-12 → 08-13），open-source attention 已经进入"1% 头部"区间
3. **MIT License**：明确无版权风险
4. **与既有的 nextlevelbuilder-ui-ux-pro-max 互补**：该仓为检索驱动（Python + CSV 数据）；本仓为反 slop 规则约束（prompt+骨架代码）
5. **v2 重写（08-07）**：引入三旋钮 VARIANCE / MOTION / DENSITY，是少数可以量化"模型是否真的改变取舍"的观察点

## 互补组合（前端/UI 工作流）

```
look-up style / palette / font     -> nextlevelbuilder-ui-ux-pro-max（本仓已有，08-11）
anti-slop opinionated rules        -> leonxlnx-taste-skill（本仓新入，08-13）
frontend engineering discipline    -> addyyosmani/agent-skills/frontend-ui-engineering（观望）
image-first comps                  -> taste-skill/imagegen-frontend-web / imagegen-frontend-mobile
native taste + general web         -> frontend-design (Anthropic official)
```

## 关联

- `nextlevelbuilder-ui-ux-pro-max` — 与本仓同向优先互补（`skills/ui-design/nextlevelbuilder-ui-ux-pro-max/`）
- `frontend-design` — Anthropic 官方通用 Web UI（不在本仓，仅参考）
- `leonxlnx/taste-skill` 原仓 README 提到的 `stitch-design-taste` 与 Google Stitch 兼容，Stitch 风格统一导出
