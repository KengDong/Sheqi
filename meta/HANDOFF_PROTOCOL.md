---
status: approved-process
version: 1.1
created_at: 2026-09-21
authority: author-approved-process
canon_effect: none
outline_effect: none
---

# HANDOFF PROTOCOL｜窗口交接与续接规则 V1

> 目标：
>
> **聊天窗口会满，Git仓库不会。任何长期任务都必须把“继续工作所需的最小上下文”留在仓库里，而不是留在某个聊天窗口里。**

---

# 0. 核心原则

1. **任务产物不等于交接信息。**
   - research/review/outline/draft 记录“做了什么”；
   - handoff 记录“下一个窗口怎样继续而不走偏”。

2. **每个窗口每完成一个任务，都必须写交接。**
   - 没有 handoff，任务视为流程未完成。

3. **CURRENT 是当前入口，history 是不可变历史。**
   - `CURRENT.md` 永远只保留该窗口最新可接续状态；
   - `history/` 每次任务结束新增一份，不覆盖旧记录。

4. **handoff 不能创造新权威。**
   - 它只总结并指向 repo 中真正的 Canon / Outline / Decision / Review / Draft。
   - 与高权威文件冲突时，以高权威文件为准。

5. **禁止只写“已完成，请看文件”。**
   - 必须把最容易丢失的判断、作者反馈、失败路线、下一步和禁区写清楚。

---

# 1. 目录

```text
handoffs/
  README.md
  editor_in_chief/
    CURRENT.md
    history/
  opening_writer/
    CURRENT.md
    history/
  mid_continuity/
    CURRENT.md
    history/
  visual/
    CURRENT.md
    history/
  blind_reader/
    CURRENT.md
    history/
```

角色映射：

- `editor_in_chief` = 总评审 / 总编窗口
- `opening_writer` = 开头 / 主作者窗口
- `mid_continuity` = 中段+衔接 / 研究、红队、编辑窗口
- `visual` = 视觉窗口
- `blind_reader` = 盲读窗口

以后新增长期窗口：
> 必须新增独立目录，不要共用别人的 CURRENT。

---

# 2. 新窗口启动顺序

普通长期窗口：

1. `AGENTS.md`
2. `meta/STATE.md`
3. `meta/HANDOFF_PROTOCOL.md`
4. 自己角色的 `handoffs/<role>/CURRENT.md`
5. `canon/_INDEX.md`
6. CURRENT 中列出的“必须读取”
7. 当前任务 brief
8. 需要的源文件

原则：

> **先读 CURRENT，知道“为什么现在做到这里”；再读具体资料。**

不要先把整个仓库从头扫一遍。

---

# 3. 正式盲读的 Clean-room 例外

正式文本盲读需要避免设计污染。

因此新的干净盲读窗口启动时：

1. `AGENTS.md`
2. `meta/HANDOFF_PROTOCOL.md`
3. `handoffs/blind_reader/CURRENT.md` 中的 clean-room 部分
4. 当前 blind brief 指定的材料

在第一遍盲读锁定前，不读：
- `meta/STATE.md`
- `meta/DECISIONS.md`
- Canon
- 章卡设计理由
- 总评审结论
- 作者预期

若任务 brief 明确要求两阶段：
> 第一阶段盲读锁定后，第二阶段再读取允许的权威材料。

---

# 4. 每次任务结束必须写两份

## A. 更新 CURRENT

路径：
> `handoffs/<role>/CURRENT.md`

CURRENT 必须包含：

### 1. ROLE
- 当前角色
- 当前是否 ACTIVE / PAUSED / RETIRED / CLEAN-ROOM

### 2. LAST COMPLETED TASK
- 任务名
- Issue（如有）
- 任务 brief
- 完成时间

### 3. WHAT ACTUALLY HAPPENED
不写流水账。
只写：
- 最重要结论；
- 作者后来有没有否决；
- 哪些旧结论已失效；
- 哪些判断仍有效。

### 4. AUTHOR FEEDBACK
必须原义记录作者关键反馈。
特别是：
- “这版看不下去”
- “这个方向太机械”
- “不要顺着我举的例子”
这类会改变后续判断的问题。

### 5. AUTHORITY / OUTPUTS
列出：
- 正式冻结文件；
- review；
- research；
- draft；
- decision；
- commit / issue（有则写）。

### 6. DO NOT CONTINUE
明确写：
- 不要恢复哪些旧任务；
- 不要继续润色哪些被否稿；
- 不要默认哪些候选已批准。

### 7. OPEN QUESTIONS
只写真正未决问题。

### 8. NEXT EXPECTED ACTION
下一个窗口接手后：
> 第一件事做什么。

### 9. REQUIRED READS
控制在最小必要集合。
不要列整个仓库。

### 10. CONTEXT SNAPSHOT
最多15条。
让新窗口3分钟内知道当前局面。

---

## B. 新增 history 快照

路径：

> `handoffs/<role>/history/YYYY-MM-DD_<task-slug>.md`

内容与 CURRENT 同结构，但：
- 不覆盖；
- 永久保留当时状态；
- 后续即使方向被推翻，也能追溯“为什么当时这么做”。

---

# 5. handoff 写入时机

必须在以下动作之前或同时完成：

- 宣布任务完成；
- 关闭 Issue；
- 把窗口切到新角色；
- 让作者去另一个窗口下新任务。

流程：

> 任务产物完成
> -> handoff CURRENT + history
> -> STATE / issue更新
> -> 才算交付完成。

---

# 6. handoff 不允许做什么

禁止：

- 把 research 候选写成已批准事实；
- 用聊天记忆覆盖 Git；
- 省略作者否决；
- 省略失败稿；
- 只记录成功，不记录“为什么不能继续”；
- 把自己窗口的观点伪装成总评审决定；
- 把 CURRENT 写成长篇百科。

CURRENT 应该像：
> **机场交接班记录。**

不是：
> 项目全史。

---

# 7. 推荐 handoff 模板

```markdown
# <ROLE>｜CURRENT HANDOFF

## ROLE
- role:
- status:
- current_issue:

## LAST COMPLETED TASK
- task:
- brief:
- completed_at:

## WHAT ACTUALLY HAPPENED
- ...

## AUTHOR FEEDBACK
- ...

## AUTHORITY / OUTPUTS
- ...

## DO NOT CONTINUE
- ...

## OPEN QUESTIONS
- ...

## NEXT EXPECTED ACTION
1. ...

## REQUIRED READS
1. ...

## CONTEXT SNAPSHOT
- ...
```

---

# 8. 总评审额外职责

总评审窗口每次批准 / 否决 / 改变阶段后，必须同时：

1. 更新自己的 `CURRENT.md`；
2. 检查被影响窗口的 CURRENT 是否已经过期；
3. 若过期，直接更新它们的：
   - status；
   - DO NOT CONTINUE；
   - NEXT EXPECTED ACTION。

这样即使原窗口突然满了：
> 新开的替代窗口也不会沿着旧任务继续跑。

---

# 9. 长期原则

> **聊天窗口只负责思考；Git负责记忆。**

任何“如果这个窗口消失，新窗口就不知道”的信息：
> 都不应该只存在聊天里。


---

# 10. Git任务派发｜禁止依赖作者手工复制长提示

正式任务派发规则：
> `meta/TASK_DISPATCH_PROTOCOL.md`

从V1.1起，长期窗口之间不再以“作者复制一大段聊天提示”为标准交接方式。

总评审/上游窗口下发正式任务时必须：

1. 先把任务要求写成仓库中的正式 brief；
2. 更新目标角色的 `handoffs/<role>/CURRENT.md`：
   - status；
   - current_task；
   - exact brief path；
   - blocked_by / prerequisites；
   - REQUIRED READS；
   - DO NOT CONTINUE；
3. 同步 `meta/ACTIVE_WORKSTREAMS.md`；
4. 若任务仍被Authority Gate阻塞，标记为 `QUEUED / BLOCKED`，不得让目标窗口提前执行；
5. 只有Git中的brief + CURRENT同时就绪，才算“已下发”。

作者之后不需要手工复制任务正文。
新窗口只需按启动顺序读取自己的CURRENT和其中引用的brief即可恢复。

---

# 11. Task-Close Integrity Check｜任务关闭完整性检查

每个长期窗口宣布任务完成前，除CURRENT + history外，还必须完成一次最小闭环核对：

- [ ] 任务产物已落库；
- [ ] CURRENT已更新；
- [ ] history已新增；
- [ ] 旧结论/失败路线已写入DO NOT CONTINUE；
- [ ] AUTHOR FEEDBACK已记录；
- [ ] REQUIRED READS是最小必要集合；
- [ ] 如影响其它窗口，已通知总评审同步其CURRENT；
- [ ] 如改变全局工作流，已同步 `meta/ACTIVE_WORKSTREAMS.md`；
- [ ] 不存在“Git显示ACTIVE，但实际已DONE/PAUSED”的明显状态漂移。

若任一关键项缺失：
> **任务不得视为完整关闭。**

---

# 12. 总评审的跨窗口同步责任｜扩展

总评审每次完成以下任一动作：
- 批准/否决；
- 阶段切换；
- Authority Gate变化；
- 任务优先级变化；
- 上游产物使下游brief失效；

必须同时执行：

1. 更新 `handoffs/editor_in_chief/CURRENT.md`；
2. 更新 `meta/ACTIVE_WORKSTREAMS.md`；
3. 检查所有受影响长期窗口CURRENT；
4. 将过期窗口改成：
   - ACTIVE；
   - PAUSED；
   - BLOCKED；
   - QUEUED；
   - RETIRED；
   之一；
5. 若下一个任务已经明确，直接写出/更新正式brief并挂到目标CURRENT；
6. 新增editor_in_chief history快照。

目标：
> **任何一个窗口突然达到上下文上限，新窗口只读Git即可继续，不需要作者恢复任务说明。**
