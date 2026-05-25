---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dancer"
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
    desc: "+4"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +7, Diplomacy +6, Performance +13, Stealth +6, Theatre Lore +5"
abilityMods: ["+1", "+3", "+1", "+0", "+0", "+4"]
abilities_top:
  - name: "Dance Specialist"
    desc: "For encounters involving contests of dancing, the dancer is a 5th-level challenge."
armorclass:
  - name: AC
    desc: "16; **Fort** +6, **Ref** +8, **Will** +3"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Foot +7 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Fascinating Dance"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The dancer Strides up to their Speed. Once during this movement, when the dancer is adjacent to a creature, the dancer can attempt to mesmerize that creature, who attempts a DC 17 [[Will]] save. On a failure, that creature is [[Fascinated]] with the dancer until the end of its next turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Dance can be used to tell stories, share emotions, provide entertainment, and display a performer's athletic ability.

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Dancer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
