---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Acolyte of Iomedae"
level: "1"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Diplomacy +5, Intimidation +5, Religion +7, Society +4"
abilityMods: ["+1", "+2", "-1", "+1", "+4", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +2, **Ref** +5, **Will** +9"
health:
  - name: HP
    desc: "15"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +6 (`pf2:1`) (versatile p), **Damage** 1d8+1 slashing"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +7 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8 piercing"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 17, attack +9<br>**1st** (6 slots) [[Heal]], [[Heal]], [[Heal]], [[Heal]], [[Sanctuary]], [[Sure Strike]]<br>**Cantrips** [[Detect Magic]], [[Light]], [[Read Aura]], [[Shield]], [[Void Warp]]"
  - name: "Cleric Domain Spells"
    desc: "DC 17, attack +9<br>**1st** [[Weapon Surge]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Underling clerics are still learning the tenets of their faith and answering to a superior priest. Their days are spent in devotion and learning, sequestered in temples.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Acolyte of Iomedae"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
