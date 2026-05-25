---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rigger"
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
    desc: "+10"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +7, Sailing Lore +6"
abilityMods: ["+3", "+4", "+1", "+0", "+1", "+0"]
abilities_top:
  - name: "Death from Above"
    desc: "The rigger deals an additional 1d4 precision damage to any creature at a lower elevation than themself."
  - name: "Practiced Climber"
    desc: "The rigger requires only one hand free to Climb and is not [[Off Guard]] when Climbing."
armorclass:
  - name: AC
    desc: "15; **Fort** +7, **Ref** +10, **Will** +5"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Rope Tension Spring"
    desc: "`pf2:2` **Requirements** The rigger is adjacent to a vertical rope on board a ship and is wielding a dagger <br>  <br> **Effect** The rigger loops the rope around one arm and severs the rope with their dagger. Counterweight and tension pull the rigger 20 feet straight up."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A knack for knots and no fear of heights are the prime qualifications of these high-flying rope wranglers and lookouts.

Adventurers may need passage on a swift vessel, or they might face danger from raiders at sea or in coastal settlements.

```statblock
creature: "Rigger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
