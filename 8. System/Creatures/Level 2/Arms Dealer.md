---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Arms Dealer"
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
    desc: "Crafting +7, Deception +7, Diplomacy +7, Intimidation +9, Society +9, Firearm Lore +14, Underworld Lore +9"
abilityMods: ["+0", "+3", "+0", "+1", "+3", "+3"]
abilities_top:
  - name: "Arms Dealing Specialist"
    desc: "For encounters involving the purchase of weapons, the arms dealer is a 5th-level challenge."
  - name: "You Call That a Gun?"
    desc: "The arms dealer seems unaffected by your attempts to threaten them. The arms dealer gains a +2 circumstance bonus to their Will DC against Intimidation checks while they're holding a firearm."
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +7, **Will** +9"
health:
  - name: HP
    desc: "28"
abilities_mid:
  - name: "+2 to Sense Motive"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sword Cane +9 (`pf2:1`) (agile, concealable, finesse), **Damage** 1d6+2 piercing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Flintlock Musket +11 (`pf2:1`) (concussive, fatal d10, reload 1, range 70 ft.), **Damage** 1d6+3 piercing"
  - name: "Ranged strike"
    desc: "Hand Cannon +11 (`pf2:1`) (modular, reload 1, range 30 ft.), **Damage** 1d6+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Take Stock"
    desc: "`pf2:1` The arms dealer advises an ally on how to properly use a firearm. The arms dealer chooses an ally within 30 feet wielding a firearm. That ally can use a reaction to Interact to reload their firearm."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A seedy arms dealer has access to all kinds of deadly weapons and can quickly provide them to clients in need… for the right price, of course.

These lone wolves have an aura of mystery, bravado, and swagger.

```statblock
creature: "Arms Dealer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
