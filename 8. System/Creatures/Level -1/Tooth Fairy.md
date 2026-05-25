---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tooth Fairy"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: "Fey"
skills:
  - name: Skills
    desc: "Acrobatics +5, Stealth +5, Thievery +6"
abilityMods: ["-2", "+3", "+0", "-1", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +2, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "8; **Weaknesses** cold iron 2"
abilities_mid:
  - name: "Plaque Burst"
    desc: "When killed, a tooth fairy bursts into sticky, foul-smelling white dust. Each creature in a @Template[emanation|distance:5] must succeed at a DC 16 [[Fortitude]] save or become [[Sickened]] 1 ([[Sickened]] 2 on a critical failure)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pliers +7 (`pf2:1`) (disarm, finesse, reach 0 ft.), **Damage** 1d6 bludgeoning plus [[Tooth Tug]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 13, attack +5<br>**1st** [[Sleep]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Tooth Tug"
    desc: "`pf2:1` **Requirements** The tooth fairy's last action was a successful pliers Strike against a creature with teeth <br>  <br> **Effect** The tooth fairy attempts a [[Thievery]] check against the creature's Fortitude DC, dealing 2 bleed damage on any result but a critical failure. On a critical success, it also pulls out one of the target's teeth. <br>  <br> If the creature loses a tooth, it takes a –1 status penalty to Charisma-based skill checks and must succeed at a DC 5 flat check to Cast a Spell unless that spell has the subtle trait. These effects last for 1 day, or until the stolen tooth is returned and the target regains at least 1 Hit Point. <br>  <br> > [!danger] Effect: Tooth Tug"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Lone fairies usually need several minutes of elbow grease and a sleeping or restrained subject to extract a tooth.

Tooth fairies spawn when a child's tooth (or, less commonly, an entire child) is buried in terrain rife with fey energies. Hatching from the buried teeth like larvae from an egg, tooth fairies build crude pliers from whatever they can find, then go hunting for more teeth—regardless of the owners' willingness.

```statblock
creature: "Tooth Fairy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
