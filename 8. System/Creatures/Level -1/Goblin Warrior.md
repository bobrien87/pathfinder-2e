---
statblock: true
layout: Basic Pathfinder 2e Layout
type: creature
group: ["Goblin", "Humanoid"]
name: "Goblin Warrior"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: "Neutral Evil"
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; Darkvision"
languages: "Goblin, Common"
skills:
  - name: Skills
    desc: "Acrobatics +5, Stealth +7, Athletics +3"
abilityMods: ["+1", "+4", "+1", "+0", "+1", "-1"]
abilities_top:
  - name: "Goblin Scurry"
    desc: "`pf2:r` **Trigger** An ally ends its movement adjacent to the goblin; **Effect** The goblin steps."
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +7, **Will** +3"
health:
  - name: HP
    desc: "6"
abilities_mid: []
speed: "25 feet"
attacks:
  - name: "Melee strike"
    desc: "Dogslicer +8 (`pf2:1`), **Damage** 1d6+1 slashing (agile, finesse)"
  - name: "Ranged strike"
    desc: "Shortbow +8 (`pf2:1`), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Bestiary"
source-type: "Remaster"
---
### `= this.file.name`

A sneaky goblin warrior equipped with a dogslicer and a shortbow.

```statblock
creature: "Goblin Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
