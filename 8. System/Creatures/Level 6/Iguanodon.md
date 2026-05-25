---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Iguanodon"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +15"
abilityMods: ["+7", "+4", "+4", "-4", "+4", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24; **Fort** +16, **Ref** +12, **Will** +14"
health:
  - name: HP
    desc: "95"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Thumb Spike +17 (`pf2:1`) (deadly d10, reach 10 ft.), **Damage** 2d8+9 piercing"
  - name: "Melee strike"
    desc: "Tail +15 (`pf2:1`) (reach 15 ft.), **Damage** 2d10+9 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Gouging Lunge"
    desc: "`pf2:2` The iguanodon makes a thumb spike Strike at an adjacent foe and then Strides up to 15 feet, dragging its thumb spike across the foe to gouge out a brutal wound. If this Strike hits, it deals an extra 1d8 slashing damage and the following Stride does not trigger reactions from the creature struck. This thumb spike Strike counts as two attacks when calculating the iguanodon's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Iguanodons are large, herbivorous dinosaurs that inhabit swamps and forests where they browse on the abundant vegetation. The iguanodon is capable of moving on two feet or on four, quickly switching from one stance to the other depending on whether it needs to move through dense foliage or to reach delectable morsels hanging up in the canopy.

Although iguanodons are herbivores, they are notoriously quick to anger. Their thumb spikes make their claws particularly devastating weapons. A well-placed blow from one of these claws can turn a hungry predator into a cowering beast with one swift strike. Iguanodons are 30 feet long and weigh 6,000 pounds.

```statblock
creature: "Iguanodon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
