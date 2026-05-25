---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Martial Student"
level: "3"
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
    desc: "Acrobatics +9, Athletics +10"
abilityMods: ["+4", "+3", "+2", "+0", "+1", "+0"]
abilities_top:
  - name: "Powerful Fists"
    desc: "The martial student's fist Strikes don't take penalties when making lethal attacks."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +10, **Will** +6"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d6+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Fancy Footwork"
    desc: "`pf2:1` The martial student Steps and Strides in any order."
  - name: "Flurry of Blows"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The martial student makes two fist Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Every warrior must begin somewhere.

Martial artists strive to master the art of hand-to-hand fighting.

```statblock
creature: "Martial Student"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
