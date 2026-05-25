---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Riding Dog"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +7, Survival +5"
abilityMods: ["+2", "+2", "+2", "-4", "+2", "-1"]
abilities_top:
  - name: "Pack Attack"
    desc: "The dog's Strikes deal 1d4 extra damage to creatures within the reach of at least two of the dog's allies."
armorclass:
  - name: AC
    desc: "16; **Fort** +7, **Ref** +5, **Will** +5"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Buck"
    desc: "`pf2:r` DC 17 [[Reflex]] save <br>  <br> Most monsters that serve as mounts can attempt to buck off unwanted or annoying riders, but most mounts will not use this reaction against a trusted creature unless the mounts are spooked or mistreated. <br>  <br> **Trigger** A creature [[Mounts]] or uses the [[Command an Animal]] action while riding the monster. <br>  <br> **Effect** The triggering creature must succeed at a Reflex saving throw against the listed DC or fall off the creature and land [[Prone]]. If the save is a critical failure, the triggering creature also takes 1d6 bludgeoning damage in addition to the normal damage for the fall."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`) (unarmed), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Riding dogs types include larger dogs, such as mastiffs, wolfhounds, and huskies, and are bred often by halflings and gnomes to serve as mounts. Riding dogs are as loyal and devoted to their masters as guard dogs and ferocious in battle, regardless of whether they bear a rider or not. As with guard dogs, these large hounds can be wild or feral in nature, and in such cases might rival wolf packs in the danger they pose to inhabitants of rural areas.

Dogs are trusted and loyal companions that serve as guardians, tracking animals, and pets. Their ability to detect prey or predators via scent and their predilection to accompany humanoids makes them ideal pets for most adventurers. There are hundreds of breeds of dogs in the world—from tiny lapdogs who shower their masters in affection to brawny hounds that stand nearly 4 feet high at the shoulder—and they can be found in nearly any place where people reside. Larger breeds might even be used as mounts for smaller adventurers, and some cultures use dogs as beasts of burden capable of pulling sleds loaded with supplies across the icy tundra. Regardless, many adventurers find value in having a dog.

```statblock
creature: "Riding Dog"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
