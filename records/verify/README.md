# 技能验证报告

由 `scripts/verify-collected-skills.py` 写入。

- `LATEST.md`：最近一次
- `VERIFY-YYYY-MM-DD.md`：按日归档
- `RUNLOG.md`：每次抽检一行（时刻、ref、阻断数）
- `ESCALATION.md`：当前要升级给昴的阻断（YAML 非法等）

供应商前缀目录（如 `heycat-…` / `omer-…`，frontmatter `name` 等于目录后缀）不计入警告。
