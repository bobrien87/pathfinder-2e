---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Smith"
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
    desc: "+5"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +8, Crafting +15, Diplomacy +5, Society +8, Smithy Lore +15"
abilityMods: ["+3", "+1", "+2", "+3", "+0", "+0"]
abilities_top:
  - name: "Smithing Specialist"
    desc: "For encounters involving smithing or other crafting tasks, the smith is a 6th-level challenge."
  - name: "Smith's Fury"
    desc: "The smith deals an additional 1d6 damage when they hit with a weapon they created."
armorclass:
  - name: AC
    desc: "17; **Fort** +9, **Ref** +8, **Will** +5"
health:
  - name: HP
    desc: "50"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Light Hammer +10 (`pf2:1`) (agile), **Damage** 1d6+3 bludgeoning plus [[Smiths Fury]]"
  - name: "Melee strike"
    desc: "Light Hammer +8 (`pf2:1`) (agile, thrown 20), **Damage** 1d6+3 bludgeoning plus [[Smiths Fury]]"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Most smaller communities have at least one smithy where locals and travelers can have horses shod or equipment repaired. Larger settlements and cities often have a variety of smiths, many specializing in blacksmithing, weapon smithing, armor smithing, or even smelting coins in a mint.

Expertise is forged through years of effort and often tedious work. Artisans are masters of their craft, able to create works both practical and beautiful.

```statblock
creature: "Smith"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
