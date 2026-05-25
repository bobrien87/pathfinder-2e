---
type: creature
group: ["Mindless", "Skeleton"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skeleton Guard"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+2; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +3"
abilityMods: ["+2", "+4", "+0", "-5", "+0", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +2, **Ref** +8, **Will** +2"
health:
  - name: HP
    desc: "4; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** cold 5, electricity 5, fire 5, piercing 5, slashing 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +6 (`pf2:1`) (forceful, sweep), **Damage** 1d6+2 slashing"
  - name: "Melee strike"
    desc: "Claw +6 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4+2 slashing"
  - name: "Ranged strike"
    desc: "Shortbow +6 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The most common skeletal minions are mere guardians.

Animated skeletons are among the most common types of undead.

```statblock
creature: "Skeleton Guard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
