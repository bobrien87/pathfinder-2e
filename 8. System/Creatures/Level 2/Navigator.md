---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Navigator"
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
    desc: "+9"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +6, Nature +11, Society +8, Survival +9, Sailing Lore +14"
abilityMods: ["+0", "+2", "+1", "+4", "+3", "+0"]
abilities_top:
  - name: "Chart a Course"
    desc: "By spending 10 minutes of work and succeeding at a DC 22 Sailing lore check{Sailing Lore} check, the navigator plots an optimal course. <br>  <br> The severity of environmental conditions other than temperature are reduced by one step for 24 hours (two steps on a critical success). This changes moderate damage to minor damage, winds that create greater difficult terrain cause only difficult terrain, and so on."
  - name: "Sailing Specialist"
    desc: "For encounters involving navigation or sailing, the navigator is a 4th-level challenge."
  - name: "Navigator's Edge"
    desc: "The navigator's Strikes deal an additional 1d6 damage when on a ship."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +8, **Will** +9"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+4 piercing plus [[Navigators Edge]]"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+4 piercing plus [[Navigators Edge]]"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A navigator uses celestial bodies and shipping lanes to determine routes.

Adventurers may need passage on a swift vessel, or they might face danger from raiders at sea or in coastal settlements.

```statblock
creature: "Navigator"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
