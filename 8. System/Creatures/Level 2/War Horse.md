---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "War Horse"
level: "2"
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
    desc: "+6; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +11"
abilityMods: ["+5", "+3", "+4", "-4", "+2", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +7, **Will** +6"
health:
  - name: HP
    desc: "36"
abilities_mid:
  - name: "Buck"
    desc: "`pf2:r` DC 17 [[Reflex]] save <br>  <br> Most monsters that serve as mounts can attempt to buck off unwanted or annoying riders, but most mounts will not use this reaction against a trusted creature unless the mounts are spooked or mistreated. <br>  <br> **Trigger** A creature [[Mounts]] or uses the [[Command an Animal]] action while riding the monster. <br>  <br> **Effect** The triggering creature must succeed at a Reflex saving throw against the listed DC or fall off the creature and land [[Prone]]. If the save is a critical failure, the triggering creature also takes 1d6 bludgeoning damage in addition to the normal damage for the fall."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hoof +9 (`pf2:1`), **Damage** 1d6+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Gallop"
    desc: "`pf2:2` The war horse Strides twice. It has a +10-foot circumstance bonus to its Speed during these Strides."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Horses serve as mounts and beasts of burden in many societies. They are loyal and typically gentle creatures, and they are invaluable to those looking to travel long distances. Smaller folk, like gnomes and halflings, often utilize ponies as mounts, while horses are the favored steeds for humans and other Medium humanoids. Most horses that the average humanoid encounters are domesticated, though large herds can be found in the wild.

```statblock
creature: "War Horse"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
