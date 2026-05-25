---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Veteran War Horse"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +15, Intimidation +12"
abilityMods: ["+6", "+3", "+4", "-4", "+2", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +12, **Ref** +11, **Will** +10"
health:
  - name: HP
    desc: "90"
abilities_mid:
  - name: "Buck"
    desc: "`pf2:r` DC 21 [[Reflex]] save <br>  <br> Most monsters that serve as mounts can attempt to buck off unwanted or annoying riders, but most mounts will not use this reaction against a trusted creature unless the mounts are spooked or mistreated. <br>  <br> **Trigger** A creature [[Mounts]] or uses the [[Command an Animal]] action while riding the monster. <br>  <br> **Effect** The triggering creature must succeed at a Reflex saving throw against the listed DC or fall off the creature and land [[Prone]]. If the save is a critical failure, the triggering creature also takes 1d6 bludgeoning damage in addition to the normal damage for the fall."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hoof +13 (`pf2:1`) (unarmed), **Damage** 2d6+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Gallop"
    desc: "`pf2:2` The veteran war horse Strides twice. It has a +10-foot circumstance bonus to its Speed during these Strides."
  - name: "Into the Fray"
    desc: "`pf2:1` The veteran war horse Strides then Demoralizes an adjacent Medium or smaller creature. When it does, Demoralize loses the auditory trait and gains the visual trait, and it doesn't take a penalty for the veteran war horse not speaking a language."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A veteran war horse has not only been extensively trained but has also experienced battle several times. They have grown used to the chaos of war and fearlessly strides forward, striking fear into their enemies. A veteran war horse could accompany a champion, champion of Rovagug, captain of the guard, deific champion, equestrian constable, or orc gamekeeper.

```statblock
creature: "Veteran War Horse"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
