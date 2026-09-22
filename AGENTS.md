# Sheqi AI 协作宪法

本仓库是《舍弃》项目的唯一长期权威记忆。聊天记录、单次模型记忆、临时脑洞均不能覆盖仓库中的已批准事实。

## 新会话启动顺序
任何 AI 在开始创作或修改前，必须依次读取：
1. `AGENTS.md`
2. `meta/COMMERCIAL_FIRST_PRINCIPLES.md`
3. `meta/STATE.md`
4. `meta/HANDOFF_PROTOCOL.md`
5. 当前角色的 `handoffs/<role>/CURRENT.md`
6. `canon/_INDEX.md`
7. 与任务相关的 `canon/` 文件
8. 当前卷 `outline/`
9. 当前章节卡
10. 最近相关 `manuscript/` 正文
11. 必要的 `research/` 资料

不得仅凭聊天记忆继续写作。

### 正式盲读例外
正式 clean-room 盲读为了避免设计污染，可以按 `meta/HANDOFF_PROTOCOL.md` 的盲读规则：
- 先读 `AGENTS.md`
- 读 handoff protocol
- 只读 blind_reader 的 clean-room handoff
- 再读 blind brief 指定材料

第一遍锁定前不得自行读取 State / Canon / 章卡设计理由 / 总评审结论。

## 商业第一性原理

正式总则：
> `meta/COMMERCIAL_FIRST_PRINCIPLES.md`

项目最高目标不是保护旧设计，而是：
> **让陌生普通读者从点开开始持续觉得新鲜、好看、爽、想继续读。**

因此：
- Frozen = 不得静默覆盖，不等于永远不能挑战；
- 旧Story Engine / Outline / 章卡 / 职业入口 / 写法若被真实Benchmark、原型、盲读或作者亲读证明伤害最高目标，必须主动提出Change Proposal；
- AI必须主动发现爽感、可读性、AI味、场景、节奏、重复与回报问题，不得把作者当基础QA；
- “借鉴热门小说”必须同时覆盖Concept、Architecture、Payoff、Scene/Prose、Long-Run Novelty，不得只拆Hook和结构；
- 交作者前必须尽可能完成Benchmark Comparator、Novelty & Payoff Audit、Canon/Continuity Gate、Human Prose Gate、Independent Red Team，必要时再做Fresh Blind Read。

权威层级仍然约束“怎么改”；商业第一性原理决定“该不该重新打开”。

## 权威层级
从高到低：
1. `manuscript/` 已批准正稿中的已发生事实
2. `canon/` 已批准世界设定
3. `outline/` 已批准未来规划
4. `meta/DECISIONS.md` 已批准决策
5. `drafts/` 草稿
6. `research/` 研究、拆解、灵感、候选方案

若低层与高层冲突，不得静默选择；应登记冲突并由作者决定是否改 Canon、改大纲或 Retcon。

## Canon 变更规则
Bible V1.0 已冻结。AI 不得静默修改 Canon。

任何底层规则变更必须先写成 Proposal，说明：
- 当前 Canon
- 拟修改内容
- 修改理由
- 影响的人物/大纲/伏笔/已写正文
- 是否需要 Retcon

然后经过独立审核和作者明确确认，才允许合并。

## 正文流程
研究/提案 -> 作者确认 -> 大纲 -> 章节卡 -> 初稿 -> 审稿 -> 修订 -> 作者确认 -> 正稿。

正式正文前必须检查：
- 连续性
- 人物知识边界
- 时间线
- 世界规则
- 伏笔状态
- 物品/伤势/关系状态

## 禁止事项
- 为了高潮临时新增规则。
- 把候选脑洞当成已确定事实。
- 自动恢复已经明确不可恢复的舍弃。
- 用“系统扫描”替代人物调查、定相与推理。
- 因新点子更酷而偷偷覆盖旧设定。
- 先决定角色要舍什么，再倒推“这个境界刚好需要它”。
- 把舍台写成能无目标扫描全部人格、自动推荐最佳舍项的面板。
- 未经批准把 draft 视为 manuscript。

## 项目当前原则
当前处于 **Bible V1.0 Frozen -> 第一卷故事研发** 阶段，尚未开始正式正文。

底层系统默认停止扩张。新的工作优先回答：
> 谁想要什么？谁阻止他？发生什么不可逆变化？

而不是继续增加新的修炼系统、余器类别或终极奥秘。


## 窗口交接是任务完成条件

任何长期GPT窗口每完成一个任务，必须同时：

1. 更新自己的：
   `handoffs/<role>/CURRENT.md`
2. 新增一份：
   `handoffs/<role>/history/YYYY-MM-DD_<task-slug>.md`

正式规则：
> `meta/HANDOFF_PROTOCOL.md`

没有完成 handoff：
> **任务流程视为未完成。**

交接必须记录：
- 实际完成了什么；
- 作者是否否决/修正；
- 哪些旧方向不能继续；
- 当前权威输出；
- 未决问题；
- 下一步；
- 新窗口必须读取的最小文件。

Git 是长期记忆。
聊天窗口不是长期权威。
