---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vermin Catcher"
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
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +9, Nature +6, Stealth +8, Survival +6, Vermin Lore +9"
abilityMods: ["+3", "+2", "+4", "+1", "+0", "-2"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The vermin catcher deals an additional 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "17; **Fort** +10, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "35"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +9 (`pf2:1`), **Damage** 1d6+5 bludgeoning"
  - name: "Melee strike"
    desc: "Club +8 (`pf2:1`) (thrown 10), **Damage** 1d6+5 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Giant Rat Trap"
    desc: "`pf2:3` The vermin catcher places a rat trap in an adjacent space. Any Small or Medium creature that moves into the space with the trap triggers it and must attempt a DC 18 [[Reflex]] save. On a failure, the creature takes 1d4 bleed damage (2d4 bleed on a critical failure) and is [[Immobilized]] and [[Off Guard]] for 1 round."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Paid exterminators keep streets and sewers clear of pests like rats, snakes, weasels, and insects—even giant rats.

Society is built upon the backs of laborers.

```statblock
creature: "Vermin Catcher"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
