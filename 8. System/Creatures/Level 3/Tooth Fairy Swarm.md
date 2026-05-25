---
type: creature
group: ["Fey", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tooth Fairy Swarm"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Fey"
trait_02: "Swarm"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +10, Stealth +10, Thievery +12"
abilityMods: ["-2", "+3", "+0", "-1", "+2", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +5, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "28; **Immunities** precision, swarm mind; **Weaknesses** area damage 5, cold iron 5, splash damage 5; **Resistances** bludgeoning 2, piercing 5, slashing 5"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
  - name: "Plaque Burst"
    desc: "When killed, a tooth fairy swarm bursts into sticky, foul-smelling white dust. Each creature in a @Template[emanation|distance:15] must succeed at a DC 20 [[Fortitude]] save or become [[Sickened]] 1 ([[Sickened]] 2 on a critical failure)."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Pinch"
    desc: "`pf2:1` Tooth fairies pinch their victims' fingers, noses, ears, or similar protruding body parts. Each enemy in the swarm's space takes 2d6 bludgeoning damage (DC 20 [[Reflex]] save). Creatures that critically fail this save are [[Sickened]] 1 from the pain."
  - name: "Pry"
    desc: "`pf2:3` The tooth fairies try to pry out one of their target's teeth. One enemy in the swarm's space takes 4d6 bludgeoning damage with a DC 20 [[Reflex]] save. On a failed save, the target takes 2 bleed damage and loses a tooth. <br>  <br> If the creature loses a tooth, it takes a –1 status penalty to Charisma-based skill checks and must succeed at a DC 5 flat check to Cast a Spell unless that spell has the subtle trait. These effects last for 1 day, or until the stolen tooth is returned and the target regains at least 1 Hit Point. <br>  <br> > [!danger] Effect: Tooth Tug"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A mob of tooth fairies working together can conduct forced dentistry in seconds.

Tooth fairies spawn when a child's tooth (or, less commonly, an entire child) is buried in terrain rife with fey energies. Hatching from the buried teeth like larvae from an egg, tooth fairies build crude pliers from whatever they can find, then go hunting for more teeth—regardless of the owners' willingness.

```statblock
creature: "Tooth Fairy Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
