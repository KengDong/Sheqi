# REBOOT-V4｜11套包装匿名混排书架 Forge Brief

date: 2026-09-26
branch: `reboot-v4-fanqie-market-entry`
role: `reboot_v4_anonymous_shelf_forge`

# PURPOSE

把最终通过包装质检的 11 套番茄包装制作成两份 clean-room Reader 书架。

只做匿名化与顺序变化。

不得改写任何：
- 书名；
- 一句话钩子；
- 简介。

# HARD INPUT BOUNDARY

只允许读取：

1. `experiments/reboot_v4/packages/2026-09-26_pool01_package_set.md`
2. `experiments/reboot_v4/packages/2026-09-26_pool02_package_set.md`
3. `experiments/reboot_v4/packages/2026-09-26_pool03_package_set.md`
4. `experiments/reboot_v4/packages/revisions/2026-09-26_package_targeted_revision.md`
5. `reviews/2026-09-26_reboot_v4_package_targeted_revision_review.md`

不得读取：
- Concept 文件；
- 市场研究；
- 旧 Sheqi；
- Reader 结果；
- 正文；
- 联网。

# FINAL PACKAGE SOURCE RULE

最终 11 套中：

- Pool 1 方案一/二/三：取原 package set；
- Pool 1 方案四：必须用 targeted revision；
- Pool 2 方案一：必须用 targeted revision；
- Pool 2 方案二/三/四：取原 package set；
- Pool 3 方案一/二/三：取原 package set；
- Pool 3 方案四：不存在于书架。

# READER-VISIBLE CONTENT

每张书卡只允许：

1. 匿名编号，例如 `书架01`
2. 书名
3. 一句话钩子
4. 简介

严禁放：
- Pool；
- 方案编号；
- 原 Concept 名；
- “民俗池 / 医武池 / 诡异池”等研发标签；
- 包装自检；
- 前三章承诺；
- PASS / REVISE；
- 作者状态；
- 市场证据；
- 为什么这样设计。

# TWO SHELVES

Create two shelves containing the exact same 11 books but in different orders:

A:
> `experiments/reboot_v4/shelf/2026-09-26_anonymous_mixed_shelf_a.md`

B:
> `experiments/reboot_v4/shelf/2026-09-26_anonymous_mixed_shelf_b.md`

要求：
- 顺序必须明显不同；
- 不要让同一题材全部连在一起；
- A/B 中匿名编号只代表该书架位置，不得可逆推同一本书；
- Reader A 只看 A；
- Reader B 只看 B。

# PRIVATE MAPPING

Create:
> `experiments/reboot_v4/shelf/private/2026-09-26_anonymous_shelf_mapping.md`

Mapping must record:
- Shelf A position → actual Pool / 方案
- Shelf B position → actual Pool / 方案
- exact source file
- whether package came from original or targeted revision

Reader must never be allowed to read this file.

# SELF CHECK

Verify:
- 11 books in A;
- 11 books in B;
- same 11 titles exactly once in each;
- two revised packages replace old versions;
- Pool 3 concept04 absent;
- no text modified;
- no研发标签 leaked to visible shelves.

Complete CURRENT / history / Git commit, then STOP.
