---
status: approved-process
version: 1.1
created_at: 2026-09-22
authority: author-approved-process-extension
canon_effect: none
outline_effect: none
---

# TASK DISPATCH PROTOCOL｜Git任务派发协议 V1

## 0. 目标
让长期窗口之间的任务派发不依赖作者手工复制聊天内容。

原则：
> **任务说明写进Git，窗口只按CURRENT读取。**

## 1. 正式任务的最小三件套
任何跨窗口正式任务都必须同时存在：

1. **Brief**
   - 路径：`research/briefs/` 或与任务类型匹配的正式目录；
   - 说明角色、目标、输入、输出、Gate、禁止事项、handoff要求。

2. **目标窗口CURRENT**
   - 必须写明：
     - status；
     - current_task；
     - brief path；
     - blocked_by / prerequisites；
     - NEXT EXPECTED ACTION；
     - REQUIRED READS；
     - DO NOT CONTINUE。

3. **ACTIVE_WORKSTREAMS**
   - 全局记录：
     - 哪个窗口ACTIVE / PAUSED / BLOCKED / QUEUED；
     - 当前任务；
     - 上游依赖；
     - 下一次Gate；
     - 谁负责最终审批。

三件套缺一：
> **不算正式下发。**

## 2. 状态定义
- **ACTIVE**：可立即执行当前brief。
- **PAUSED**：没有当前执行任务，等待上游结果。
- **BLOCKED**：任务已定义，但前置条件未满足。
- **QUEUED**：下一任务已准备好，但尚未授权启动。
- **CLEAN-ROOM**：正式盲读，不可读设计污染资料。
- **RETIRED**：该长期角色暂时退出。

## 3. 作者如何启动窗口
正常情况下，作者无需再复制长任务说明。

作者只需在目标窗口说：
> **继续 Sheqi，按 Git CURRENT 执行。**

新窗口必须按：
1. AGENTS.md
2. meta/FIRST_PRINCIPLES_FICTION_RND_OS.md（clean-room例外）
3. meta/STATE.md（clean-room例外）
4. meta/HANDOFF_PROTOCOL.md
5. 自己的 CURRENT
6. CURRENT中的REQUIRED READS
7. CURRENT指定brief

恢复任务。

## 4. 总评审如何下发
总评审完成上游审批后：

1. 写/更新目标brief；
2. 更新目标CURRENT；
3. 更新ACTIVE_WORKSTREAMS；
4. 如有必要同步STATE；
5. 更新editor_in_chief CURRENT + history；
6. 然后才宣布“任务已下发”。

不得：
- 只在聊天里给任务；
- 让作者复制长提示；
- CURRENT还是旧任务却口头说“你去做新任务”；
- 没有brief就让窗口凭聊天摘要执行。

## 5. Authority Gate
若任务涉及：
- Canon Change；
- Approved Outline Change；
- 正式正文批准；

必须在CURRENT和ACTIVE_WORKSTREAMS里明确写：
> **WAITING FOR AUTHOR / APPROVAL REQUIRED**

在作者明确批准前：
- brief可以预写；
- 状态只能是QUEUED/BLOCKED；
- 不得执行权威修改。

## 6. 任务完成后的自动交接
执行窗口完成任务时必须：
1. 写产物；
2. 更新自己的CURRENT；
3. 新增history；
4. 若结果需要总评审，CURRENT状态改为PAUSED / AWAITING REVIEW；
5. 在NEXT EXPECTED ACTION写：
   > 总评审读取哪些文件、做什么判断。

总评审完成后再负责下一轮跨窗口派发。

## 7. 防状态漂移
总评审每次阶段切换必须检查：
- STATE；
- ACTIVE_WORKSTREAMS；
- editor_in_chief CURRENT；
- 受影响角色CURRENT。

如果出现：
> 某文件写ACTIVE，而实际已经DONE/PAUSED

必须在本轮修正。

## 8. 当前Sheqi应用｜REBOOT-V3

Current authority:
> `meta/CURRENT_AUTHORITY.md`

Current task:
> `handoffs/newcomer_breakout_market_scout/CURRENT.md`

Current brief:
> `research/briefs/2026-09-25_b_lane_newcomer_breakout_dossier_brief.md`

All old D-00xx / D-01xx task chains:
> history/evidence only unless CURRENT_AUTHORITY explicitly reactivates them.

Hard:
> no new task may be dispatched from a historical NEXT field.

