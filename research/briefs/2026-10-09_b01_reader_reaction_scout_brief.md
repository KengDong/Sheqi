# b01_reader_reaction_scout｜B01并行实搜任务
status: ACTIVE / EXECUTE NOW
date: 2026-10-09
branch: b01-reader-reaction-scout
base: reboot-v6-verified-scene-lab
owner_role: b01_reader_reaction_scout

## 独占方向｜读者自发提名的名场面与爆笑脑洞
重点从真实读者自发讨论/书评/章评/论坛/社交媒体中挖掘被频繁记住、转述或主动推荐的具体小说名场面、荒诞事件、神反转、笑点与剧情爆发。尝试追到原作章节；严格区分真人讨论的证据、营销帖和未经核验的二手复述，不能把高赞评论当全体读者意见。可跨平台，但主调查对象是读者对某个具体情节的感受。

本窗口最重要的问题：
> 真实读者到底为什么主动复述哪一段，能否追到原文核验

避免：
> 不要只做热评词云/书名排行，不要捏造讨论或把零散评论升级成普遍结论。

## 共同方法
- 作者真正想要：**脑洞大开、剧情高效、实际读起来有意思**，不要求每章都搞笑。
- 研究单位：具体设定 PREMISE、真实事件 SCENE、可持续玩法 ENGINE；一个作品可提供多条，也可能一条都不给。
- **广搜**：多渠道、多轮次发现大量不重复的具体线索；总项目探索量级100–200乃至更多，不是上限，更非单一窗口必须凑满的数字。
- **分层证据**：RAW_DISCOVERED / SOURCE_LOCATED / SCENE_VERIFIED / CONTEXT_READ，只有合法阅读到真实内容才可声称验证。
- 每条记录：唯一 ID（本窗口使用自己的前缀）、作品+作者（可确认）、平台、URL与检索日期、1–3句具体场面/玩法、候选类型、证据等级、为何令人惊奇、叙事回报与后果、原文章节定位、真实读者反馈或UNKNOWN、去重识别。
- 搜索面大不等于随便造列表：没有真实出处不可当已核验，缺失要说明，允许对未核验线索持续追查。
- 保留失败/一般案例线索以比较，但是别为了凑表格花大把时间。
- 不复制小说整章、不绕收费、不写可直接发表的近似换皮稿；功能研究可以，商用原创必须改变具体故事表达和独特事件安排。
- 只做研究。不写程野、双世界道种或任何新小说正文；不挑定最后主题；作者先看候选再授权B02。

## 输出文件（只能本窗口写）
- `research/verified_scene_lab/lanes/reader/LEADS.md`：广搜去重线索库，含未核验状态。
- `research/verified_scene_lab/lanes/reader/VERIFIED_EVENTS.md`：已核验高质量事件卡，记录可复述的具体事件及真出处。
- `research/verified_scene_lab/lanes/reader/COVERAGE.md`：已搜/未搜类型、关键词线索、重复和证据局限、每批实际新增。
- `research/verified_scene_lab/lanes/reader/HIGHLIGHTS.md`：一眼看懂的候选精选，不限制全库规模；要标核验等级。
- `handoffs/b01_reader_reaction_scout/CURRENT.md` 和 `handoffs/b01_reader_reaction_scout/history/YYYY-MM-DD_batchN.md`：每批交接。
- Git commits 在自己的分支，完成可评审批次后向 `reboot-v6-verified-scene-lab` 开 Pull Request（可以留 open / draft），**不要自己合并**。

## 执行原则
1. 读取本 brief 后**立即外部搜索、获取原始资料**，不要用长篇计划替代实际研究。
2. 一轮能找到多少真实具体素材就提交多少；继续下一轮时在本分支追加，不能声称一轮已覆盖全部。
3. 所有本角色工作只写 `lanes/reader`、本角色 `handoffs/b01_reader_reaction_scout` 和自己 PR；**不要修改共享 `meta/` 文件、其它研究员目录或别人的分支**。这样三个 GPT 并行不冲突。
4. 先报告有限的真实结果，避免为了“100–200”虚构案例。批次结束后输出提交 SHA 和 PR 链接，并说明下一轮缺口。
5. 无法访问某章时写 UNKNOWN / NOT_READ，不要由书评反推正文的细节。


## 本轮最低验收（不以假数字充数）
- 实际完成一批来源可追溯的具体桥段/玩法搜索并写入LEADS。
- 抽取真的核验过的场面写入VERIFIED_EVENTS；不足就如实汇报。
- 记录本轮最想推给作者的具体名场面或创新机制及为什么有意思，不能只有“反差大/很爽”四字。
- Handoff、commit、PR，结束本批后停下让作者或统稿窗口决定是否继续本 lane。
