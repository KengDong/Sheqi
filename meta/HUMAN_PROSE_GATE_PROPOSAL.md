---
status: proposal
version: 1.1
document_type: human-prose-gate
project: 修仙先舍一件人间事
created_at: 2026-09-22
verified_at: 2026-09-22
authority: proposal-only
canon_effect: none
outline_effect: none
source_report: research/reports/2026-09-22_commercial_prose_execution_benchmark.md
---

# HUMAN PROSE GATE V1.1｜商业正文人类可读性闸门 PROPOSAL

> 目标不是“更文学”。
>
> 目标：
>
> **作者看到正文前，先由AI挡掉：看不懂、看不见、像说明书、像Scene Spine扩写、像API对白、像AI刻意完整。**

---

# 0. 建议放置位置

> Scene Spine  
> -> Reader-Language Sheet  
> -> Functional Reference Cards  
> -> Draft  
> -> Commercial Prose Comparator  
> -> **HUMAN PROSE GATE**  
> -> Prose Editor  
> -> Independent Red Team  
> -> Fresh Blind Reader（必要时）  
> -> Author Taste Review

作者不再承担基础QA。

---

# G1｜500字复述门【HARD】

第一次读者读完关键开场约500字，应能不用项目术语回答：

1. 谁是当前主视角？
2. 人大概在哪？
3. 主角正在做什么？
4. 当前最大问题/欲望是什么？
5. 失败会怎样？
6. 场上最重要的东西大概长什么样/干什么用？

若3项以上只能答：
> “好像是什么装置/流程/专业操作。”

直接FAIL。

---

# G2｜空间草图门【HARD for action scenes】

一个主要动作beat后，第一次读者必须能画最低三锚：

- 主角；
- 危险/目标物；
- 受害者/对手/关键关系对象。

只要求相对位置，不要求工程图。

### FAIL
- 左/右/几丈外很多，却不知道相对什么；
- 新零件持续加入但主锚不稳定；
- 必须回翻才能知道人站哪。

---

# G3｜陌生物件功能门【HARD】

重要陌生物第一次出现后，读者至少能说：

> “它大概是什么类别，现在为什么重要。”

不要求精确术语定义。

### FAIL
物件首见同时要求读者猜：
- 名字；
- 形状；
- 空间位置；
- 功能；
- 故障模式。

---

# G4｜术语功能门【HARD】

任何当前因果依赖的新术语，第一次出现后应能翻成一句普通话。

例如《舍弃》：
> “舍味”至少要能被理解成：永久失去味觉，用来降低这次续我需要带过去的“自己”；不是凭空换力量。

不要求Canon全定义。

### FAIL
读者只能复述原词，不能说明当前作用。

---

# G5｜对白翻译门【HARD】

每句关键专业对白，第一次读者都应能回答：

> “这人现在是在叫对方做什么 / 警告什么 / 拒绝什么？”

### HARD FAIL
- 一句依赖3个以上首次出现专名；
- 两个圈内人互相复述双方都懂的规则；
- 紧急现场说完整制度句；
- 像API返回状态。

---

# G6｜Camera Continuity【HARD】

相邻段落之间，必须能解释：

- 人有没有移动；
- 视线为什么转；
- 新东西从哪里进入；
- 操作对象是否还是之前那个。

### FAIL
前一句手边闸柄，下一句突然操作远处控制扣，但从未建立两者关系。

---

# G7｜Lived Texture【SOFT；连续失败升级HARD】

检查：

> 除了为剧情功能/规则因果服务的细节，人物是否仍像真的活在这个空间里？

可来自：
- 身体小反应；
- 熟人习惯；
- 工具磨损；
- 吃喝；
- 钱；
- 一个不需要回收成伏笔的小动作。

### WARN
连续800—1200字所有细节都能在Scene Spine中找到对应功能。

### HARD FAIL
连续多个场景都像：
> 每个物件是机关，每句话是信息，每个动作是证明。

---

# G8｜Paragraph Rhythm【SOFT/HARD】

连续5—8段检查“功能节奏”，不是字数。

高风险模板：

> 动作  
> -> 对白  
> -> 作者解释  
> -> 防误读  
> -> 新动作  
> -> 对白  
> -> 再解释

连续两轮以上明显复现：
> FAIL。

允许：
- 连续对白；
- 连续内心；
- 一段直接说明；
- 一段较长环境；
只要与当前认知任务匹配。

---

# G9｜Explanation Burden【HARD】

同一规则第一次出现，原则上只设一个主要解释渠道：

- 近距叙述；
- 真知识差对白；
- 动作后果；
- 主角当前判断。

其它渠道只能补新信息。

### HARD FAIL
同一事实：
> 对白解释一次 -> 旁白再解释 -> 内心再确认。

A-T1原版“舍味不产力量”就是典型。

---

# G10｜AI-Smell Scan【HARD】

逐项扫：

1. API对白；
2. 作者工程标签泄漏；
3. 名词串；
4. 机械三连/四连；
5. 高频“不是X而是Y”；
6. 每段都有作者结论；
7. 人人说话都过于精准；
8. 规则解释比现场画面更清楚；
9. 情绪被作者命名多于被动作/身体呈现；
10. 章卡措辞进入正文；
11. 每个细节都只有剧情功能；
12. 为防误读而重复边界条件。

命中3项以上：
> 不送作者，先Commercial Comparator返工。

---

# G11｜Core-Premise Clarity Exception【HARD】

重要补丁：

> **“自然”不等于把标题级核心压成黑话。**

若当前选择必须理解核心机制，可以直接用一小段普通叙述讲清。

A-T1第一次“舍味”至少应让读者知道：

- 舍掉什么；
- 永久；
- 什么不会自动一起消失（只给当前需要层级）；
- 为什么陆野早就准备它；
- 为什么这次到了执行阈值；
- 它不直接增加力量；
- 为什么仍能帮助他完成筑基最后一步。

不必全部塞进对白。

---

# G12｜Shelf Test【FINAL HARD】

Commercial Comparator选2—4个功能相邻成熟公开正文样本，遮掉作者名对比当前500—1200字。

只问：

> **是不是一眼就能看出《舍弃》这一段更像AI / 设计稿扩写？**

检查：

1. 我们是否更晚才让读者知道人在哪？
2. 我们是否名词更多、画面更少？
3. 我们对白是否更像接口？
4. 我们是否每个动作后都解释原因？
5. 我们段落功能是否过于均匀？
6. 我们是否缺少活人纹理？
7. 我们是否“规则零歧义、场景高歧义”？
8. Scene Spine骨架是否肉眼可见？

只要独立Comparator判断：
> “是，明显。”

则FAIL。

---

# G13｜Author-Should-Not-Catch-This【FINAL RED TEAM】

交作者前最后自问：

> **一个完全不知道设定的普通读者，是否还能很轻易指出：**
>
> - “这里不像小说。”
> - “这里我看不懂。”
> - “这句像AI。”
> - “他们为什么这样说话？”
> - “我不知道这个东西在哪。”
> - “作者怎么又解释了一遍？”

只要答案是“很可能”：
> **继续修，不交作者。**

这一Gate不是taste门。

它专门阻止：
> 把基础可读性QA继续外包给作者。

---

# 14. Gate输出模板

| Gate | PASS / WARN / FAIL | 证据位置 | 修复责任 |
|---|---|---|---|
| G1 500字复述 | | | |
| G2 空间草图 | | | |
| G3 物件功能 | | | |
| G4 术语功能 | | | |
| G5 对白翻译 | | | |
| G6 Camera | | | |
| G7 Lived Texture | | | |
| G8 Paragraph Rhythm | | | |
| G9 Explanation Burden | | | |
| G10 AI-Smell | | | |
| G11 Core Premise | | | |
| G12 Shelf Test | | | |
| G13 Author-Should-Not-Catch-This | | | |

---

# 15. 与现有规则体系的关系

本Gate不替代：

- `meta/PROSE_BIBLE.md`
- `meta/PROSE_PLAYBOOK.md`
- `meta/READER_LANGUAGE_GATE.md`
- `meta/READER_LANGUAGE_MAP.md`

它补的是以前缺失的外部比较：

> **“项目内部规则都对，但放成熟商业正文旁边是不是仍不正常？”**

---

# 16. 不机械KPI化

以下不设死数字：
- 句长；
- 每段几句；
- 每千字感官数；
- 每章对白比例；
- 每场新词数。

“500字复述”“三锚空间”等只是测试工具，不是写作模板。

---

# 17. A-T1当前预判

以现原型为准：

- G1：WARN / FAIL
- G2：FAIL
- G3：FAIL
- G4：WARN
- G5：FAIL
- G6：FAIL
- G7：WARN
- G8：WARN
- G9：FAIL
- G10：FAIL
- G11：WARN
- G12：FAIL
- G13：FAIL

详细证据：
> `reviews/2026-09-22_AT1_commercial_prose_gap_audit.md`

> 本文件待总评审批准后，才升级为正式process gate。
