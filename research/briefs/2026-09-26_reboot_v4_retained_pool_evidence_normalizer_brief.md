# REBOOT-V4｜Retained Pool Evidence Normalizer Brief

date: 2026-09-26
branch: `reboot-v4-fanqie-market-entry`
role: `retained_pool_evidence_normalizer`
stage: POST-DEEPREAD / PRE-EDITOR-SYNTHESIS
mode: MECHANICAL / NON-RANKED

# Purpose

Convert the five completed retained-pool deep reads into a common evidence schema.

This worker is NOT an editor and must NOT recommend, rank, score, or choose a pool.

# Hard Inputs

Read only:
1. this brief;
2. the five completed reports:
   - `research/deepreads/2026-09-26_reboot_v4_fanqie_pool01_minsu_deepread.md`
   - `research/deepreads/2026-09-26_reboot_v4_fanqie_pool02_yiwu_deepread.md`
   - `research/deepreads/2026-09-26_reboot_v4_fanqie_pool03_weiyi_deepread.md`
   - `research/deepreads/2026-09-26_reboot_v4_fanqie_pool04_survival_asset_deepread.md`
   - `research/deepreads/2026-09-26_reboot_v4_fanqie_pool06_historical_status_deepread.md`

Do NOT read:
- old Sheqi candidates;
- prose;
- Concept files;
- other old market studies unless directly referenced by one of the five reports.

# Required Output

Create:
> `research/synthesis_inputs/2026-09-26_reboot_v4_retained_pool_normalized_evidence.md`

For each Pool use the exact same fields:

1. Primary Reader Fantasy
2. First Payment
3. First Irreversible State Change
4. Compounding Asset
5. Long-Run Loop
6. Earliest HIT-vs-WEAK divergence
7. Does divergence persist to Ch20?
8. Major confounders
9. Newcomer burdens:
   - domain
   - logic continuity
   - scene generation
   - character/relationship
   - long-run escalation
10. False imitation trap
11. Weakly served reader functions
12. Evidence confidence by conclusion:
   - STRONG MECHANISM
   - MODERATE MECHANISM
   - LIMITED CAUSAL
   - UNPROVEN

# Hard Rules

- No overall pool grade.
- No ranking.
- No “best / easiest / most suitable”.
- No recommendation.
- No Concept generation.
- Preserve Pool 6 = MAYBE.
- Do not turn read-count differences into causal proof.
- If the five reports use different terminology for the same field, normalize terminology but preserve meaning.
- If evidence is missing, write MISSING / UNPROVEN rather than infer.

# Exit

Commit output, update own CURRENT/history, then STOP.
