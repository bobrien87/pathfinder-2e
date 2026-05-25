---
type: creature
group: ["Beast", "Cold"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Witchwarg"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Cold"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common, Jotun"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +13, Deception +11, Intimidation +11, Stealth +13, Survival +12"
abilityMods: ["+6", "+4", "+4", "+2", "+3", "+2"]
abilities_top:
  - name: "Pack Attack"
    desc: "The witchwarg's Strikes deal 1d6 extra damage to creatures within the reach of at least two of the witchwarg's allies."
armorclass:
  - name: AC
    desc: "23; **Fort** +13, **Ref** +15, **Will** +10"
health:
  - name: HP
    desc: "70; **Immunities** cold; **Weaknesses** fire 5"
abilities_mid:
  - name: "Avenging Bite"
    desc: "`pf2:r` **Trigger** A creature within reach of the witchwarg's jaws attacks one of the witchwarg's allies. <br>  <br> **Effect** The witchwarg makes a jaws Strike against the triggering creature."
  - name: "Buck"
    desc: "`pf2:r` DC 21 [[Reflex]] save <br>  <br> Most monsters that serve as mounts can attempt to buck off unwanted or annoying riders, but most mounts will not use this reaction against a trusted creature unless the mounts are spooked or mistreated. <br>  <br> **Trigger** A creature [[Mounts]] or uses the [[Command an Animal]] action while riding the monster. <br>  <br> **Effect** The triggering creature must succeed at a Reflex saving throw against the listed DC or fall off the creature and land [[Prone]]. If the save is a critical failure, the triggering creature also takes 1d6 bludgeoning damage in addition to the normal damage for the fall."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +15 (`pf2:1`) (cold, unarmed), **Damage** 1d10+6 piercing plus 1d6 cold plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Winter Breath"
    desc: "`pf2:2` The witchwarg breathes a cloud of frost in a @Template[cone|distance:15] that deals @Damage[5d8[cold]|options:area-damage] damage (DC 23 [[Reflex]] save). <br>  <br> The witchwarg can't use Winter Breath again for 1d4 rounds."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Witchwargs are related to wargs, but are larger, smarter, and far more dangerous. They are capable of exhaling plumes of freezing breath. When they deign to serve others, they usually reserve this privilege for more dangerous creatures, such as the winter witches of Irrisen.

The warg is an intelligent and malevolent wolf that dwells among goblins, hobgoblins, orcs, and violent humanoids.

```statblock
creature: "Witchwarg"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
