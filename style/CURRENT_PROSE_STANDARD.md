# Sheqi｜CURRENT PROSE STANDARD
status: CANONICAL SHARED WRITING STANDARD
scope: all formal fiction prose on this branch
stable_path: yes

> This file is the stable entrypoint.
> Git history carries versions. Future writer windows should read THIS path, not guess which dated V1/V2 file is newest.

# 1. Target prose
Write fast, natural Chinese webnovel prose that reads like continuous storytelling, not subtitle cards.

Core:
> 快，不等于碎。
> 一个段落应该完成一个语义动作，而不是把一个动作切成很多视觉短句。

Default paragraph:
- 1-3 linked sentences;
- one complete beat: stimulus -> interpretation/reaction -> action/consequence;
- medium-length sentences are the default;
- short sentences are emphasis, not the base texture.

# 2. Paragraph-break rule
Before every paragraph break ask:
> 这个意思真的讲完了吗？

If not, do not break.

Do not split:
- one observation into 3 lines;
- one answer into several one-word turns;
- one body movement into separate body-part shots.

Bad:
> “哪学的？”
> “刚才。”
> “谁？”
> “不知道。”

Better:
> “哪学的？”
> 程野看了眼刚才雨院消失的位置：“刚才现学的。你要问老师是谁，我也正想知道。”

# 3. Short-line hard guard
Before author review:
- standalone narrative under 6 Chinese chars: almost never;
- standalone dialogue under 4 Chinese chars: only if brevity itself carries pressure/emotion;
- no 3 consecutive short turns under 8 chars in ordinary conversation;
- in ~300 Chinese chars, no more than 2 standalone short units under 8 chars.

Rare legitimate examples:
> “跑！”
> “谁？”
> “停手！”

These are pressure beats, not ordinary rhythm.

# 4. Dialogue standard
Dialogue should carry at least two of:
- information;
- attitude;
- relationship;
- decision;
- conflict;
- humor;
- scene movement.

Do not leave drafting shorthand in formal prose:
> 刚才。
> 少贫。
> 查。
> 对。
> 行。
> 不信。

Integrate or expand unless the character intentionally shuts the exchange down.

Use action beats when they add subtext, not every line.

# 5. Cheng Ye voice application
His humor comes from how he thinks, not joke density.

Pattern:
> notice practical rule -> make slightly crooked but reasonable inference -> act -> dry/light conclusion.

Good:
> 平台买极限数据，保险也生效了。他还一直绕着弱点走，多少有点对不起这份保费。

Avoid:
> 八百。
> 保险。
> 值。
> 干。

# 6. Sentence rhythm
Mix:
- short: impact / turn / joke;
- medium: default narrative;
- long: continuous motion / layered observation / causal explanation.

Do not make an entire page one-sentence-one-paragraph.

# 7. Action continuity
Linked motion stays causally linked.

Must be able to answer:
- body position;
- what creates next movement;
- opponent response;
- why hit/evasion succeeds.

Preferred:
> 程野右脚内扣，重心随之压低，借着错身的势头从周航掌侧切过去，转腰时右手顺势拍上对方后背的感应区。

Do not write:
> 内扣。
> 压身。
> 切线。
> 转身。
> 拍中。

unless intentionally slowing a decisive instant.

# 8. Suspense
Create suspense through impossible information or violated expectation, not line breaks.

Preferred:
> 程野先听见了雨声。可训练馆顶棚封得严严实实，场内连风都没有。

Avoid:
> 雨。
> 不对。
> 这里没有雨。

# 9. Explanation
Do not let narrator defend worldbuilding.

Bad:
> 古法并不比现代更高级。

Better:
show risk through coach playback, failed angle, injury consequence; let character conclude naturally:
> “不是学校没教，是学校不敢拿这招教一屋子人。”

# 10. Reaction specificity
Avoid default AI reactions:
- 愣了一下;
- 沉默两秒;
- 眼神一变;
- 心里一动;
- 嘴角勾起.

Prefer visible behavior or specific thought.

# 11. Modern / ancient language
Modern:
- contemporary names;
- ordinary institutions;
- familiar work/platform vocabulary;
- contemporary conversational rhythm.

Ancient/source era:
- older naming texture;
- era-appropriate social vocabulary;
- no accidental modern corporate/internet phrasing.

Reader should often classify era before exposition.

# 12. Required pre-delivery passes
Every formal chapter, in order:
1. STORY PASS — scene function and payoff;
2. CHARACTER PASS — Cheng Ye and recurring cast behave from their engines;
3. SEMANTIC-BEAT PASS — merge fragments into complete thought units;
4. DIALOGUE PASS — remove shorthand ping-pong;
5. ACTION PASS — physical continuity;
6. AI-PATTERN PASS — repeated stock phrasing / contrast structures;
7. READ-ALOUD PASS — prose must sound natural when read continuously;
8. PROSE LINT — run tools/prose_lint.py if executable environment is available;
9. HOOK/PAYOFF PASS — chapter both pays something and opens next desire.

Only then show author.

# 13. Authority
If dated style research conflicts with this file:
> this file wins unless the active writer brief explicitly declares a newer override.

Detailed failure examples:
> style/COMMON_PROSE_FAILURES.md

Mechanical checker:
> tools/prose_lint.py
