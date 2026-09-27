# SHARED｜FORMAL PROSE WRITER PROTOCOL
status: MANDATORY BOOTSTRAP FOR FORMAL FICTION WRITER WINDOWS
stable_path: yes

Purpose:
> make separate windows behave like one continuing human writing team.

# 1. Required read order
A formal prose writer window should be explicitly authorized by its own CURRENT / brief to read these shared files.

Read in this order:
1. its own handoff CURRENT and assigned brief;
2. style/CURRENT_PROSE_STANDARD.md;
3. style/COMMON_PROSE_FAILURES.md;
4. characters/CHENG_YE_CHARACTER_BIBLE.md if Cheng Ye appears;
5. characters/CHENG_YE_CURRENT_STATE.md if Cheng Ye appears;
6. any scene/world/rule files explicitly named by the assigned CURRENT;
7. current formal-draft baseline explicitly named by the assigned CURRENT.

Do NOT roam the repository to gather extra inspiration if HARD INPUT BOUNDARY forbids it.

# 2. Stable file principle
Shared operational files use stable paths.

Do NOT create:
> CURRENT_PROSE_STANDARD_V3_FINAL_FINAL.md

Instead:
- update the stable file in place;
- Git history preserves older versions;
- dated research notes may remain as archive.

This prevents future windows from guessing which version is latest.

# 3. Authority order
If information conflicts:
1. active task CURRENT / brief for task-specific boundaries;
2. current shared stable files for prose/character behavior;
3. specifically named current rule/world files;
4. old dated experiments / reports.

Never let an obsolete prose draft override the current character bible.

# 4. Invariant vs mutable character memory
Character personality:
> CHARACTER_BIBLE

Changing story facts:
> CURRENT_STATE

Why:
> a human character stays recognizable while knowledge, trust, resources and scars evolve.

Do not rewrite personality because plot-state changed.
Do not freeze story-state inside personality file.

# 5. Writer delivery workflow
Before author sees prose:
1. write scene for story goal;
2. verify character choices against bible;
3. verify mutable facts against current state;
4. apply prose standard;
5. check common failures;
6. run prose lint when available;
7. read-aloud pass;
8. update draft;
9. only after author acceptance or clear state change, update CURRENT_STATE;
10. record meaningful new author feedback into the relevant stable shared file.

# 6. Feedback routing
When author says:
> "这句太AI"
Do not only patch the sentence.

Ask internally:
> is this a reusable failure class?

If yes:
- add/update COMMON_PROSE_FAILURES;
- add a rule to CURRENT_PROSE_STANDARD only if it changes positive writing behavior.

When author says:
> "程野不会这么说"
Route to:
- CHARACTER_BIBLE if it reveals stable personality;
- CURRENT_STATE if it depends on what Cheng Ye knows/feels at this point only.

When author changes names:
- update naming convention / current state as needed;
- do not muddy character personality file with long naming history.

# 7. No silent canonization
Author feedback like:
> 可以 / 这个方向可以

means:
> retained / current working direction unless explicitly locked.

Formal writer must distinguish:
- working;
- current baseline;
- author-approved direction;
- canon/locked.

# 8. Handoff requirement for new writer windows
When architect creates a new prose-writer CURRENT, include a HARD INPUT BOUNDARY block explicitly listing the shared files above.

Example:
> You may read:
> - your CURRENT;
> - your writer brief;
> - style/CURRENT_PROSE_STANDARD.md;
> - style/COMMON_PROSE_FAILURES.md;
> - characters/CHENG_YE_CHARACTER_BIBLE.md;
> - characters/CHENG_YE_CURRENT_STATE.md;
> - [specific chapter/world files].

Without explicit authorization:
> do not assume shared files are allowed under isolation tests.

# 9. End-of-window handoff
A writer window should record:
- file written;
- exact baseline it used;
- which shared standards it read;
- any new reusable style feedback;
- character state changes proposed vs accepted;
- Git commit.

This lets the next window continue without chat history.

# 10. Desired result
Separate windows should feel like:
> one author with memory,
not
> many assistants independently rediscovering tone.
