# ARCH_MEMO · D4 cloud-resume 续温脚本

- **Project：** OrgOps
- **需求 ID：** D4
- **主程：** 主控直干（昴书面指令：`bash cloud-resume.sh OrgOps`）
- **栈适配器：** 无

## 定层

- 层：接单入口（可执行续温，只读）
- 理由：续温协议要求读盘；Cloud 会话需要一条可重复命令。现场执行 `bash cloud-resume.sh OrgOps` 得到 exit 127，脚本不在本仓、不在 PATH。

## 允许改的路径

- 本仓根 `cloud-resume.sh`（必须让用户那条命令在 PROJECT_ROOT 直接可跑）
- `projects/OrgOps/PROJECT.md` · `AGENTS.md` · `README.md`（接单补这一条命令）
- `projects/OrgOps/records/**`（D4 闸门文件 + BOARD/BACKLOG）

## 禁止改的路径（越界红线）

- 拷贝 Gitea 网络脚本 / 主机环境写入
- 合入 `CursorSkillSearch` skills
- 改 `Command/人设.md`
- 脚本改 git 配置、代理、系统设置
- 脚本把 token / 带凭证的 remote URL 打到 stdout

## 硬规则

- 默认只读：不改 BOARD、不 commit、不 push
- 未知 ProjectId → 非 0 退出
- 缺 PROJECT/RULES/BOARD/BACKLOG → 非 0 退出
- 一次只做续温入口，不顺手开 D1 升格策略

## 非目标

- 不是 My Machines worker 拉起器
- 不是恢复被归档的 Cloud Agent
- 不是 SCL 续温（SCL 不在本仓；参数不是 OrgOps 时只查 `projects/<Id>`，没有就失败）

## 主程签字

- 结论：**批准开工**
