---
status: READY
date: 2026-09-26
decision: REBOOT-V4
platform: FANQIE
role: fanqie_market_entry_scout
version: 2.1
creative_output: FORBIDDEN
---

# Fanqie Market Entry V2.1｜Coverage & Evidence Freeze Patch

# 0. Authority
Read:
1. `meta/RESTART_AUTHORITY_V1.md`
2. `reviews/2026-09-26_master_failure_postmortem_and_repo_reset.md`
3. `reviews/2026-09-26_fanqie_market_entry_v2_editor_gate.md`
4. existing V2 report + Board.

# 1. Goal
Do NOT redo the six pools from scratch.

Patch the missing question:
> **Did V2 comprehensively scan the relevant current Fanqie male market before freezing the author-choice board?**

# 2. Build a full category coverage matrix

Using current Fanqie official rank taxonomy, enumerate all relevant male categories / major subcategories visible to the platform.

For each:
- category;
- official reading-rank URL;
- official new-book-rank URL;
- scanned date;
- current strong examples;
- current new-book examples;
- potential exact Reader Pools;
- outcome:
  - QUALIFIED POOL;
  - NO CLEAN POOL FOUND;
  - IP/SEQUEL-DISTORTED;
  - VETERAN-ONLY;
  - TOO BROAD / NEEDS SPLIT;
  - EVIDENCE INSUFFICIENT.

At minimum explicitly inspect whether current evidence exists for:
- 都市高武;
- 玄幻脑洞;
- 传统玄幻 / 东方玄幻;
- 都市脑洞;
- 游戏体育 / 全民转职 / 游戏入侵;
- 御兽 / 宠兽;
- any other major male categories present in current Fanqie rank taxonomy.

Do NOT assume these categories must qualify.

# 3. New pool qualification

Any newly discovered pool must meet the SAME V2 bar:
- 3–5 strong/direct or clearly labeled neighbor comps;
- current new-book proof where available;
- low-author-credit/newcomer evidence where available;
- >=2 matched weak controls where available;
- Primary / Secondary / Protagonist Fantasy;
- Ch1–3 promise;
- post-novelty continuation;
- saturation;
- falsification.

# 4. DIRECT / NEAR evidence labels

For every final Board pool:
label every strong example:
- DIRECT;
- NEAR;
- VETERAN CONTROL;
- IP/SEQUEL CONTROL.

Hard:
> at least 2 current/recent DIRECT Fanqie comps,
otherwise mark the pool CONDITIONAL.

# 5. Evidence freeze

Create:
> `research/evidence/fanqie_market_entry_2026-09-26/INDEX.md`

For every cited dynamic rank / author evidence:
freeze a compact observation record:
- source URL;
- observed / cutoff date;
- title;
- rank/category if available;
- current in-read figure if used;
- word/chapter length if used;
- author visible work/follower/creation-time signals if used;
- role in analysis: DIRECT / NEAR / WEAK / NEWCOMER / CONTROL.

Do NOT copy full copyrighted prose.

# 6. Revise research report

Update:
> `research/2026-09-26_reboot_v4_fanqie_market_entry_v2.md`

Add:
- category coverage appendix;
- any missing qualified pools;
- DIRECT/NEAR labels;
- corrected exclusions;
- evidence freeze references.

# 7. Revise author board

Update:
> `experiments/reboot_v4/author_choice/fanqie_market_entry_board_v2.md`

Add one factual field:
> **Evidence Strength**
- STRONG EVIDENCE
- MODERATE EVIDENCE
- CONDITIONAL

This is evidence quality only.
No ranking / recommendation.

# 8. Control-plane sync

On completion update:
- own CURRENT -> COMPLETE;
- HISTORY;
- `meta/STATE.md` -> AWAITING EDITOR REVIEW;
- `meta/ACTIVE_WORKSTREAMS.md` -> scout complete, no downstream;
- editor CURRENT -> READY FOR V2.1 REVIEW.

# 9. Hard
- no concept generation;
- no prose;
- no AI winner;
- no old candidate revival;
- no automatic downstream dispatch.

# STOP
After V2.1 patch, STOP.
