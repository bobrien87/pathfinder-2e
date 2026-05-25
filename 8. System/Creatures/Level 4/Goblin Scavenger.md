---
type: creature
group: ["Goblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Goblin Scavenger"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Crafting +12, Society +8, Stealth +11, Survival +10, Thievery +9"
abilityMods: ["+1", "+3", "+2", "+2", "+3", "+0"]
abilities_top:
  - name: "Big Boom Gun"
    desc: "The scavenger's gun is a comically oversized hand cannon that has the fatal d12 trait and a 20-foot range increment. If a Strike with it critically fails, the weapon misfires and explodes, dealing 1d12 fire damage to its wielder. It's a martial one-handed weapon with 2 Bulk and a Price of 10 gp. It has the uncommon, cobbled, and goblin traits. The cobbled trait means that on a failed attack roll with the gun, the user must succeed at a DC 5 flat check or the weapon misfires."
  - name: "One Person's Junk"
    desc: "The goblin scavenger intuitively knows how to make use of junk. When they use a weapon with the goblin trait or an improvised weapon, they do an additional die of damage (already included in the Strikes above)."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +11, **Will** +13"
health:
  - name: HP
    desc: "70"
abilities_mid:
  - name: "Finders Keepers"
    desc: "`pf2:r` **Trigger** A creature within 15 feet drops an item <br>  <br> **Requirements** The goblin scavenger has a hand free <br>  <br> **Effect** The goblin scavenger Strides up to their speed to an adjacent square and Interacts to pick up the item. The movement triggers reactions as normal, but the Interact action to pick up the item does not."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dogslicer +12 (`pf2:1`) (agile, backstabber, finesse), **Damage** 2d6+3 slashing"
  - name: "Melee strike"
    desc: "Jaws +12 (`pf2:1`) (unarmed), **Damage** 1d8+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Big Boom Gun +14 (`pf2:1`) (cobbled, fatal d12, modular, reload 1, range 20 ft.), **Damage** 2d6+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Fireworks Barrage"
    desc: "`pf2:2` **Requirements** The goblin scavenger has a free hand <br>  <br> **Effect** The goblin scavenger draws a bundle of fireworks and launches them toward a point within 60 feet, where they explode, dealing @Damage[1d10[fire],1d10[sonic]|options:area-damage] damage in a @Template[type:burst|distance:10]. Every creature in the area must attempt a DC 21 [[Reflex]] save. <br> - **Critical Success** The creature is unaffected. The goblin scavenger realizes that's because a firework fell at their feet and takes 2 fire damage when it explodes in their face. <br> - **Success** The creature takes half damage. <br> - **Failure** The creature takes full damage and is [[Dazzled]] and [[Deafened]] for 1 round. <br> - **Critical Failure** As failure, except the creature is also [[Stunned]] 1."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Many goblins scavenge materials, shiny objects, and anything else they can get their hands on, but a goblin scavenger is the best at finding such useful items. More importantly, they're great at making use of them without killing themselves. Most of the time.

Goblins can be found across Golarion, sometimes threatening taller humanoids (whom they refer to as "longshanks") and sometimes redeeming harmful history by working alongside others.

```statblock
creature: "Goblin Scavenger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
