---
status: queued
version: 1.0
document_type: opening-writer-commercial-prose-calibration-brief
project: 修仙先舍一件人间事
created_at: 2026-09-22
authority: process
canon_effect: none
outline_effect: none
blocked_by: issue-36
parallel_with: issue-37
---

# Opening Writer Commercial Prose Calibration｜开头Writer商业正文校准

## 身份

> **Opening Writer / Commercial Prose Calibration Writer**

本任务不是写正式第一章。

目的：
> **在第一卷架构最终重构期间，提前把Writer本身的正文执行能力校准到“成熟商业网文正常区间”，避免新架构出来后再次因为AI腔、场景不清、对白黑话而返工。**

---

# 0. 启动条件

本任务只有在 #36 Commercial Prose Calibration 经总评审通过后才能启动。

启动后可与 #37 Commercial First-Principles Volume 1 Rebuild 并行。

原因：
- #36负责建立“标准”；
- #38负责证明Writer能不能实际写到这个标准；
- #37负责重构“写什么”；
- 三者职责不得混淆。

当前 #36 未通过前：
> **Opening Writer继续暂停。**

---

# 1. 启动后必读

1. `AGENTS.md`
2. `meta/COMMERCIAL_FIRST_PRINCIPLES.md`
3. `meta/STATE.md`
4. `meta/HANDOFF_PROTOCOL.md`
5. `handoffs/opening_writer/CURRENT.md`
6. #36总评审批准后的：
   - Commercial Prose Benchmark；
   - Reference Cards；
   - HUMAN PROSE GATE；
   - A-T1 Commercial Gap Audit；
   - Reader Scene Map；
   - Reader-Language Patch。
7. `meta/PROSE_BIBLE.md`
8. `meta/PROSE_PLAYBOOK.md`

不要把旧A-T1原型当文风模板。

---

# 2. 本轮只校准“怎么写”，不决定“写什么”

禁止：
- 决定A-T1/C-T2谁胜；
- 改Opening Architecture；
- 改Story Engine；
- 改Canon；
- 改正式Outline；
- 偷写完整第一章。

即使#37正在挑战现有开篇，#38也只训练可迁移的正文能力。

---

# 3. 写三个功能型微型样本

每篇约 **700—1100汉字**。

不是三个故事方案，而是三个写作能力测试。

## Sample A｜高压场景可视化

目标：
- 读者150字内知道人在哪、什么在危险、谁被困；
- 主要物理锚点不超过3个；
- 陌生器物先有形状/位置/作用，再给短称；
- 动作连续，读者可画简图；
- 不靠零件名制造专业感。

情节可使用A'事故的固定物理真值，但不得推进正式剧情。

## Sample B｜核心机制自然入门

目标：
- 让第一次读者自然理解“舍味”；
- 讲清：舍什么、永久后果、为什么备、为什么有用、为什么不是换力量；
- 不写成百科；
- 不靠两个人互相说早就知道的设定；
- 允许必要的直接叙述。

## Sample C｜活人感 / 日常声线

目标：
- 写陆野与1名普通同工/生活人物的短场景；
- 展示陆野现实、算账、轻嘴贫、手上实在；
- 有生活纹理，但不是为了“惜物文学”；
- 对话允许含糊、打断、没说全；
- 场景必须仍有一个小目标/小变化，不能变纯闲聊。

---

# 4. 每篇必须过Human Prose Gate

Writer自己先检查：
- 500字能否复述；
- 空间能否画；
- 新词能否说出功能；
- 对白能否翻成人话；
- 有没有Camera Jump；
- 有没有动作→对白→解释模板循环；
- 有没有API Dialogue；
- 有没有“不是X而是Y”机械堆叠；
- 有没有每句都太精确；
- 有没有明显设计文档标签；
- 有没有一眼AI的段落节奏。

不能只写“已通过”。

必须逐项指出：
> 哪一句/哪一段最危险，以及自己怎么处理。

---

# 5. Commercial Shelf Test

三个样本完成后，Writer自己不能宣布“像资深作者”。

只提交给总评审/Commercial Comparator。

总评审会重点判断：
> **如果把这三段混进成熟男频商业小说片段里，它们是否仍一眼显得像AI/项目稿？**

不通过：
> 继续校准Writer，不进入完整Ch1。

通过：
> 形成Opening Writer Prose Baseline。

---

# 6. 输出

1. `experiments/prose_calibration/2026-09-22_opening_writer_scene_clarity_sample.md`
2. `experiments/prose_calibration/2026-09-22_opening_writer_core_mechanism_sample.md`
3. `experiments/prose_calibration/2026-09-22_opening_writer_human_texture_sample.md`
4. `reviews/2026-09-22_opening_writer_commercial_prose_selfcheck.md`

不得写正式Ch1。

---

# 7. 完成后

按 `meta/HANDOFF_PROTOCOL.md`：
- 更新 `handoffs/opening_writer/CURRENT.md`；
- 新增history；
- 然后停止。

由总评审做Commercial Shelf Test。

只有：
> **#37最终Opening方向冻结 + #38 Writer Prose Baseline通过**

两者同时成立后，才下发：
> **完整第一章正式Draft任务。**