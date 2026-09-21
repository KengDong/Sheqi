# VISUAL TASK TEMPLATE｜单次视觉任务

~~~text
VISUAL TASK ID:

PURPOSE:
  [internal_qa / v0_explore / public_candidate / approved-public revision]

PUBLICATION LEVEL:
  [internal only / may publish after approval / public asset revision]

TEXT AUTHORITY:
  - manuscript:
  - canon:
  - approved outline:
  - approved chapter card:
  - decisions:

TIMEPOINT:
  - volume:
  - chapter:
  - before/after event:
  - character knowledge boundary:

CHARACTERS:
  - name:
  - master_ref:
  - body_ref:
  - outfit_ref:
  - state_ref:
  - required anchors:
  - allowed variation:
  - forbidden drift:

SCENE:
  - scene_ref:
  - scene_version:
  - normal/accident/state:
  - fixed geometry:
  - source_ref:
  - scope:
  - allowed visual exploration:
  - forbidden spatial changes:

PROPS:
  - prop_ref:
  - scale:
  - hand/side:
  - current condition:

LIGHTING:
  - lighting_ref:
  - time:
  - normal/emergency:

ALLOWED CANON ON SCREEN:
  -

FORBIDDEN / SPOILER:
  -

COMPOSITION INTENT:
  -

STYLE REF:
  -

OUTPUT:
  - aspect ratio:
  - intended size:
  - line/color:
  - text in image allowed?:

HARD-GATE CHECKS REQUIRED:
  [A/B/C/D/E/F/G/H]

REVIEWER:
APPROVAL REQUIRED FROM:

STORY CHANGE AUTHORITY:
  NONE.
  If image conflicts with approved text, reject/repair image.
  Do not alter story from image output.
~~~

## 停止条件

以下任一项成立，停止正式生成：
- 必要reference缺失；
- 角色仍处V0却要求官方角色图；
- 场景空间未通过文字硬门；
- 时间点不清；
- 剧透边界不清；
- 要求AI自由设计剧情关键设备；
- 要求根据生成结果修改章卡。
