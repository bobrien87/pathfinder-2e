---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Eagle"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6"
abilityMods: ["+0", "+3", "+1", "-4", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +4, **Ref** +6, **Will** +2"
health:
  - name: HP
    desc: "6"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +6 (`pf2:1`) (finesse, unarmed), **Damage** 1d6 piercing"
  - name: "Melee strike"
    desc: "Talon +6 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4 slashing"
spellcasting: []
abilities_bot:
  - name: "Eagle Dive"
    desc: "`pf2:2` The eagle [[Flies]] up to double its fly Speed in a straight line, descending at least 10 feet, and then makes a talon Strike."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These large birds of prey swoop down from incredible heights to snatch fish and small mammals in their powerful talons. Eagles nest atop high trees or steep cliffs that provide a commanding view of the surrounding area.

Few avian creatures can match the beauty and grace of the eagle.

```statblock
creature: "Eagle"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
