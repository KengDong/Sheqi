# ACTIVE WORKSTREAMS｜Sheqi 当前窗口与任务总表

- window_reuse_plan: `meta/WINDOW_REUSE_PLAN.md`
- hit_fiction_workplan: `meta/HIT_FICTION_WORKPLAN.md`

> 本文件只记录当前工作流状态，不创造Canon / Outline权威。
> 总评审每次阶段切换必须同步。

## editor_in_chief
- status: ACTIVE
- current_task: D-0067 Asymmetric Finalist Development Orchestration
- gate: C01 ARC DESIGN DONE + C12 LIFE-FIRST ARC ACTIVE
- current: `handoffs/editor_in_chief/CURRENT.md`

## mid_continuity
- status: PAUSED
- current_task: DONE｜Authority Rewrite + Targeted PATCH
- current: `handoffs/mid_continuity/CURRENT.md`
- final_review: `reviews/2026-09-22_authority_rewrite_targeted_patch_final_review.md`
- waiting_for: none

## opening_writer
- status: RETIRED / CONTEXT LIMIT REACHED
- role: world_prototype / Finalist Continuation Writer
- completed_task: Finalist Opening Arc Stress Test｜DONE
- current: `handoffs/opening_writer/CURRENT.md`
- output:
  - B Ch2—Ch3
  - D Ch2—Ch3
  - Writer Selfcheck
- hard_rule: no future tasks to this window

## benchmark_deepread
- status: ACTIVE
- role: c12_book_architect / Life-First Arc Architect
- execution_window: 复用原 Benchmark Deep Read / C12 Book Architect窗口
- current_task: C12 Ch11—15 Life-First De-Curricularization Arc
- current: `handoffs/benchmark_deepread/CURRENT.md`
- output:
  - `research/design/2026-09-23_c12_longform_canopy_architecture.md`
  - `reviews/2026-09-23_c12_longform_canopy_selfcheck.md`
- verdict: PASS TO DUAL CANOPY TOTAL-EDITOR AUDIT
- deliver_to: editor_in_chief

## market_scout
- status: DONE / PAUSED
- role: c01_book_architect / Reader-Desire Arc Architect
- execution_window: 复用原 Market Scout / C01 Book Architect窗口
- current_task: C01 Ch11—30 Reader-Desire Arc Development｜DONE
- current: `handoffs/market_scout/CURRENT.md`
- brief: `research/briefs/2026-09-23_c01_ch011_030_reader_desire_arc_brief.md`
- output:
  - `research/design/2026-09-23_c01_ch011_030_reader_desire_arcs.md`
  - `reviews/2026-09-23_c01_ch011_030_arc_selfcheck.md`
- verdict: PASS / READY FOR TOTAL-EDITOR ARC AUDIT
- deliver_to: editor_in_chief

## hit_concept_scout
- status: DONE
- execution_window: 新开独立窗口
- current_task: Hit Concept Foundry｜DONE
- current: `handoffs/hit_concept_scout/CURRENT.md`
- output: `research/design/2026-09-22_hit_concept_foundry.md`
- top5:
  - C01《明天已经卖掉》
  - C03《人格股份有限公司》
  - C02《热搜成真以后》
  - C12《替有钱人渡劫》
  - C08《职业遗产》
- deliver_to: editor_in_chief

## world_reframe
- status: PAUSED / SHEQI-FAMILY HOLD
- execution_window: 复用“中段+衔接”窗口
- current_task: HOLD｜C1R / C2 / C8R仅作为Sheqi-family候选
- current: `handoffs/world_reframe/CURRENT.md`
- output:
  - `research/design/2026-09-22_sheqi_world_reframe_options.md` v1.1
  - `research/design/2026-09-22_world_reframe_top3_combustion_cards.md`
  - `reviews/2026-09-22_world_reframe_top3_patch_selfcheck.md`
- deliver_to: editor_in_chief
- waiting_for: Top-3 PATCH Re-review

## world_prototype
- status: DONE / PAUSED
- execution_window: 复用“开头 / 主作者”窗口
- current_task: Book-Level Prototype Duel
- current: `handoffs/world_prototype/CURRENT.md`
- brief: `research/briefs/2026-09-22_book_level_prototype_duel_brief.md`
- candidates:
  - A = C10《死人也要履约》
  - B = C01《明天已经卖掉》
  - C = C08《职业遗产》
  - D = C12《替有钱人渡劫》
- deliver_to: fresh_book_blind_reader / editor_in_chief

## visual
- status: PAUSED
- next_task: only update internal visual assets if new approved opening invalidates current V0 references
- current: `handoffs/visual/CURRENT.md`

## fresh_book_blind_reader
- status: DONE / PAUSED
- execution_window: 必须新开全新GPT窗口
- current_task: Fresh Book Prototype Blind Read
- brief: `research/briefs/2026-09-22_book_prototype_fresh_blind_read_brief.md`
- first_pass_output: `reviews/2026-09-22_book_prototype_fresh_blind_read.md`
- next_brief: `research/briefs/2026-09-22_finalist_returning_reader_continuation_brief.md`
- input_ready: finalist B/D Ch2—Ch3 complete
- deliver_to: editor_in_chief

## finalist_fresh_reader
- status: DONE / PAUSED
- execution_window: 必须新开第二个全新GPT窗口
- current_task: Finalist 3-Chapter Fresh Shelf Test
- brief: `research/briefs/2026-09-22_finalist_three_chapter_fresh_shelf_test_brief.md`
- input_ready:
  - `experiments/finalist_three_chapter_packages/2026-09-22_finalist_X_ch001_003.md`
  - `experiments/finalist_three_chapter_packages/2026-09-22_finalist_Y_ch001_003.md`
- deliver_to: editor_in_chief

## book_writer_v2
- status: DONE / PAUSED
- execution_window: Ch7—10正文续写已完成并经Total Editor Internal Quality PASS
- current: `handoffs/book_writer_v2/CURRENT.md`
- completed_task: Dual Finalist Ch7—10 Prose Continuation
- brief: `research/briefs/2026-09-23_dual_ch007_010_prose_continuation_brief.md`
- selfcheck: `reviews/2026-09-23_dual_ch007_010_writer_selfcheck.md`
- ten_chapter_packages:
  - `experiments/finalist_ten_chapter_packages/2026-09-23_finalist_X3_ch001_010.md`
  - `experiments/finalist_ten_chapter_packages/2026-09-23_finalist_Y3_ch001_010.md`
- mapping:
  - X3 = C01
  - Y3 = C12
- deliver_to: editor_in_chief / Internal Quality Gate
- hard_rule: no Ch11 / no Primary / no reader test / no new research
- note: 原opening_writer已到对话上限，永久退休

## blind_reader
- status: PAUSED
- next_task: Fresh Blind Read after new Ch1 / Ch1—3 package exists
- current: `handoffs/blind_reader/CURRENT.md`

---

# Next Gate Sequence

1. **Author P1｜DONE 2026-09-22**
   - AC-Hybrid P1 Authority Change已获作者明确批准（D-0048）。

2. **Authority Rewrite｜DONE / PASS（D-0049）**
   - Story Engine
   - Phase Outline
   - 第一重点收藏设计
   - Opening Scene Spine
   - Ch1—3
   - Ch4—10
   - Self Red Team

3. **Authority Rewrite Review｜DONE / PASS**
   - 只复核第一收藏来源与Canon语法
   - 只复核余扰/隔离/退余闭环
   - 只复核Ch7/Ch9去教学关
   - 只复核STATE权威导航
   - 决定是否放行Event-First Execution Validation

4. **Opening Execution Validation｜DONE / PASS（D-0050）**
   - 只验证新版Event-First完整体验链：
     > 真切味 -> 无即时力量 -> 正常筑基 -> 稳定离体 -> 救援继续
   - 不重开A/C大理论研究。

5. **Formal Ch1 Draft｜DONE / HOLD AS CONTROL**
   - Human Prose Gate
   - Commercial Shelf Test
   - Independent Red Team
   - 必要时Fresh Blind Read
   - 然后交作者。

6. **World Background Reframe Research｜TOP-3 PATCH DONE / AWAITING RE-REVIEW**
   - Benchmark Deep Read｜DONE；
   - Market Scout｜DONE；
   - Total-editor consolidation｜DONE；
   - World Reframe主体｜DONE；
   - Top-3 Sharpening PATCH｜DONE；
   - 当前三席：C1R缺位复归 / C2人格工业 / C8R舍险契约；
   - Traditional AC-Hybrid继续作为Control；
   - Controlled Prototype Duel仍QUEUED，等待总评审复核PATCH。

---

# Global Do Not Continue
- 不重开#37大Benchmark。
- 不重开#38无限微样本训练。
- Authority Rewrite已获D-0048授权；仅mid_continuity按正式brief可修改第一卷Approved Outline。
- 不在新Opening Scene Spine前写正式Ch1。
- 不把Event-First当成已经完成新版完整执行验证。
- 不把微场景Prose PASS等同于整章能力PASS。


## World Background Research｜TOP-3 PATCH DONE / RE-REVIEW ACTIVE
- Benchmark Deep Read：DONE
- Market Scout：DONE
- Total-editor consolidation：DONE
- World Reframe主体：DONE
- Top-3 Sharpening PATCH：DONE
- Current Top 3：C1R缺位复归 / C2人格工业 / C8R舍险契约
- Traditional Control：KEEP
- Total Editor Re-review：ACTIVE
- World Prototype：QUEUED / BLOCKED BY RE-REVIEW
- Clean-room Blind Reader：NOT YET OPEN


## Book-Level Hit Concept Reframe｜ACTIVE UPSTREAM
- D-0053：Hit Fiction First
- Reader Obsession Market Scan：DONE
- Independent Hit Concept Foundry：DONE
- Popular Fiction Benchmark Gate：DONE
- Sheqi-family C1R/C2/C8R：HOLD AS CANDIDATES
- Book-Level Synthesis：DONE / Prototype Pool APPROVED
- Prototype Duel：DONE
- Fresh Clean-Room Blind Read：ACTIVE


## Book Finalists｜ACTIVE
- C01《明天已经卖掉》：FINALIST
- C12《替有钱人渡劫》：FINALIST
- C10《死人也要履约》：RESERVE
- C08《职业遗产》：DROP FOR CURRENT FINAL
- current_test: Ch2—Ch3 continuity / concept-fade / life-compounding


## Finalist Opening Arc｜STATUS UPDATE
- B Ch2—Ch3：DONE
- D Ch2—Ch3：DONE
- Writer Selfcheck：DONE
- Returning Reader Continuation Test：ACTIVE
- Second Fresh 3-Chapter Shelf Test：ACTIVE
- Old Opening Writer：RETIRED
- Book Writer V2：QUEUED / NEW WINDOW REQUIRED


## Final Book Direction｜AWAITING AUTHOR APPROVAL
- total_editor_recommendation: C01《明天已经卖掉》
- reserve: C12《替有钱人渡劫》
- returning_reader_test: DONE
- second_fresh_three_chapter_test: DONE
- final_synthesis: `reviews/2026-09-22_final_book_direction_synthesis.md`
- full_reboot_proposal: `reviews/2026-09-22_full_reboot_proposal_c01.md`
- authority_gate: **AUTHOR APPROVE / REJECT / HOLD**
- no Canon / Outline changes before approval


## D-0056 Dual Finalist Bootstrap｜ACTIVE
- author_direction: **C01 / C12两部都推进**
- C01:
  - status: DONE / PASS TO SYNTHESIS
  - task: Time-Market Analog + Novelty + Technical Plausibility + Long-Run
  - owner: market_scout
  - output:
    - `research/design/2026-09-23_c01_time_market_analog_novelty_bootstrap.md`
    - `reviews/2026-09-23_c01_novelty_bootstrap_selfcheck.md`
- C12:
  - status: ACTIVE RESEARCH
  - task: Industrial Cultivation + 《没钱修什么仙》Scale Benchmark + Long-Run
  - owner: benchmark_deepread
- C01 Full Reboot Proposal: HOLD
- Book Writer V2: BLOCKED
- hard_rule:
  > 两个Bootstrap完成前都不写Ch4。


## Dual First-10 Story Engine｜ACTIVE
- bootstrap_synthesis:
  `reviews/2026-09-23_dual_finalist_bootstrap_synthesis.md`
- C01 Bootstrap: DONE / PASS
- C12 Bootstrap: DONE / PASS
- C01 First-10 Engine: DONE / PASS SELF-CHECK
- C01 output:
  - `research/design/2026-09-23_c01_first10_story_engine.md`
  - `reviews/2026-09-23_c01_first10_engine_selfcheck.md`
- C12 First-10 Engine: ACTIVE
- Book Writer V2: still BLOCKED
- next_after_both_engines:
  > Total Editor engine audit -> Book Writer V2 controlled 6-chapter validation


## D-0057 Longform Canopy Architecture｜ACTIVE
- framework:
  `meta/LONGFORM_CANOPY_ARCHITECTURE.md`
- author_reason:
  > 当前纵线/横线仍像光秃树干，必须在连续正文前证明枝叶和爽点供给足够厚。
- C01:
  - First-10: DONE
  - Canopy: DONE / PASS SELF-CHECK
  - output:
    - `research/design/2026-09-23_c01_longform_canopy_architecture.md`
    - `reviews/2026-09-23_c01_longform_canopy_selfcheck.md`
- C12:
  - First-10: ACTIVE
  - Canopy: QUEUED AFTER FIRST-10
- Book Writer V2:
  - BLOCKED
- hard_gate:
  > 两本Canopy通过总评审前，不进入持续正文生产。


## D-0059 Finalist Convergence Roadmap｜ACTIVE
- roadmap:
  `meta/FINALIST_CONVERGENCE_ROADMAP.md`
- now:
  - C01 Longform Canopy: DONE / PASS SELF-CHECK
  - C12 Longform Canopy: ACTIVE
- next:
  > Dual Canopy Total-Editor Shelf-Parity Audit
- after_pass:
  > single Book Writer V2 -> controlled six-chapter prose duel
- research_policy:
  > no new broad research unless a named evidence gap directly threatens real reading quality
- hard_rule:
  > writing/reading/prose proof becomes default after Canopy


## D-0060 Controlled Six-Chapter Prose Duel｜WRITER DONE / QUALITY CHAIN NEXT
- dual_canopy_audit:
  `reviews/2026-09-23_dual_canopy_total_editor_shelf_parity_audit.md`
- C01 Canopy: PASS TO PROSE
- C12 Canopy: PASS TO PROSE
- writer:
  `handoffs/book_writer_v2/CURRENT.md`
- writer_status: DONE / PAUSED
- prose_packages:
  - `experiments/finalist_six_chapter_packages/2026-09-23_finalist_X2_ch001_006.md`
  - `experiments/finalist_six_chapter_packages/2026-09-23_finalist_Y2_ch001_006.md`
- writer_selfcheck:
  `reviews/2026-09-23_dual_six_chapter_writer_selfcheck.md`
- next:
  > editor_in_chief / internal quality kill chain -> fresh six-chapter blind read -> total editor synthesis
- hard_rule:
  > no new broad research; no Ch7; no Primary decision before independent prose proof


## D-0061 Targeted Prose Patch｜WRITER PATCH DONE / DIFF GATE NEXT
- reason:
  - C01 T1-R continuity hard fail
  - C12 Ch5 failure fairness hard fail
  - several minor AI-summary / explanation issues
- audit:
  `reviews/2026-09-23_dual_six_chapter_internal_quality_gate.md`
- patch_brief:
  `research/briefs/2026-09-23_dual_six_chapter_targeted_prose_patch_brief.md`
- patch_selfcheck:
  `reviews/2026-09-23_dual_six_chapter_targeted_patch_selfcheck.md`
- patched_packages:
  - `experiments/finalist_six_chapter_packages/2026-09-23_finalist_X2_ch001_006_v2.md`
  - `experiments/finalist_six_chapter_packages/2026-09-23_finalist_Y2_ch001_006_v2.md`
- writer_status: DONE / PAUSED
- next:
  > Total Editor Quick Diff Gate -> if PASS Fresh Six-Chapter Blind


## six_chapter_fresh_reader
- status: DONE / PAUSED
- role: six_chapter_fresh_reader / Fresh Shelf Reader
- execution_window: **必须新开从未参与Sheqi项目的全新GPT窗口**
- current: `handoffs/six_chapter_fresh_reader/CURRENT.md`
- brief: `research/briefs/2026-09-23_finalist_six_chapter_fresh_blind_read_brief.md`
- hard_input:
  - `experiments/finalist_six_chapter_packages/2026-09-23_finalist_X2_ch001_006_v2.md`
  - `experiments/finalist_six_chapter_packages/2026-09-23_finalist_Y2_ch001_006_v2.md`
- mapping: hidden from reader
- deliver_to: editor_in_chief
- next: Total Editor synthesis


## D-0063 Fresh Six-Chapter Blind｜ACTIVE
- diff_gate:
  `reviews/2026-09-23_dual_six_chapter_targeted_patch_diff_gate.md`
- verdict: PATCH PASS
- fresh_reader:
  `handoffs/six_chapter_fresh_reader/CURRENT.md`
- no new broad research
- no Ch7
- after_blind:
  > Total Editor synthesis -> decide First-30 Development vs Targeted Patch vs Hold


## D-0064 Dual Ch7—10 Continuation｜ACTIVE
- six_chapter_fresh_blind:
  `reviews/2026-09-23_finalist_six_chapter_fresh_blind_read.md`
- total_editor_synthesis:
  `reviews/2026-09-23_six_chapter_fresh_blind_total_editor_synthesis.md`
- result:
  - C01: STRONG PASS
  - C12: STRONG PASS
  - relative: C01 small lead
  - C12: stronger character attachment
- writer:
  `handoffs/book_writer_v2/CURRENT.md`
- brief:
  `research/briefs/2026-09-23_dual_ch007_010_prose_continuation_brief.md`
- next:
  > Writer Ch7—10 -> Total Editor Internal Quality Gate
- hard:
  > no Ch11 / no Primary yet / no broad research


## ten_chapter_fresh_reader
- status: DONE / PAUSED
- role: ten_chapter_fresh_reader / Fresh Longform Shelf Reader
- execution_window: **必须全新GPT窗口，且此前从未读过Sheqi/C01/C12/X/Y系列**
- current: `handoffs/ten_chapter_fresh_reader/CURRENT.md`
- brief: `research/briefs/2026-09-23_finalist_ten_chapter_fresh_blind_read_brief.md`
- inputs:
  - `experiments/finalist_ten_chapter_packages/2026-09-23_finalist_X3_ch001_010.md`
  - `experiments/finalist_ten_chapter_packages/2026-09-23_finalist_Y3_ch001_010.md`
- mapping: hidden from reader
- deliver_to: editor_in_chief


## D-0065 Fresh Ten-Chapter Blind｜ACTIVE
- quality_gate:
  `reviews/2026-09-23_dual_ch007_010_internal_quality_gate.md`
- verdict:
  - C01 PASS
  - C12 PASS
- fresh_reader:
  `handoffs/ten_chapter_fresh_reader/CURRENT.md`
- core_test:
  > Mature hot-shelf feel + Ch11 click + 20—50 chapter willingness
- next:
  > Fresh report -> Total Editor synthesis
- hard:
  > no Ch11 / no new research / no Writer polish before reader evidence


## D-0066 Dual-Evidence Gate｜QUEUED
- current_step:
  > Fresh Ten-Chapter Blind
- next_step:
  > Head-Tier Benchmark Parity
- benchmark_brief:
  `research/briefs/2026-09-23_ten_chapter_headtier_benchmark_parity_brief.md`
- activation_condition:
  > ten_chapter_fresh_reader DONE
- final_decision_requires:
  - Fresh Reader evidence
  - Head-Tier Benchmark evidence
- hard_rule:
  > neither internal taste nor benchmark alone can authorize Ch11—30 / Primary


## D-0067 Asymmetric Finalist Development｜ACTIVE
- fresh_ten_chapter:
  `reviews/2026-09-23_finalist_ten_chapter_fresh_blind_read.md`
- headtier_benchmark:
  `reviews/2026-09-23_ten_chapter_headtier_benchmark_parity.md`
- synthesis:
  `reviews/2026-09-23_dual_evidence_ten_chapter_total_editor_synthesis.md`
- C01:
  - status: DONE / PASS TO TOTAL-EDITOR ARC AUDIT
  - task: Ch11—30 Reader-Desire Arc Development
  - owner: market_scout / c01_book_architect
  - output:
    - `research/design/2026-09-23_c01_ch011_030_reader_desire_arcs.md`
    - `reviews/2026-09-23_c01_ch011_030_arc_selfcheck.md`
- C12:
  - status: ACTIVE
  - task: Ch11—15 Life-First De-Curricularization Arc
  - owner: benchmark_deepread / c12_book_architect
- Book Writer V2:
  - status: PAUSED
  - reason: next-arc designs must pass Total Editor first
- no_primary_yet:
  > C01 current front-runner; C12 retained because gap is targeted and repairable
