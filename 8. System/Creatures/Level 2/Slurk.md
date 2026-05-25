---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Slurk"
level: "2"
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
    desc: "+6; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +8, Stealth +5"
abilityMods: ["+4", "+2", "+4", "-4", "+0", "+0"]
abilities_top:
  - name: "Entangling Slime"
    desc: "A creature struck by a slurk's slime squirt becomes [[Clumsy]] 1 and takes a –5-foot penalty to Speed for 1 hour or until the slime is removed. <br>  <br> The slime can be removed with a total of three Interact actions by the entangled creature or creatures adjacent to the creature. These actions don't need to be consecutive or made by the same creature. <br>  <br> > [!danger] Effect: Entangling Slime"
armorclass:
  - name: AC
    desc: "17; **Fort** +10, **Ref** +6, **Will** +4"
health:
  - name: HP
    desc: "35"
abilities_mid:
  - name: "+2 to Fortitude Saves vs. Grapple, Reposition, or Shove"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tusks +11 (`pf2:1`) (deadly d10), **Damage** 1d8+4 piercing"
  - name: "Ranged strike"
    desc: "Slime Squirt +9 (`pf2:1`) (range 30 ft.), **Damage**  plus [[Entangling Slime]]"
spellcasting: []
abilities_bot:
  - name: "Belly Grease"
    desc: "`pf2:3` The slurk extrudes a slippery grease from its ventral glands to coat the floor under it and in a @Template[emanation|distance:5], turning the affected area into uneven ground for 10 minutes, after which it dries to a putrid crust. The DC to `act balance dc=18` across the slime is 18."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The slurk is a sticky, tusked frog-beast found in underground lairs and caves. It has two massive tusks that it uses to gore prey and tangle with rival slurks. With the slurk's natural ability to climb walls and cling effortlessly to ceilings, it can be easy for unwary cave explorers to end up on the wrong end of these formidable ivory tusks.

Slurks exude two very different types of foul-smelling secretions from their pale white skin. Large pustules on the slurk's back drip a sticky resin-like slime that quickly hardens upon exposure to air. By flexing its skin, the slurk can burst these pustules in the direction of intruders, covering its foes in sticky goo and severely limiting their ability to withstand the monster's other attacks, including the effects of its other secretion. Glands along the slurk's ventral side excrete an incredibly slippery and fetid grease, which protects the slurk from the immobilizing effects of its own back slime but also has the added benefit of making it extremely difficult to grapple and capture. The best way to discover if a slurk is in the vicinity is to look for hard clumps of such grease, which accumulate and dry in cave corners and amid rock piles where slurks rest between meals.

Slurks are thought to be descendants of a failed dwarven attempt to domesticate and breed large subterranean frogs as food and labor animals. Despite this apparent failure, others who live underground often befriend slurks. The sticky frog-beasts have proven extremely desirable to kobolds (page 210), who now domesticate and train slurks as powerful mounts and guardians. While other creatures, particularly boggards, sometimes train slurks to serve as guardians, kobolds remain those who use these creatures the most. A kobold mounted on a slurk will often hide in the upper ledges of a cave, using the advantages of height and surprise to harry foes with ranged attacks. Kobold riders also take advantage of the slurk's ability to climb, and charge at their enemies from the walls of a cavern.

```statblock
creature: "Slurk"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
