---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Runaway Blueblood"
level: "3"
rare_01: "Uncommon"
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
    desc: "Deception +9, Diplomacy +9, Society +11, Genealogy Lore +9"
abilityMods: ["+1", "+3", "+0", "+2", "+0", "+4"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The runaway blueblood deals an extra 1d6 damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "18; **Fort** +7, **Ref** +10, **Will** +9"
health:
  - name: HP
    desc: "45"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+5 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
  - name: "Ranged strike"
    desc: "Dueling Pistol +10 (`pf2:1`) (concealable, concussive, fatal d10, reload 1, range 60 ft.), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "\"Courageous\" Retreat"
    desc: "`pf2:1` **Requirements** The runaway blueblood is adjacent to at least one enemy <br>  <br> **Effect** The runaway blueblood gains the [[Fleeing]] condition, gains a +5-foot status bonus to their Speed, and gains a +2 circumstance bonus to their AC against reactions triggered by their movement. The blueblood Strides. The effects last until the end of the blueblood's current turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Dissatisfied with their privileged upbringing, the runaway blueblood has left the life of luxury behind to forge a new path for themself.

These lone wolves have an aura of mystery, bravado, and swagger.

```statblock
creature: "Runaway Blueblood"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
