---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Trained Bat"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Echolocation]] (precise) 20 feet, [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +9, Intimidation +6, Stealth +12, Survival +8"
abilityMods: ["+3", "+4", "+3", "-4", "+2", "+0"]
abilities_top:
  - name: "Echolocation"
    desc: "A bat can use hearing as a precise sense at the listed range."
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +12, **Will** +10"
health:
  - name: HP
    desc: "50"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +14 (`pf2:1`) (finesse, unarmed), **Damage** 2d6+6 piercing"
  - name: "Melee strike"
    desc: "Wing +14 (`pf2:1`) (agile, finesse, unarmed), **Damage** 2d4+6 slashing"
spellcasting: []
abilities_bot:
  - name: "Wing Thrash"
    desc: "`pf2:2` The trained bat thrashes wildly with its wings, making wing Strikes against up to three adjacent foes. Each attack counts toward the bat's multiple attack penalty, but the penalty increases only after all the attacks have been made."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`



```statblock
creature: "Trained Bat"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
