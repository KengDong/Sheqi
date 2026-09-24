# D-0084｜R7 P1 Writer Boundary Selfcheck

date: 2026-09-24
role: p1_prototype_writer
candidate: R7 Dead People Still Work

- 新增规则：否。
- 新增核心人物：否。
- 写了 Ch2：否。
- 读取其它候选：否。
- 越界读取：是。

越界说明：
- 为定位 Git 仓库与确认提交能力，读取了 Git 提交元数据；
- 该提交元数据意外包含 `meta/ACTIVE_WORKSTREAMS.md` 的局部 diff；
- 这是 CURRENT HARD INPUT BOUNDARY 之外的内容暴露；
- 未据此修改 R7 设定、情节或正文方向。

正文只基于允许输入：
1. `research/briefs/2026-09-24_d0084_p1_isolated_prototype_brief.md`
2. `experiments/first_principles_forge/prototypes/p1/packs/R7_dead_people_work_writer_pack.md`
