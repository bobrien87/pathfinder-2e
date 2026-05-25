---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pteranodon"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +7"
abilityMods: ["+3", "+4", "+1", "-4", "+2", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +7, **Ref** +10, **Will** +6"
health:
  - name: HP
    desc: "25"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +10 (`pf2:1`) (unarmed), **Damage** 1d10+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Swoop"
    desc: "`pf2:2` The pteranodon Flies up to its Speed and makes one beak Strike at any point during that movement."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Pteranodons are quick and agile reptiles with 20-foot wingspans that enable them to hover on wind currents for hours. These creatures have long beaks and equally long crests that protrude from the backs of their heads.

Pterosaurs are primitive flying creatures. While many are smaller than a human or even small enough to perch on a shoulder, the two presented below are quite a bit larger. Each of these creatures could pose a serious threat to a person.

These flying reptiles can be found in a wide selection of regions, but they tend to soar above warm or temperate climates. They sometimes spread outside their natural range as pets and hunting companions for lizardfolk or giants. Cloud giants living in isolated valleys also train the largest pterosaurs to carry their messages to the outside world.

```statblock
creature: "Pteranodon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
