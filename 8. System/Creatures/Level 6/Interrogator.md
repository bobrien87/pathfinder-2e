---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Interrogator"
level: "6"
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
    desc: "+13"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +15, Intimidation +13, Medicine +13"
abilityMods: ["+4", "+3", "+1", "+0", "+2", "+2"]
abilities_top:
  - name: "Torment"
    desc: "The interrogator's Strikes deal an additional 1d8 mental damage to [[Frightened]] creatures."
armorclass:
  - name: AC
    desc: "22; **Fort** +12, **Ref** +12, **Will** +11"
health:
  - name: HP
    desc: "90"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dart +15 (`pf2:1`) (agile, thrown 20), **Damage** 1d4+7 piercing plus [[Torment]]"
  - name: "Melee strike"
    desc: "War Razor +17 (`pf2:1`) (agile, backstabber, deadly d8, finesse, magical), **Damage** 1d4+10 slashing plus [[Torment]]"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning plus [[Torment]]"
spellcasting: []
abilities_bot:
  - name: "Blood and Fear"
    desc: "`pf2:2` The interrogator Strikes with a slashing melee weapon. If they hit and deal damage, the target takes an additional 1d4 persistent bleed damage and is [[Frightened]] 1 (or 2d4 persistent bleed damage and [[Frightened]] 2 on a critical hit). <br>  <br> Each of the interrogator's other enemies in a @Template[type:emanation|distance:30] around the target that witnesses the bloodshed must succeed at a DC 19 [[Will]] save or be frightened 1. The frightened part of this ability is an emotion, fear, mental, and visual effect."
  - name: "Hobble"
    desc: "`pf2:1` **Requirements** A creature is [[Grabbed]] or [[Restrained]] by the interrogator <br>  <br> **Effect** One creature grabbed or restrained by the interrogator takes 2d6 bludgeoning damage with a DC 23 [[Fortitude]] save. If the creature fails its save, it also gains a condition of the interrogator's choice: [[Clumsy]] 2 for 1 minute, [[Enfeebled]] 2 for 1 minute, or [[Drained]] 1."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Interrogators use pain and intimidation against prisoners and other helpless victims to force "confessions."

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Interrogator"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
