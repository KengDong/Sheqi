# ACTIVE WORKSTREAMS｜REBOOT-V6 B01-V4 PARALLEL LANES
updated: 2026-10-09
branch: reboot-v6-verified-scene-lab

## ACTIVE / 3 INDEPENDENT RESEARCH ROLES
1. b01_fanqie_scout | branch `b01-fanqie-scene-scout` | handoffs/b01_fanqie_scout/CURRENT.md
   Focus: real Fanqie male-fiction scenes and narrative efficiency
2. b01_crossplatform_scout | branch `b01-crossplatform-idea-scout` | handoffs/b01_crossplatform_scout/CURRENT.md
   Focus: cross-platform original premise/scene/durable plot engine
3. b01_reader_reaction_scout | branch `b01-reader-reaction-scout` | handoffs/b01_reader_reaction_scout/CURRENT.md
   Focus: reader-remembered moments and original chapter traceability

Branches each start from the same base and own different output directories/handoffs. Each worker may search simultaneously, must commit actual findings and create PR against `reboot-v6-verified-scene-lab`, not directly merge.

## PAUSED / INTEGRATION ROLE
verified_scene_scout | base `reboot-v6-verified-scene-lab`
handoffs/verified_scene_scout/CURRENT.md
Role now **CURATOR**, to merge/dedup/critically review after lane results/PRs. Do not compete with other workers before their first results.

## B01 AUTHOR GATE
Author receives rolling verified highlights and full source library, then decides favorite concrete scenes/reader fantasies.
No B02/novel writing until explicit author selection.

## STOP / WRITE COLLISION SAFETY
- Never ask 3 GPT chats to write the same branch/file.
- Each role only modifies its `lanes/<id>` and `handoffs/<role>` directory; no shared meta edits.
- Old B01 V1/V2 sample caps withdrawn; B01 V3 broad discovery remains valid.
- No fake comments/heat, no copied original expression or near-copy publishable rewrite.
- Start guide: `ops/2026-10-09_B01_MULTI_WINDOW_START.md`.
