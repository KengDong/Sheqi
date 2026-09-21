---
status: ready
document_type: visual-bible-skeleton-task-brief
project: 修仙先舍一件人间事
created_at: 2026-09-21
authority: process
canon_effect: none
outline_effect: none
---

# Visual Bible Skeleton + 内部空间资产规则｜任务书

## 角色定位

> **视觉连续性工程师**

本轮不生成正式人物脸，不公开剧情插画。

已有研究：
- `research/reports/2026-09-21_visual_bible_and_illustration_continuity_study.md`
- `reviews/2026-09-21_visual_bible_illustration_continuity_final_audit.md`

目标：

> 先建立可长期维护的视觉资产制度，让未来任何AI绘图都从 approved reference assets 出发，而不是每次重新抽角色。

---

# 一、必须读取

1. `AGENTS.md`
2. `meta/STATE.md`
3. `meta/DECISIONS.md` D-0031
4. `outline/chapter_cards/volume1_ch001_003.md`
5. `outline/chapter_cards/volume1_ch004_010.md`
6. visual research + final audit

---

# 二、Visual Bible Skeleton

必须设计未来目录：

```
visual/
  bible/
  characters/
  scenes/
  props/
  illustrations/
  qa/
```

并给每层定义：
- 什么能进；
- 谁批准；
- 版本怎么升；
- 与文字冲突怎么办。

正式权威关系：

> manuscript > Canon > approved Outline > approved chapter cards > visual approved assets > visual exploration

图不能反向静默改故事。

---

# 三、硬门QA

不要100分总分制作为主要门槛。

必须建立 **hard gates**：

任何一项失败直接退回：
1. 人脸身份明显漂移；
2. 关键发型锚点漂移；
3. 身高 / 体型破坏角色关系；
4. 伤势 / 服装剧情时间错误；
5. 场景空间与批准章卡冲突；
6. 提前剧透；
7. 新增Canon没有的可见特征；
8. 左右手 / 工具位置导致剧情错误。

通过硬门后，才允许软评：
- 构图；
- 光；
- 材质；
- 氛围；
- 完成度。

---

# 四、角色reference制度

当前只定义流程，不生成正式母脸。

流程：

> 文字视觉卡 -> V0 6—10个差异化方向 -> 作者筛2—3个 -> turnaround -> 表情 / 全身 -> approved master -> 后续reference生成/编辑。

不得：
- 一上来20—40张抽卡；
- 只靠seed；
- 只靠角色名字；
- 只靠同一prompt；
- 假设跨会话模型会记住脸。

必须设计：
- reference ID；
- 版本号；
- outfit版本；
- injury/state版本；
- 禁止漂移字段。

---

# 五、第一阶段内部空间资产

本轮不画图，但必须把需要锁的**文字空间字段**定义清楚。

优先：

## 1. 固定中转台
至少字段：
- 正常货路；
- F转运架；
- 导向结构；
- 凹入式舍台服务位；
- O外环；
- S核心；
- R封存格；
- B辅助制动 / 牵引结构；
- W工作位；
- 安全线；
- 救援方向；
- 光源；
- 正常 / 事故状态版本。

## 2. 驿货行
- 货流入口 / 出口；
- 常用工作区；
- 夜班汤 / 休息位置；
- 工具；
- 光源；
- 材质；
- 阶层感；
- 普通低阶灵力怎样进入劳动。

## 3. 合租屋
- 共用桌面；
- 吃饭位置；
- 工具 / 旧零件区；
- 手艺学徒工作面；
- 灶；
- 收纳；
- 光；
- 两人的边界如何长期变化。

## 4. 全局风格板字段
先定义：
- 半写实国风为主候选；
- 正常世界的材质；
- 穷但不脏；
- 舍务正规而非邪教；
- 修仙不靠满屏发光特效。

---

# 六、哪些内容现在禁止视觉定稿

- 余世真实形态；
- 弃相终极形态；
- 漏舍永久可视特效；
- 第一件正式余器；
- 卷末复合余灾最终形态；
- 合租旧友正式人脸；
- 曹闻川正式母脸；
- 陆野最终公开母脸。

可以做V0探索，但不能公开成事实。

---

# 七、插图策略

正式记录：

> **正文低密度功能图 + 内部空间图 + 宣传图重点投入。**

必须分别列：
- 内部QA图；
- 正文可选图；
- 宣传图；
- 不建议图。

正文必须满足：
> 没图也能完全读懂。

---

# 八、最终输出

`reviews/2026-09-21_visual_bible_skeleton_proposal_for_audit.md`

必须包含：
1. 目录架构；
2. 权威层级；
3. hard-gate QA；
4. reference资产流程；
5. 版本命名；
6. 四类第一阶段空间字段；
7. 当前允许V0探索清单；
8. 禁止定稿清单；
9. 插图密度策略；
10. 未来真正开始生成图片时的单次任务模板。

不得生成正式插图。
