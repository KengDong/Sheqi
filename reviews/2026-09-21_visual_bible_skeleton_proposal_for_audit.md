---
status: proposal-for-audit
document_type: visual-bible-skeleton-proposal
project: 修仙先舍一件人间事
created_at: 2026-09-21
authority: review-proposal
canon_effect: none
outline_effect: none
visual_effect: none-until-approved
source_brief: research/briefs/2026-09-21_visual_bible_skeleton_brief.md
depends_on:
  - AGENTS.md
  - meta/STATE.md
  - meta/DECISIONS.md
  - outline/volume1_story_engine.md
  - outline/volume1_phase_outline.md
  - outline/chapter_cards/volume1_ch001_003.md
  - outline/chapter_cards/volume1_ch004_010.md
  - research/reports/2026-09-21_visual_bible_and_illustration_continuity_study.md
  - reviews/2026-09-21_visual_bible_illustration_continuity_final_audit.md
---

# Visual Bible Skeleton Proposal｜视觉连续性骨架审议稿

> 本文件只建立视觉资产制度、字段与QA门槛。
>
> 本轮不生成正式角色脸，不生成正文插图，不修改 Canon，不修改 approved Outline / chapter cards。
>
> 核心原则只有一句：
>
> **先有已批准文字事实，再让视觉资产服从它；AI随机图无权反向修改故事。**

---

# 0. 本轮边界与裁决

## 0.1 当前允许建立

本轮允许冻结为“视觉生产流程”的只有：

1. 视觉资产目录与职责；
2. 文字权威与视觉权威的从属关系；
3. reference 资产制度；
4. 文件版本与资产状态制度；
5. hard-gate QA；
6. 固定中转台、驿货行、合租屋的文字空间字段；
7. 全局视觉风格板字段；
8. 当前允许的 V0 探索范围；
9. 禁止视觉定稿范围；
10. 未来单次生成任务模板。

## 0.2 当前明确不做

- 不生成陆野最终公开母脸；
- 不生成合租旧友正式人脸；
- 不生成曹闻川正式母脸；
- 不把任何 V0 图当作故事事实；
- 不把木作从“当前首选实现”升级成生活锚点永久职业；
- 不锁死修籍、B机构、R封存件的最终美术；
- 不提前定稿余世、弃相、余缝、余灾、正式余器视觉；
- 不用视觉图补写章卡没有的制度；
- 不因AI画出“更好看”的空间而修改 A' 事故因果。

---

# 1. 视觉资产权威层级

正式权威关系：

> **manuscript > Canon > approved Outline > approved chapter cards > approved visual assets > visual exploration**

视觉层内部再分：

1. **Approved Reference Asset**
   - 已经作者批准；
   - 可用于后续视觉生成；
   - 仍低于全部已批准文字资产。

2. **Candidate Asset**
   - 已通过部分内部检查；
   - 等待作者选择 / 审核；
   - 不构成视觉事实。

3. **V0 Exploration**
   - 纯探索；
   - 可大幅推翻；
   - 不允许被后续AI当成“既定角色/场景”。

## 1.1 冲突处理

如果图与文字冲突：

> **图改。**

不能：
> 看到图更顺眼 -> 静默改正文 / 章卡 / Canon。

若视觉制作暴露了文字内部的真实矛盾，例如：
- A' 空间无论如何都无法成立；
- 某设备在两个已批准文本中方向互斥；

则视觉工程师只能：

1. 登记冲突；
2. 指出冲突来自哪些文字权威；
3. 停止把该资产升级为 Approved；
4. 由作者决定是否走 Outline / Canon Proposal。

视觉层不得自行 Retcon。

## 1.2 “视觉事实”不能越权

Approved Visual Asset 只能固定：

> **文字已允许、且作者明确批准用视觉表达的那部分外观。**

它不能新增：
- 人物年龄事实；
- 阶层制度；
- 全国建筑标准；
- 舍务技术原理；
- 角色伤痕；
- 余世真相；
- 后续剧情装备。

---

# 2. 目录架构

建议未来目录：

~~~text
visual/
  bible/
    README.md
    AUTHORITY.md
    STYLE.md
    CHARACTER_SCHEMA.md
    SCENE_SCHEMA.md
    PROP_SCHEMA.md
    REFERENCE_REGISTRY.md
    TIMELINE_VISUAL_STATE.md
    SPOILER_BOUNDARIES.md

  characters/
    luye/
      v0_explore/
      candidates/
      master/
      turnaround/
      expressions/
      outfits/
      states/
    qiaojiu/
    shixiaogeng/
    luohuai/
    tanghe/
    zhouzhao/
    caowenchuan/
    rental_friend/

  scenes/
    posthouse/
      v0_explore/
      approved/
      lighting/
    transfer_station/
      normal/
      accident_a_prime/
      qa/
    rental_home/
      v0_explore/
      approved/
      timeline_states/
    abandonment_service/
    city_activity_radius/

  props/
    cargo_tag_clip/
    ordinary_tools/
    transport_tools/
    cultivation_tools/
    abandonment_tools/
    credentials/

  illustrations/
    internal_qa/
    public_candidates/
    approved/
    rejected/

  qa/
    checklists/
    reports/
    conflict_log/
    rejected_examples/
~~~

## 2.1 visual/bible/

只能放：
- 规则；
- 字段模板；
- 权威关系；
- reference登记；
- 状态时间线；
- 风格约束。

不能放：
- 未批准角色事实；
- 具体剧情新设定。

批准：
> 作者批准后才能成为长期视觉流程权威。

版本升级：
- 字段新增但不改变规则：minor；
- 改变资产权威 / QA逻辑：major；
- 文字错漏：patch。

## 2.2 visual/characters/

只能放：
- 角色探索图；
- 作者筛选候选；
- turnaround；
- 表情；
- outfit；
- injury/state；
- approved master。

角色文件不能以“看起来合理”为由新增：
- 疤；
- 异色瞳；
- 特殊发色；
- 永久漏舍特效；
- 未批准法器。

批准：
> 人物母图必须作者明确确认。

## 2.3 visual/scenes/

只能放：
- 已批准文字空间的视觉实现；
- 内部空间 QA；
- 光源 / 材质候选；
- 场景状态版本。

场景图不是世界建筑法典。

例如：
> 固定中转台的凹入式舍台服务位只代表本事故场景已批准布局，
> 不自动升级成全国所有舍台统一建筑标准。

## 2.4 visual/props/

按“普通物 / 普通修炼工具 / 舍务工具 / 凭证”分开。

任何 prop 必须有：
- 来源文字；
- 尺寸级别；
- 使用者；
- 当前章节状态；
- 是否可公开；
- 是否只是临时视觉候选。

## 2.5 visual/illustrations/

分四层：

### internal_qa
作者 / 写作AI内部使用。

### public_candidates
视觉已基本合格，但尚未批准公开。

### approved
通过 hard-gate、作者批准且允许公开。

### rejected
保留典型错误：
- 脸漂；
- 空间错；
- 服装时代错；
- 提前剧透；
- 新增 Canon 特征。

Rejected 不代表废物，而是未来 QA 反例库。

## 2.6 visual/qa/

每一张进入 Candidate 或 Approved 的图都应留下 QA 记录。

至少记录：
- asset_id；
- reference_ids；
- text_authority_refs；
- hard-gate 结果；
- reviewer；
- 结论；
- 被拒原因；
- superseded_by。

---

# 3. “资产状态”与“版本号”分离

为避免 V0 / V1 与 v1.0 混乱，正式分成两个维度。

## 3.1 资产状态层级

### V0｜Explore
- 纯内部探索；
- 不构成视觉事实；
- 可同时存在多个互相矛盾方向；
- 不可作为公开图的唯一 reference。

### V1｜Approved Internal Reference
- 作者已批准为内部母 reference；
- 后续剧情图必须优先引用；
- 可以因未来文字冻结变化而走正式视觉版本升级。

### V2｜Approved Public Visual
- 已在封面 / 宣传 / 正文 / 官方设定物料公开；
- 主要锚点进入公开连续性债务；
- 修改必须有版本说明，不能静默换脸 / 换场景。

### V3｜Commercial Master
- 实体出版 / 授权 / 商业主视觉；
- 额外要求来源、版权、素材许可、模型许可记录。

当前阶段：

> **空间与风格最多准备 V0 -> V1 审核；角色脸保持 V0，暂不进入 V1。**

## 3.2 文件版本号

版本格式：

> vMAJOR.MINOR.PATCH

### MAJOR
改变已批准视觉锚点或空间拓扑，例如：
- 角色脸型显著变化；
- 发型轮廓改变；
- 中转台 O / S / F / P 关系改变；
- 合租屋共用空间位置逻辑改变。

需要：
> 作者重新批准。

### MINOR
不改核心锚点，只增加 / 调整：
- 材质；
- 非剧情关键小工具；
- 局部照明；
- 衣物小变化；
- 场景非拓扑细节。

仍需重新过 hard-gate。

### PATCH
不改变视觉内容的：
- 裁切；
- 导出；
- 压缩；
- 文件命名修正；
- 轻微瑕疵修复。

---

# 4. Reference ID 制度

Reference ID 必须稳定，文件名可以变。

推荐格式：

> 类型-主体-用途-编号

示例仅作为命名规则，不代表当前已有母图：

- CH-LY-FACE-001
- CH-LY-BODY-001
- CH-LY-OUTFIT-WORK-EARLY-001
- CH-LY-STATE-POSTACCIDENT-001
- SC-TRANSFER-NORMAL-001
- SC-TRANSFER-APRIME-001
- SC-POSTHOUSE-WORKFLOW-001
- SC-RENTALHOME-BASE-001
- PR-BRAKE-CONTROL-001
- PR-CARGO-TAG-CLIP-001
- ST-GLOBAL-MAIN-001

## 4.1 每个 reference 必须登记

在 REFERENCE_REGISTRY 中至少有：

- reference_id；
- subject；
- asset_status：V0 / V1 / V2 / V3；
- version；
- file_path；
- source_text_refs；
- approved_by；
- approved_at；
- allowed_use；
- forbidden_use；
- anchors；
- allowed_variation；
- forbidden_drift；
- supersedes；
- superseded_by；
- notes。

## 4.2 Reference Bundle

未来任何正式剧情图，不得只给一张“感觉像”的图。

输入必须是一个 Reference Bundle：

1. 角色 master reference；
2. body / height reference；
3. 当前 outfit；
4. 当前 injury/state；
5. scene reference；
6. prop references；
7. 当前章节文字权威；
8. 禁止剧透清单；
9. 禁止漂移字段。

如果必要 reference 尚未批准：

> **降级为 V0 探索，不得冒充正式剧情图。**

---

# 5. 角色 reference 生产流程

当前只定义流程，不生成正式角色脸。

正式流程：

> **文字视觉卡**
> -> **V0 6—10个明确差异化方向**
> -> **作者筛到2—3个**
> -> **针对2—3个做 turnaround**
> -> **表情 / 半身 / 全身 / 多人比例验证**
> -> **作者批准 master**
> -> **建立 reference bundle**
> -> **后续生成 / 编辑**
> -> **hard-gate QA**
> -> **进入 approved assets**

## 5.1 第一轮 V0 的目的

不是：
> 抽到最好看的脸。

而是比较明确设计方向，例如：
- 更精干 / 更朴实；
- 更成熟 / 更年轻；
- 眉眼更机灵 / 更沉稳；
- 脸型更窄 / 更方。

每个方向要有文字差异说明。

## 5.2 不得依赖

- seed；
- 角色名字；
- 同一 prompt；
- 同一个模型会话；
- “模型记得陆野”；
- 只上传一张低质量剧情截图当唯一母 reference。

## 5.3 人物视觉卡字段

未来每个角色至少记录：

### Identity
- 视觉年龄感；
- 身高；
- 肩宽；
- 体型；
- 头身比例；
- 脸型；
- 眉；
- 眼型；
- 鼻 / 嘴辨识点；
- 肤色 / 日晒；
- 发际线；
- 发型；
- 发长。

### Silhouette
- 常态轮廓；
- 工作姿态；
- 常用工具位置；
- 左 / 右手习惯；
- 2—3个不可漂移锚点。

### Outfit
- 永久身份轮廓；
- 当前日常层；
- 当前工作层；
- 任务装备；
- 鞋 / 靴；
- 可变项；
- 禁止漂移项。

### State
- 当前章；
- 境界；
- 伤势；
- 污渍；
- 包扎；
- 装备损坏；
- 新旧工具；
- 是否允许公开。

### Reference
- face_ref；
- body_ref；
- outfit_ref；
- state_ref；
- latest_approved_version。

---

# 6. Hard-Gate QA

视觉 QA 不采用“总分达到90就通过”作为主门槛。

任何 hard gate 失败：

> **直接退回。**

构图、光影、氛围再好也不能抵消。

---

## Gate A｜文字权威门

必须能回答：

1. 这张图依据哪一章 / 哪个 Canon / 哪个 approved Outline？
2. 图中每个剧情关键视觉事实是否有文字来源？
3. 有没有把 research 候选误当成 Canon？
4. 有没有把“当前首选”画成永久事实？

失败示例：
- 把木作直接定成合租旧友永久职业；
- 给陆野加 Canon 没有的伤疤；
- 把舍台画成全国统一型号并在说明中写成制度事实。

任一出现：
> Reject。

---

## Gate B｜角色身份门

适用于已有 Approved Reference 的角色。

检查：
- 脸型；
- 眉眼关系；
- 发际线；
- 关键发型轮廓；
- 年龄感；
- 身高；
- 肩宽；
- 头身比例。

明显像“另一个人”：
> Reject。

不得用“光影不同”掩盖脸漂。

---

## Gate C｜剧情时间门

检查：
- 当前章节；
- 境界；
- 服装层；
- injury / state；
- 工具损坏；
- 是否已经舍味；
- 是否已经资格冻结 / 复工；
- 是否出现尚未获得的装备。

例如：
- 第1章陆野出现事故后包扎；
- 第1章视觉暗示永久失味；
- 第4章直接画出外界余痕来源；
- 第10章把陆野画成正式押手制服。

任一出现：
> Reject。

---

## Gate D｜场景空间 / 物理门

任何剧情空间必须服从批准文本。

### 固定中转台专项硬门

以下任一失败，A'场景图直接退回：

1. F 正常轨线就能碰到 O；
2. 普通小偏移就会撞舍台；
3. S 核心比 O 更靠外，成为第一接触面；
4. W 被画在明显违规 / 无法解释的危险位置；
5. R 不在 F 右端独立加固格；
6. 事故需要第二个独立故障才能让 R 和 O 同时受损；
7. B 被画成由陆野念力直接承重；
8. 看不出 B 本身承担制动力 / 咬合 / 牵引载荷；
9. 安全线、人员撤离方向与救援通道互相打架；
10. 图必须扭曲距离或建筑才让“一次侧摆”成立。

正常状态必须先成立：

> 正常直行安全 -> 普通偏移仍安全 -> 只有导向轮脱槽后的异常大角度侧摆越界。

否则：
> Reject，不反改章卡。

---

## Gate E｜剧透 / 知识边界门

视觉会比文字更容易把暧昧变成结论。

必须检查：

- 是否画出了人物当前不知道的来源；
- 是否给异常味明确来源标签；
- 是否提前表现“弃相去了哪里”；
- 是否把余缝画成确定的余世通道；
- 是否提前展示正式余器；
- 是否定稿卷末复合余灾形态。

第一卷前期尤其禁止：

> 用视觉特效告诉读者“答案是什么”。

失败：
> Reject 或只允许内部 V0，不得公开。

---

## Gate F｜Canon 新增门

禁止为了让画面有辨识度新增：

- 异色瞳；
- 灵纹；
- 永久发光伤痕；
- 神秘印记；
- 特殊发色；
- 额外武器；
- 组织徽章；
- 舍务宗教符号；
- UI；
- 系统面板。

没有文字批准：
> Reject。

---

## Gate G｜左右手 / 工具门

检查：
- 左右手；
- 腰间工具位置；
- 绳扣方向；
- 伤势左右；
- 工作台器具位置；
- prop 尺寸；
- 同一工具是否无故变结构。

若错误会改变剧情动作或空间因果：
> Reject。

---

## Gate H｜公开用途门

即使图本身正确，也要问：

> 这张图是否适合现在公开？

例如：
- A'事故平面图：内部 QA 很有价值，但开篇前公开会剧透；
- 合租屋平面：内部可用，正文通常无必要；
- V0脸：不得包装成官方角色图。

“内部正确”不等于“公开正确”。

---

# 7. 软评

只有通过全部 hard gates 后，才评：

- 构图；
- 光；
- 材质；
- 氛围；
- 动作可读性；
- 角色表演；
- 完成度；
- 平台适配。

软评只决定：
- 哪张更好；
- 是否值得修；
- 是否适合宣传。

软评不能救 hard-gate 失败图。

---

# 8. 第一阶段内部空间资产字段

本节分三种标记：

> **[TEXT-LOCKED]** 已由高层文字批准，视觉只能服从。  
> **[VISUAL-FIELD]** 需要视觉设计，但本文件只定义字段，不锁答案。  
> **[OPEN]** 当前不应定稿。

---

# 8A. 固定中转台｜Transfer Station

这是第一阶段最高优先级内部空间资产。

## 8A.1 资产目标

必须最终拥有至少三类内部 reference：

1. **NORMAL PLAN**
   - 正常俯视平面；
2. **HUMAN-EYE NORMAL**
   - 人高视角正常作业；
3. **A' ACCIDENT OVERLAY**
   - 同一空间上的事故侧摆覆盖图。

事故图不能独立另画成“另一个片场”。

## 8A.2 空间字段

### 正常货路
- [TEXT-LOCKED] F 为长型重载转运架；
- [TEXT-LOCKED] 正常沿东西方向进入固定导向位；
- [TEXT-LOCKED] 正常直行碰不到 O；
- [TEXT-LOCKED] 普通小偏移仍碰不到 O；
- [VISUAL-FIELD] 轨线宽度；
- [VISUAL-FIELD] 地面导向标识；
- [VISUAL-FIELD] 与人员安全线的视觉分隔方式。

### F｜转运架
- [TEXT-LOCKED] 长型重载转运单元；
- [TEXT-LOCKED] 机械结构承担主要载荷；
- [VISUAL-FIELD] 轮组数量；
- [VISUAL-FIELD] 材质；
- [VISUAL-FIELD] 常规固定点；
- [VISUAL-FIELD] 空架 / 载货状态差异；
- [OPEN] 正式世界内名称。

### 导向结构 P
- [TEXT-LOCKED] 左侧存在固定导向柱 / 护柱；
- [TEXT-LOCKED] W 正常工作位在左侧导向位；
- [VISUAL-FIELD] 柱体防撞结构；
- [VISUAL-FIELD] 人员站位标识；
- [VISUAL-FIELD] 导向轮与轨线如何在画面中让非工程读者看懂。

### 凹入式舍台服务位
- [TEXT-LOCKED] 位于正常货路外；
- [TEXT-LOCKED] 凹入式 / 半封闭；
- [TEXT-LOCKED] 正常轨线与普通偏移都不能碰到；
- [VISUAL-FIELD] 凹入深度；
- [VISUAL-FIELD] 入口防护层；
- [VISUAL-FIELD] 工具存放；
- [VISUAL-FIELD] 操作人员站位；
- [OPEN] 外观风格正式定稿。

### O｜封位外环
- [TEXT-LOCKED] 位于服务龛入口外沿；
- [TEXT-LOCKED] A' 中先受损；
- [VISUAL-FIELD] 是环、框、复合边界还是其它可维护构件的具体美术；
- [VISUAL-FIELD] 正常工作状态；
- [VISUAL-FIELD] 损坏状态；
- [OPEN] 材质 / 阵纹细节。

### S｜舍台核心
- [TEXT-LOCKED] 比 O 进一步后缩；
- [TEXT-LOCKED] A' 中未被直接撞毁；
- [TEXT-LOCKED] 事故后仍保留执行既有舍契的可能；
- [VISUAL-FIELD] 操作面；
- [VISUAL-FIELD] 维护区；
- [VISUAL-FIELD] 正常防护；
- [OPEN] 核心具体结构与技术原理视觉。

### R｜低风险封存退件格
- [TEXT-LOCKED] 属于同一正规返运批次；
- [TEXT-LOCKED] 已验低风险；
- [TEXT-LOCKED] 位于 F 右端独立加固格；
- [TEXT-LOCKED] A' 同一次右端挤压使外封壳受损；
- [VISUAL-FIELD] 独立加固方式；
- [VISUAL-FIELD] 普通标签 / 封条逻辑；
- [OPEN] R 正式外观；
- [OPEN] 泄漏视觉。

### B｜辅助制动 / 牵引结构
- [TEXT-LOCKED] 现场既有机械；
- [TEXT-LOCKED] 负责制动力 / 机械咬合 / 牵引载荷；
- [TEXT-LOCKED] 陆野只远距持续操作控制点；
- [TEXT-LOCKED] 炼气可短时作用，筑基可远距持续稳定；
- [VISUAL-FIELD] 控制点结构；
- [VISUAL-FIELD] 机械传力路径；
- [VISUAL-FIELD] 如何直观看出“设备吃力，陆野做控制”；
- [OPEN] B 正式术语。

### W｜事故前工作位
- [TEXT-LOCKED] 左侧导向位；
- [TEXT-LOCKED] 是正常合法工作位，不靠违规站位制造事故；
- [VISUAL-FIELD] 站位标识；
- [VISUAL-FIELD] 正常工具；
- [VISUAL-FIELD] 与 P / F 的安全余量。

### 安全线 / 撤离区
- [TEXT-LOCKED] 南侧存在人员安全线 / 撤离区；
- [VISUAL-FIELD] 地面视觉语言；
- [VISUAL-FIELD] 正常人员分布；
- [VISUAL-FIELD] 事故后人员如何退到安全线外。

### 专业救援方向
- [TEXT-LOCKED] 西北存在专业救援服务通道；
- [VISUAL-FIELD] 通道宽度；
- [VISUAL-FIELD] 与货路是否交叉；
- [VISUAL-FIELD] 远景识别方式。

### 光源
- [VISUAL-FIELD] 夜班主照明位置；
- [VISUAL-FIELD] 服务龛工作光；
- [VISUAL-FIELD] 应急照明；
- [VISUAL-FIELD] 正常 / 事故状态是否改变；
- [OPEN] 光色与灯具最终样式。

## 8A.3 正常版 / 事故版状态

### NORMAL-v1
必须先验证：
- 正常工作合理；
- 安全设施不妨碍周转；
- W 站位合理；
- R 运输方式合理；
- B 普通状态合理。

### APRIME-v1
只能在 NORMAL 同一底图上改变：
- 一侧导向轮脱槽；
- F 顺时针异常大角度侧摆；
- 左端向 P 压 W；
- 右端 R/O 同一次挤压接触。

不得为了事故：
- 搬动建筑；
- 临时添加第二故障；
- 把 O 拉出墙外；
- 把 W 移到危险区；
- 让 S 突然前移。

---

# 8B. 驿货行｜Posthouse / Freight House

本资产目标不是先画“仙侠大货栈”，而是建立：

> **长期工作动线、普通器物、材质与阶层感。**

## 8B.1 文字事实边界

### [TEXT-LOCKED]
- 陆野为驿货行短途杂役 / 押货杂役；
- 第一章存在白班收尾 / 夜班交接前分货区；
- 乔九在真实排班中拆补班次；
- 有普通杂役、候选辅助位、正式押手等职业层级差异；
- 有普通货签夹、固定点、普通工具、转运架等工作物；
- 有夜班前廉价热汤这一生活动作；
- 乔九需要降低空转与后续周转拖延；
- 前40章绝大多数货物必须是普通货。

### [OPEN]
- 货行正式名称；
- 建筑规模；
- 城市地域建筑样式；
- 精确入口数量；
- 是否与固定中转台同一院落 / 同一站点的永久空间关系；
- 修籍凭证最终载体美术。

## 8B.2 必须建立的字段

### 货流入口 / 出口
- 普通货从哪里进；
- 普通货去哪里；
- 空架如何回流；
- 人流是否与货流冲突；
- 临时待分区在哪里。

### 工作区
至少区分视觉功能：
- 分货；
- 绑扎 / 固定；
- 工具取放；
- 临时清点；
- 排班 / 交接；
- 普通低风险设备回位。

不要求现在锁建筑平面。

### 夜班汤 / 短休位置
只锁功能字段：
- 是否离主货路有安全距离；
- 是否能让第一章咸汤自然出现；
- 是否属于廉价工人日常，而不是酒楼场景。

不锁：
- 汤铺还是货行内部灶；
- 汤的正式品种；
- 具体摆设。

### 工具系统
字段：
- 廉价耗材；
- 重复使用工具；
- 可维修普通件；
- 废料筐；
- 个人小工具；
- 公用工具；
- 工具归位方式。

必须支持：
> “坏货签夹里簧针仍可安全二用，真坏夹体照样扔。”

### 光源
至少记录：
- 白班；
- 交接黄昏 / 夜班；
- 分货区；
- 工具区；
- 汤 / 休息点；
- 户外货路。

### 材质
风格候选方向：
- 长期使用；
- 反复修补；
- 功能优先；
- 普通木 / 石 / 金属 / 织物 / 低阶炼器材料混合；
- 不把所有表面做成琉璃、玉石、仙宫材质。

注意：
> 这是视觉方向，不是 Canon 材料清单。

### 阶层感
通过：
- 工位；
- 工具状态；
- 衣服层次；
- 谁拿什么设备；
- 谁需要等排班；
表现。

禁止只靠：
- 穷人永远脏；
- 管事永远华服。

### 低阶灵力如何进入劳动
只允许视觉化已批准行动：
- 灵力灌注普通工具；
- 低阶法器；
- 炼气短时离体不足；
- 筑基稳定离体后能持续操作远端控制点。

禁止把货行画成：
> 全自动仙术物流中心。

---

# 8C. 合租屋｜Rental Home

合租屋的意义不是“温馨背景”。

它是第一卷长期观察：

> **味觉永久缺位怎样改变普通生活，以及两个人的边界怎样随工作 / 钱变化。**

## 8C.1 当前文字事实边界

### [TEXT-LOCKED]
生活锚点是：
- 高频；
- 非任务型；
- 规整；
- 重生活边界；
- 有独立手艺目标；
- 手艺学徒 / 小手艺接单者方向；
- 木作为当前实现首选但未永久冻结；
- 正在争取独立完成一件真正算自己手艺的小单；
- 正在攒基础工具。

第4章必须允许：
- 一整顿没味的饭；
- 共同伙食 / 调味成本重新协商；
- 调料 / 食材支出可从共同小账拆分；
- 旧零件 / 修补件 / 小工具占用共用空间；
- 旧友要求陆野清出一块工作位置。

### [OPEN]
- 姓名；
- 性别；
- 精确年龄；
- 正式手艺；
- 房间数量；
- 同屋各灶是否最终成立；
- 是否卷末搬走；
- 建筑朝向；
- 精确城市街区。

## 8C.2 必须建立的空间字段

### 共用吃饭位置
字段：
- 两人是否面对 / 错位坐；
- 调料放哪；
- 公共食材与个人食材怎么区分；
- 第4章后如何出现可见变化；
- 陆野失味后餐具 / 食物份量是否变化。

不得用：
> “陆野面前永远只有白粥”这种视觉夸张替代真实生活变化。

### 共用桌面 / 工作面
必须区分：
- 吃饭；
- 临时修补；
- 手艺小单；
- 工具摊开。

如果同一张桌承担多功能，要记录：
> 时间切换与清桌规则。

视觉上要能支持：
> “能留，不等于能无限占别人的空间。”

### 陆野旧零件 / 工具区
字段：
- 收纳方式；
- 数量上限感；
- 哪些是可用备件；
- 哪些只是待处理；
- 是否侵占公共空间。

“惜物”不能画成垃圾山。

### 生活锚点手艺区
字段：
- 需要平整工作面；
- 基础工具；
- 半成品暂存；
- 接单材料；
- 不为陆野服务的独立进度。

若正式手艺未冻结：
> 用中性“手艺工作面”做 V0 空间，不把木工器具画成不可替代事实。

### 灶
字段：
- 共用还是分时；
- 基础锅具；
- 调味区；
- 热水；
- 廉价日常烹饪能力。

不需要画成精致古风厨房。

### 收纳
必须能长期追踪：
- 共用物；
- 陆野物；
- 旧友物；
- 工具；
- 食材；
- 调味；
- 房租 / 小账相关票据或记录位置（若未来文字需要）。

### 光
至少准备：
- 白天自然光；
- 夜间普通照明；
- 饭桌；
- 手艺工作面。

正常照明先稳定，未来异常才有对比。

## 8C.3 时间状态版本

建议至少记录：

### HOME-BASE
事故前 / 尚未因失味重排生活边界的正常版。

### HOME-CH04
味觉永久损失第一次进入整顿饭；
共同伙食与调味支出开始拆分；
共用空间发生第一次边界重谈。

### HOME-CH08
陆野重新挣到钱后；
不是大和解，只是现金重新流动后的生活回声；
生活锚点自己的小单继续推进。

这些是视觉状态版本，不是三套不同房子。

---

# 8D. 全局视觉风格板｜Global Style Board

本轮只定义字段与方向，不选最终图。

## 8D.1 主风格候选

研究与终审当前首选：

> **克制的半写实国风插画。**

但在作者批准实际 style board 前：

> 仍属于主候选，不是永久商业美术法典。

辅助体系：
- 黑白线稿：内部空间 / 器物 / 实体附录；
- 水墨概念：卷首 / 氛围宣传；
- 国漫：如未来短视频 / 动态漫需要，可另开视觉分支。

连续剧情图不建议频繁跨画风。

## 8D.2 Style Board 必须有的字段

### 世界正常态
- 正常人间环境先成立；
- 修仙设施是生活系统的一部分；
- 不每个角落仙气缭绕；
- 低阶修士劳动有重量。

### 材质
记录：
- 木；
- 石；
- 金属；
- 织物；
- 纸 / 册；
- 普通法器材质；
- 舍务设备材质；
- 修补痕迹；
- 使用痕迹。

不要求现在锁具体材料配方。

### “穷但不脏”
必须给正反例：
- 可旧；
- 可补；
- 可有磨损；
- 可重复利用；
- 但不长期污头垢面；
- 不用破衣烂衫表示阶层；
- 工作安全逻辑优先。

### 舍务正规而非邪教
正规舍台视觉必须强调：
- 可操作；
- 可维护；
- 有工具区；
- 有安全边界；
- 有防护；
- 有重复使用逻辑。

禁止：
- 血祭感；
- 黑红邪阵；
- 人骨；
- 宗教祭坛；
- 大量不可解释神秘符号。

### 修仙不满屏发光
境界差异优先体现：
- 动作距离；
- 控制持续性；
- 站位；
- 法器关系；
- 工作空间。

禁止：
> 升境 = 换发光颜色 / 全身光效升级。

### 角色差异
优先：
- 轮廓；
- 体型；
- 穿法；
- 工具位置；
- 动作习惯。

不优先：
- 彩色发色；
- 异色瞳；
- 夸张疤痕。

### 光照
至少设计字段：
- 白班；
- 夜班货场；
- 合租屋夜间；
- 舍台服务位；
- 应急照明；
- 后期余灾异常光（暂不定稿）。

原则：
> 正常光源先稳定，异常光才有意义。

### 色彩
本轮只建立：
- 常态主色群字段；
- 工作区色群字段；
- 舍务设施识别色字段；
- 警戒 / 应急字段；
- 角色服装色群字段；
- 异常视觉保留字段。

不在本 Proposal 直接锁具体色号。

---

# 9. 当前允许 V0 探索清单

Skeleton 审核通过后，第一批允许进入 V0 的顺序建议：

## Priority 1｜固定中转台
允许：
- 黑白平面；
- 正常货路；
- A' 事故 overlay；
- 人高视角；
- O / S / R / B / W 相对位置测试。

不允许：
- 公开成正文事故图；
- 用AI随机空间替换章卡几何。

## Priority 2｜驿货行材质 / 器物板
允许：
- 分货区材质；
- 绑扎工具；
- 普通转运器具；
- 废料筐；
- 坏货签夹比例；
- 夜班普通照明；
- 工人层服装轮廓探索。

不允许：
- 先画整座“仙侠物流城”并倒逼世界观。

## Priority 3｜合租屋平面
允许：
- 2—4种功能平面；
- 共用桌 / 工作面关系；
- 灶与收纳；
- 陆野工具区；
- 中性手艺工作区。

不允许：
- 用具体木工器具把职业永久锁死；
- 生成生活锚点正式母脸。

## Priority 4｜全局风格板
允许：
- 半写实国风方向差异；
- 材质；
- 劳动感；
- 正规舍务设施；
- 正常光源；
- 穷但不脏正反例。

## Priority 5｜人物 V0
只有在上述空间 / 风格方向先通过一次作者审核后，再开始：
- 陆野 6—10个差异化方向；
- 乔九轮廓；
- 石小庚轮廓。

本轮：
> **不实际生成。**

---

# 10. 当前禁止视觉定稿清单

以下内容即使探索图很好看，也不得进入 V1 / V2：

1. 余世真实形态；
2. 弃相终极形态；
3. 漏舍永久可见特效；
4. 第一件正式余器；
5. 卷末复合余灾最终形态；
6. 合租旧友正式人脸；
7. 曹闻川正式母脸；
8. 陆野最终公开母脸；
9. 余缝等于某种已确定视觉通道；
10. 味觉舍备的全国统一凭证样式；
11. 全国统一舍台建筑标准；
12. B 的最终术语 / 工业标准；
13. R 的最终标准封存箱型号；
14. 城市整体建筑美术法典；
15. 未批准组织徽章 / 制服系统。

---

# 11. 插图策略

正式建议继续采用：

> **正文低密度功能图 + 内部空间图 + 宣传图重点投入。**

## 11.1 内部 QA 图｜优先级最高

适合：
- 固定中转台；
- A'事故空间；
- 驿货行动线；
- 合租屋平面；
- 工具比例；
- 多人身高比例；
- 以后复杂法器结构。

作用：
> 提升文字连续性，不要求公开。

## 11.2 正文可选图｜低密度

只有同时满足才可进入正文：

1. 没图也能完全理解；
2. 图增强而不替代文字；
3. 不剧透；
4. reference 已稳定；
5. hard-gate 全过；
6. 手机一眼能读；
7. 不需要放大小字。

不机械规定：
- 每章1图；
- 每5章1图；
- 每10章1图。

第一卷：
> **0张完全可以。**

## 11.3 宣传图｜重点投入

更适合：
- 陆野真实工作场；
- 驿货行夜班；
- 核心群像；
- 卷级氛围；
- 卷末已公开后再做关键场景。

宣传图也不能跳过：
> reference + hard-gate。

## 11.4 不建议图

- 角色第一次出场立即立绘；
- 第1—3章提前公开 A' 精确事故图；
- “异常味”的明确视觉来源图；
- 余世定稿；
- 漏舍发光特效；
- 为每章凑画面；
- 只因AI能生成就插。

---

# 12. 单次未来生成任务模板

未来任何一次正式绘图任务，先填写以下模板。

~~~text
VISUAL TASK ID:
PURPOSE:
  [internal_qa / v0_explore / public_candidate / approved-public revision]

PUBLICATION LEVEL:
  [internal only / may publish after approval / public asset revision]

TEXT AUTHORITY:
  - manuscript:
  - canon:
  - approved outline:
  - approved chapter card:
  - decisions:

TIMEPOINT:
  - volume:
  - chapter:
  - before/after event:
  - character knowledge boundary:

CHARACTERS:
  - name:
  - master_ref:
  - body_ref:
  - outfit_ref:
  - state_ref:
  - required anchors:
  - allowed variation:
  - forbidden drift:

SCENE:
  - scene_ref:
  - scene_version:
  - normal/accident/state:
  - fixed geometry:
  - allowed visual exploration:
  - forbidden spatial changes:

PROPS:
  - prop_ref:
  - scale:
  - hand/side:
  - current condition:

LIGHTING:
  - lighting_ref:
  - time:
  - normal/emergency:

ALLOWED CANON ON SCREEN:
  -

FORBIDDEN / SPOILER:
  -

COMPOSITION INTENT:
  -

STYLE REF:
  -

OUTPUT:
  - aspect ratio:
  - intended size:
  - line/color:
  - text in image allowed?:

HARD-GATE CHECKS REQUIRED:
  [A/B/C/D/E/F/G/H]

REVIEWER:
APPROVAL REQUIRED FROM:

STORY CHANGE AUTHORITY:
  NONE.
  If image conflicts with approved text, reject/repair image.
  Do not alter story from image output.
~~~

## 12.1 单次任务停止条件

若出现以下任一情况，停止正式生成并退回：

- 必要 reference 缺失；
- 角色仍只处 V0，却要求“官方角色图”；
- 场景空间未通过文字硬门；
- 时间点不清；
- 当前章剧透边界不清；
- 任务要求模型“自由设计”剧情关键设备；
- 任务要求根据生成结果修改章卡。

---

# 13. 视觉时间线状态规则

Visual Bible 不能只维护“长什么样”，还要维护：

> **什么时候长成当前这样。**

TIMELINE_VISUAL_STATE 至少记录：

- chapter_start；
- chapter_end；
- character；
- cultivation_stage；
- outfit；
- injury；
- dirt / wetness；
- prop changes；
- location changes；
- public spoiler level；
- active references。

例如第一卷前10章，至少要区分：

### 陆野 CH01
- 炼气；
- 味觉正常；
- 无事故后状态；
- 高危候选尚未冻结。

### 陆野 CH03-post
- 筑基；
- 永久失味；
- 漏舍成立；
- 不允许出现异常味可视化；
- 高危候选资格被冻结。

### 陆野 CH04-10
- 筑基新手逐渐适应；
- 高危限制仍在；
- 服装 / 工作状态不得误画成正式押手；
- 第5章唯一异常味多数情况下不视觉化；
- 第10章只有连续受限排班，不是正式资格恢复。

---

# 14. 三处场景的最低视觉交付标准

Skeleton 通过后，真正开始空间资产时，不要求先做精美插画。

## 14.1 固定中转台
最低：
- 一张可读俯视平面；
- 一张 A' 侧摆 overlay；
- 一张人高视角；
- 一个 hard-gate QA 记录。

精美度次于几何正确。

## 14.2 驿货行
最低：
- 一个简化工作动线；
- 一张材质 / 器物板；
- 一张夜班照明候选；
- 不必先做整座建筑。

## 14.3 合租屋
最低：
- 2—4个功能平面候选；
- 标出共同 / 个人 / 手艺工作面；
- 标出灶、饭桌、工具 / 旧零件收纳；
- 标出 CH04 后生活边界变化点。

---

# 15. 自我红队

## 15.1 Visual Bible 会不会成为第二套 Canon？

风险存在。

防线：

> 每个视觉资产必须保存 source_text_refs，并且权威永远低于批准文字。

## 15.2 “Approved Reference”会不会反过来锁死没写过的东西？

会。

所以作者批准 reference 时必须区分：

> 哪些锚点真的批准，哪些只是画师补全。

图里为了完整构图被迫出现的非关键细节，不自动变 Canon。

## 15.3 固定中转台画得太漂亮，能不能改章卡配合？

不能。

图服务 A'，不是 A' 服务图。

## 15.4 可以先让AI自由画几个货场找灵感吗？

可以作为 V0。

但：
- 不得进入 approved；
- 不得作为后续唯一 reference；
- 不得用它修改已批准空间因果。

## 15.5 合租屋能不能先定成木工房？

不能。

“木作”当前只是首选实现。
V0 可以测试木作版，但空间骨架要允许未来替换成别的手艺而不推翻整屋功能。

## 15.6 为什么不现在锁陆野脸？

当前正文马上要启动，空间 / 工具 / 工作逻辑对正文帮助更直接。

而具体五官、发型、城市地域视觉基调尚未冻结。

过早锁脸会制造不必要的视觉债。

## 15.7 异常味要不要做统一特效？

当前不建议。

它本质是陆野的主观味觉感知，且早期信息边界要求极严。

多数时候：
> 不画，比画一团彩色雾更准确。

## 15.8 舍台为什么不能做得神秘漂亮一点？

可以有审美，但首先必须是：

> 成熟、安全、可维护的技术设施。

若画面第一感受是祭坛 / 邪教：
> 视觉已经改写了制度立场。

## 15.9 “穷但不脏”会不会削弱底层感？

不会。

底层感可以由：
- 衣物使用年限；
- 修补；
- 工具复用；
- 空间紧；
- 材质普通；
- 工钱与排班；
表达。

不需要靠不卫生。

## 15.10 hard-gate 会不会让图太死？

hard-gate只锁：
- 身份；
- 时间；
- 空间；
- 剧透；
- Canon。

构图、光、动作、镜头、气氛仍有大量自由。

---

# 16. 建议审核时只拍板的内容

本 Proposal 建议总编 / 作者本轮只决定：

1. 是否采用本文件的视觉资产权威层级；
2. 是否采用“资产状态 / 文件版本分离”；
3. 是否采用 reference registry + reference bundle；
4. 是否采用 A—H hard-gate；
5. 是否批准固定中转台专项几何 hard-gate；
6. 是否批准驿货行 / 合租屋 / 风格板字段；
7. 是否同意 Skeleton 通过后优先做：
   > 固定中转台 -> 驿货行材质器物 -> 合租屋 -> 全局风格板；
8. 是否继续保持人物正式母脸在后。

不需要本轮拍板：
- 正式颜色；
- 正式脸；
- 正式城建风格；
- B术语；
- R外观；
- 舍台最终工业设计；
- 合租旧友性别 / 姓名 / 正式手艺。

---

# 17. 最终建议

本轮建议正式冻结的不是“图长什么样”，而是：

> **以后图必须怎样被批准、怎样被引用、怎样被退回。**

第一批最有价值的视觉资产也不是角色海报，而是：

1. **固定中转台正常 / A' 双状态空间 reference；**
2. **驿货行材质、器物与工作动线；**
3. **合租屋功能平面与生活边界；**
4. **全局视觉风格板。**

等这四项稳定以后，再进入人物 V0。

这样才能保证未来的 AI 插图：

> **不是每次重新抽世界，而是在同一个世界里继续拍下一张。**

> 本文件到此停止。
>
> 未经审核与作者确认，不创建 visual/ 正式资产，不生成正式角色脸，不生成正文插图，不修改 Canon / approved Outline / chapter cards。
