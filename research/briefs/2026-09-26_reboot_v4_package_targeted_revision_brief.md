# REBOOT-V4｜两套番茄包装定向返修 Brief

date: 2026-09-26
branch: `reboot-v4-fanqie-market-entry`
role: `reboot_v4_package_targeted_revision`

# PURPOSE

只修两套包装文案，不改 Concept：

1. Pool 1｜方案四｜《出事以后，他们先来问我》
2. Pool 2｜方案一｜《下山神医回城》

包装质检结论来源：
> `reviews/2026-09-26_reboot_v4_package_editor_review.md`

# HARD INPUT BOUNDARY

只允许读取：

1. 本 brief；
2. `reviews/2026-09-26_reboot_v4_package_editor_review.md`
3. `experiments/reboot_v4/packages/2026-09-26_pool01_package_set.md`
4. `experiments/reboot_v4/packages/2026-09-26_pool02_package_set.md`
5. `experiments/reboot_v4/concepts/revisions/2026-09-26_pool01_concept04_revision.md`
6. `experiments/reboot_v4/concepts/2026-09-26_pool02_yiwu_concept_set.md`

不得读取：
- 其它 Pool 包装；
- 旧 Sheqi 候选；
- Reader 结果；
- 正文；
- 联网。

# REVISION A｜Pool 1 方案四

原测试书名：
> 《最不信玄学的人，后来也会先问我一句》

原钩子：
> 我只说“这一步先别动”，现实就逼最不信的人改了行动。

必须解决：

1. 标题 / 钩子至少有一个更直接表现：
   > 主角能看懂别人没看懂的因果 / 顺序。
2. 不能让陌生读者长期误判成：
   > 公共怪案 + 调查人员持续来找主角。
3. 简介明显过长，必须压缩到与其它包装大致同级的信息密度。
4. 必须保住：
   - 主角先排普通原因；
   - 第一次现实验证；
   - 最不信的人改变真实行动；
   - 长期主发动机在旧家庭、熟人社会、家庭 / 师门、外公旧人情和过去后果；
   - 主角越被信任越不敢乱说。
5. 不能重新把固定调查人员包装成主卖点。

# REVISION B｜Pool 2 方案一

原测试书名：
> 《神医下山：回城先救我妈》

原钩子：
> 他们还叫我没出息的儿子，后来全城看病先问我在不在。

只需解决：

1. “全城看病先问我在不在”过度绝对。
2. 保留：
   > 没出息的儿子 → 真出事只有他能解决 → 名字越来越有分量。
3. 不新增豪门、机构、顶级身份、师门后台。
4. 不需要加长简介。
5. 如果原标题仍然忠实，可以保留；不要为了返修强行换成更夸张标题。

# OUTPUT

Create:
> `experiments/reboot_v4/packages/revisions/2026-09-26_package_targeted_revision.md`

只输出两套修订后的正式包装，每套：

- 最终测试书名；
- 30字内一句话钩子；
- 测试简介；
- 前三章承诺；
- 包装自检；
- 与质检问题逐条对应的修正说明。

# HARD

- 只改包装；
- 不改 Concept；
- 不生成第三套；
- 不给备选标题；
- 不排行；
- 不写正文；
- 不跨池比较；
- 不联网；
- 不复活旧候选。

完成 CURRENT / history / Git提交后 STOP。
