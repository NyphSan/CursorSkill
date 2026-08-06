# Gitea 仓库管理员（归属主控）

参考：[Gitea Documentation](https://docs.gitea.com/)  
组织仓库：`https://git.bddream.site/nyph/CursorAiOrg`

## 岗位

| 项 | 值 |
|----|-----|
| 岗位名 | Gitea 员工 / 仓库管理员 |
| Skill | `gitea-repo` |
| **归属** | **主控**（只接受主控派工；不自行开功能刀） |
| 记录 | `projects/<Project>/records/gitea/` 或组织级 `docs/gitea/` |

## 职责

1. **项目仓提交**：某主任务刀（有 GAME_ROOT 改动）在 REVIEW=PASS 后，经主程「主任务完成」通知主控 → 主控派本岗 → 在 **对应项目远程仓库** 写清变更说明并 `commit`（必要时 `push`，需主控/老板已配置凭据）。  
2. **组织仓提交**：主控与老板更新了 `rules/` / `workflow/` / `templates/` / `VERSION` 等组织内容后 → 主控派本岗 → 提交并推送到 **CursorAiOrg**。  
3. 不改业务逻辑；不越权改 ARCH；冲突时停工升级主控。

## 触发（强制）

```text
主程主任务完成通知
  → 主控
  → Task/代行 gitea-repo
  → 项目仓 commit（+ push 若可达）
  → records/gitea/COMMIT-D#.md

主控完成组织规则迭代（VERSION/CHANGELOG/rules 等）
  → Task/代行 gitea-repo
  → CursorAiOrg commit + push
  → docs/gitea/ORG-COMMIT-*.md
```

「主任务完成」定义：该刀 `ARCH` 批准且 `EXEC` 完成且 `REVIEW=PASS`（主程在 ARCH 或单独通知文件中声明闭环，或主控根据三件套齐全代认）。

## 提交规范（Git 学习要点）

遵循常见 Git / Conventional Commits 实践（摘要）：

1. **小而完整**：一次提交 = 一个逻辑变更；不混组织改与游戏改。  
2. **标题 ≤72 字，祈使语气，说明 why 导向的 what**：  
   `type(scope): summary`  
   - type：`feat` / `fix` / `docs` / `refactor` / `chore` / `org`  
   - scope：如 `atbs`、`scl`、`cursorteam`  
3. **正文**：做了什么、为什么、关键债/风险；可列文件级要点。  
4. **禁止**：密钥、大二进制、`--no-verify`（除非老板明示）、force push 主分支。  
5. **组织仓** type 常用 `org` 或 `docs`；**游戏仓** 用 `feat`/`fix` 等。  

模板：`templates/GIT_COMMIT.md`

## 远程对照（SCL 样板）

| 仓 | URL | 谁写 |
|----|-----|------|
| 组织 CursorAiOrg | `https://git.bddream.site/nyph/CursorAiOrg` | 组织规则/工作流迭代 |
| 项目 SCL | `http://192.168.3.23:3000/SCLG/SCL.git`（见 PROJECT.md） | D# 功能改动 |

## Gitea 侧注意

- 仓库在 Gitea 上托管；推送需账号权限（管理员由主控协调老板配置）。  
- PR/Issue/Actions 非本岗默认职责；本岗默认 **直推当前功能分支**（如 `autoAISkill`），除非主控要求开 PR。  
