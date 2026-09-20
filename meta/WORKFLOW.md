# AI 长篇协作工作流

## 1. 研究
放入 `research/`。研究只回答“别人怎么做/我们为什么这样决定”，不自动变成 Canon。

## 2. Proposal
新创意先作为候选。若触碰底层规则，必须明确标注 Proposed Change。

## 3. Canon
只有作者明确确认的规则、人物事实、时间线、术语才进入 `canon/`。

## 4. Outline
- `outline/master_outline.md`：全书中央因果链
- `outline/volume_XX.md`：分卷
- `outline/chapter_cards/`：章节卡

大纲可以改，但必须记录与 Canon 的兼容性。

## 5. Draft
AI 初稿放在 `drafts/`，默认不是正史。

## 6. Review
至少检查：
- 情节因果
- 人物动机
- 爽点/悬念兑现
- 设定一致性
- 人物知识边界
- 伏笔
- 节奏与重复

## 7. Manuscript
作者明确批准后进入 `manuscript/`。这里的“已发生事实”拥有最高叙事权威。

## 每章通过后同步
- 人物当前状态
- 时间线
- 物品/余器状态
- 新伏笔/回收伏笔
- 新增世界事实
- 当前项目 STATE 摘要

## Git 约定
建议分支：
- `proposal/*`
- `outline/*`
- `draft/*`
- `fix/*`
- `research/*`

`main` 只保留已批准内容或稳定的项目管理文件。

Commit 前缀：
- `world:`
- `character:`
- `outline:`
- `draft:`
- `fix:`
- `research:`
- `meta:`
