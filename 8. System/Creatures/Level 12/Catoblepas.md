---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Catoblepas"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: "Aklo"
skills:
  - name: Skills
    desc: "Athletics +25, Intimidation +20, Stealth +22, Survival +20"
abilityMods: ["+7", "+4", "+6", "-2", "+4", "+2"]
abilities_top:
  - name: "Stench"
    desc: "30 feet. A creature entering the aura or starting its turn in the aura must succeed at a DC 30 [[Fortitude]] save or become [[Sickened]] 1 (plus [[Slowed]] 1 for as long as it's sickened on a critical failure). <br>  <br> While within the aura, affected creatures take a -2 circumstance penalty to saves against disease and to recover from the sickened condition. A creature that succeeds at its save is temporarily immune for 1 minute. <br>  <br> > [!danger] Effect: Stench"
armorclass:
  - name: AC
    desc: "33; **Fort** +24, **Ref** +20, **Will** +22"
health:
  - name: HP
    desc: "215; **Immunities** disease, poison, olfactory"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +25 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 3d10+13 piercing"
  - name: "Melee strike"
    desc: "Antler +25 (`pf2:1`) (magical, reach 15 ft.), **Damage** 3d12+13 piercing"
  - name: "Melee strike"
    desc: "Hoof +23 (`pf2:1`) (magical), **Damage** 3d10+11 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Poison Breath"
    desc: "`pf2:2` The catoblepas breathes a @Template[cone|distance:60] of horrid fumes, dealing @Damage[13d6[poison]|options:area-damage] damage (DC 32 [[Fortitude]] save). The area of this cone is reduced to @Template[cone|distance:30]{30 feet} underwater. Targets that fail their saving throw also become [[Sickened]] 1 ([[Sickened]] 2 on a critical failure). <br>  <br> The catoblepas can't use its Poison Breath again for 1d4 rounds."
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, hoof, DC 32 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The catoblepas is an aggressive beast at the best of times. Though it prefers swamps, the catoblepas has been know to forage in plains and forests for short periods, leaving behind hunting grounds tainted by its foul breath and noxious waste that other predators and prey alike avoid for days or even weeks thereafter. The catoblepas bullies those creatures it believes are a match for it, and eats everything weaker.

A catoblepas is 15 feet long and weighs 2,200 pounds.

```statblock
creature: "Catoblepas"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
