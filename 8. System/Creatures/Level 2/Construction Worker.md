---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Construction Worker"
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
    desc: "+5"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +10, Crafting +13, Society +6, Architecture Lore +15"
abilityMods: ["+4", "+0", "+3", "+2", "+1", "+0"]
abilities_top:
  - name: "By Design"
    desc: "The construction worker spends 1 minute inspecting the layout of a room and attempts a DC 22 Architecture lore check. On a success, they learn the size and layout of all adjacent rooms on the same floor (or all rooms on the floor on a critical success). They can inspect each room only once per day."
  - name: "Specialty Contractor"
    desc: "For encounters involving architecture or construction, the construction worker is a 6th-level challenge."
armorclass:
  - name: AC
    desc: "17; **Fort** +11, **Ref** +6, **Will** +7"
health:
  - name: HP
    desc: "35"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Maul +10 (`pf2:1`) (shove), **Damage** 1d12+4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Brick +6 (`pf2:1`) (thrown 10), **Damage** 1d6+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Demolishing Swing"
    desc: "`pf2:2` The construction worker makes a maul Strike against a creature. If it hits, the creature is pushed 10 feet. If the target is wearing metal armor, its armor also takes the damage, which bypasses 5 of the armor's Hardness."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A brilliant architect can contemplate wondrous structural marvels, but someone must pick up a hammer and make these dreams real. Construction workers are the backbone of any city's infrastructure.

Society is built upon the backs of laborers.

```statblock
creature: "Construction Worker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
