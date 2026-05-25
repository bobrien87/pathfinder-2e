---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Musketeer"
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
    desc: "+10"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +8, Deception +8, Intimidation +10, Stealth +11, Thievery +9"
abilityMods: ["+1", "+4", "+1", "+0", "+1", "+3"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The musketeer deals an extra 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "20; **Fort** +8, **Ref** +11, **Will** +6"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +11 (`pf2:1`) (deadly d8, disarm, finesse), **Damage** 1d6+5 piercing"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
  - name: "Ranged strike"
    desc: "Flintlock Musket +11 (`pf2:1`) (concussive, fatal d10, reload 1, range 70 ft.), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Musketeer's Advance"
    desc: "`pf2:2` **Requirements** The musketeer is wielding a flintlock musket <br>  <br> **Effect** The musketeer makes a flintlock musket Strike. If the Strike hits, the target is [[Off Guard]] to melee attacks by the musketeer until the end of the musketeer's next turn. Regardless of whether the Strike hit, the musketeer then Interacts to swap their flintlock musket for their rapier and Strides toward the creature they attacked."
  - name: "One for All"
    desc: "`pf2:1` **Requirements** The musketeer is wielding a single one-handed weapon in one hand and has their other hand free <br>  <br> **Effect** The musketeer grants a +1 circumstance bonus to AC to themself until the start of their next turn. Allies also gain this bonus while adjacent to the musketeer. If a creature would benefit from more than one creature's One for All ability, the bonus is +2 instead of +1. <br>  <br> > [!danger] Effect: One for All"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Flashy and confident, the musketeer isn't above using dirty tricks to gain the upper hand in a fight. Despite their bravado, musketeers are fiercely loyal to their allies.

These lone wolves have an aura of mystery, bravado, and swagger.

```statblock
creature: "Musketeer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
