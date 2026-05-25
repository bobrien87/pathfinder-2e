---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Prophet"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10"
languages: "Common"
skills:
  - name: Skills
    desc: "Diplomacy +8, Performance +8, Religion +7, Survival +7"
abilityMods: ["+2", "+1", "+0", "+1", "+3", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +7, **Will** +11"
health:
  - name: HP
    desc: "25"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Flail +8 (`pf2:1`) (disarm, sweep, trip), **Damage** 1d6+2 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +8 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Rock +7 (`pf2:1`) (thrown 10), **Damage** 1d4+2 bludgeoning"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 18, attack +10<br>**1st** (4 slots) [[Bless]], [[Daze]], [[Detect Magic]], [[Enfeeble]], [[Guidance]], [[Heal]], [[Know the Way]], [[Light]], [[Read Aura]], [[Sanctuary]]"
  - name: "Cleric Domain Spells"
    desc: "DC 18, attack +10<br>**1st** [[Read Fate]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The gods occasionally send messages in dreams to individuals who wander the lands. Some prophets have not received true divine missives but have misinterpreted normal dreams.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Prophet"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
