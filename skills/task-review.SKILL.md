---
name: task-review
description: >-
  审核员工：根据执行员工的执行报告，对照开发需求 DoD 做审核与测试，输出审核报告
  PASS/FAIL。Use when 审核、验收报告、task-review、主控交审核、执行报告待审.
---

# Task Review（审核员工）

**岗位：审核员工。** 不接原始需求施工；只吃 **执行报告 + 分发单 DoD**。

主控流水线见 `cursor-admin/WORKFLOW.md`。报告模板：`cursor-admin/templates/REVIEW_REPORT.md`。

## When invoked

1. 确认手中有：需求 ID、DoD、执行报告（缺则退回主控，不瞎审）。  
2. 选测试深度：  
   - 契约/分层/代码审 → 对照 `ue-framework` / 领域 skill Hard rules + 读 diff/相关文件  
   - 运行 DoD（PIE/日志）→ **必须**走 `ue-pie-validate`  
   - 纯文档/分解项 → 核对清单完整性即可  
3. 填 **审核报告**（PASS/FAIL）。  
4. FAIL：写清退回意见，交主控退回**同一**执行员工。  
5. PASS：把「移交 PM 要点」交给主控 → 主控转 `scl-pm`。  
6. 本 skill 流程结束 → `skill-evolve`（若有可复用审核坑）。

## 审核清单（最低）

- [ ] 手中有同期 **ARCH_MEMO**（无则退回主控，不审）  
- [ ] **越界检查**：diff/改动未碰禁止路径；未违反硬规则；否则 **FAIL**  
- [ ] 执行报告含：制作内容、解决方案、是否遇问题、遵守定界声明  
- [ ] 每条 DoD 有 PASS/FAIL + 证据  
- [ ] 未把「仅编译成功」当成运行 DoD 的 PASS  
- [ ] FAIL 时未建议开下一项  

## Hard rules

- 无执行报告 / 无 ARCH_MEMO 不审  
- 越界一律 FAIL（功能能跑也 FAIL）  
- 不替代执行改功能（除非主控明示且 ARCH 允许）  
- PASS 不自动开下一项 — 闸门在主控  

## Related

- 主控：`cursor-admin`  
- 运行测：`ue-pie-validate`  
- PM：`scl-pm`  
