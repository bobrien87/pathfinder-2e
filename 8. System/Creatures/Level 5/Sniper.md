---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sniper"
level: "5"
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
    desc: "+15"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +11, Medicine +11, Stealth +15, Survival +11"
abilityMods: ["+2", "+4", "+1", "+1", "+4", "+0"]
abilities_top:
  - name: "Silencer"
    desc: "A [[Silencer]] is an uncommon item worth 1 sp. It has light Bulk and can be attached to a firearm in 1 minute; the sniper typically already has one attached before going into combat. The first time a shot is fired through it, the silencer is consumed and reduces the report to a quiet noise. A silencer doesn't work on scatter firearms."
  - name: "Sniper's Edge"
    desc: "The sniper's ranged Strikes deal 2d6 extra precision damage to [[Off Guard]] creatures."
  - name: "Surprise Attack"
    desc: "All enemy creatures that have not yet acted in combat are [[Off Guard]] to the sniper."
armorclass:
  - name: AC
    desc: "21; **Fort** +10, **Ref** +15, **Will** +11"
health:
  - name: HP
    desc: "65"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +15 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+8 piercing"
  - name: "Melee strike"
    desc: "Dagger +15 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+8 piercing"
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
  - name: "Ranged strike"
    desc: "Arquebus +15 (`pf2:1`) (concussive, fatal d12, kickback, reload 1, range 150 ft.), **Damage** 1d8+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Concussive Shot"
    desc: "`pf2:2` The sniper makes an arquebus Strike against a creature within the weapon's first range increment. On a success, the creature must succeed at a DC 21 [[Fortitude]] save or be [[Stunned]] 1 ([[Stunned]] 2 on a critical failure)."
  - name: "Full Bore"
    desc: "`pf2:2` The sniper makes an arquebus Strike against two creatures that are adjacent to each other. The attack ignores any lesser cover one target provides the other. Roll damage once, and apply it to each creature the sniper hits. This counts as two attacks when determining the sniper's multiple attack penalty."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A keen eye, a steady hand, and a killer instinct combine to form a ruthless, emotionless harbinger of death. A sniper usually works alone, though they're occasionally seen alongside a spotter or as part of a larger squad.

A military serves to defend and fight on behalf of nations and can be trained and deployed in various ways.

```statblock
creature: "Sniper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
