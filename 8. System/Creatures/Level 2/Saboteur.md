---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Saboteur"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +5, Crafting +6, Deception +7, Diplomacy +5, Intimidation +5, Society +6, Stealth +9, Survival +6, Thievery +9, Engineering Lore +8, Underworld Lore +6"
abilityMods: ["+1", "+3", "+1", "+2", "+2", "+1"]
abilities_top:
  - name: "Snare Crafting"
    desc: "The saboteur can Craft snares and has the supplies to make up to two Caltrop Snares and up to two Hampering Snares."
  - name: "Sneak Attack"
    desc: "The saboteur deals an extra 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "17 (19 vs. traps); **Fort** +5, **Ref** +9 (+11 vs. traps), **Will** +8"
health:
  - name: HP
    desc: "28"
abilities_mid:
  - name: "Perception +10 to Find Traps"
    desc: ""
  - name: "Reflex +11 and AC 19 vs. Traps"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sap +7 (`pf2:1`) (agile, nonlethal), **Damage** 1d6+3 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +9 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Saboteurs excel at infiltration, using it to perform destructive acts.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Saboteur"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
