---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Cockroach"
level: "1"
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
    desc: "+6; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Stealth +8"
abilityMods: ["+1", "+3", "+1", "-5", "+1", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +6, **Ref** +8, **Will** +4"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Scurry"
    desc: "`pf2:r` **Trigger** The giant cockroach is targeted by a melee attack <br>  <br> **Effect** The giant cockroach gains a +2 circumstance bonus to AC against the triggering attack. After the attack resolves, the cockroach Strides, Climbs, or Flies up to 10 feet."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +8 (`pf2:1`) (agile, finesse), **Damage** 1d6+1 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Cockroaches are communal creatures, rarely setting out on their own unless they are searching for food. If an adventurer encounters a single giant cockroach while exploring, they had best take precautions against others, as there is likely an entire colony nearby.

```statblock
creature: "Giant Cockroach"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
