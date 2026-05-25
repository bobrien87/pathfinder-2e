---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Trilobite"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]], [[Wavesense]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +4, Stealth +5, Survival +4"
abilityMods: ["+1", "+3", "+2", "-5", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +4, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "7"
abilities_mid:
  - name: "Curl Up"
    desc: "`pf2:r` **Trigger** The trilobite takes damage <br>  <br> **Effect** The trilobite gains a +2 circumstance bonus to AC until the start of its next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Gnathobase +7 (`pf2:1`) (agile, finesse), **Damage** 1d4+1 slashing"
spellcasting: []
abilities_bot:
  - name: "Quick Escape"
    desc: "`pf2:2` The trilobite Swims up to double its Speed and attempts to [[Hide]]."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`



```statblock
creature: "Trilobite"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
