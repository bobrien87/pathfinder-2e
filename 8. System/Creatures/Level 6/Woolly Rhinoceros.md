---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Woolly Rhinoceros"
level: "6"
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
    desc: "+11; [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +16, Survival +13"
abilityMods: ["+6", "+1", "+5", "-4", "+3", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "25; **Fort** +17, **Ref** +11, **Will** +15"
health:
  - name: HP
    desc: "100"
abilities_mid:
  - name: "+2 Status to All Saves vs. Cold"
    desc: ""
  - name: "Cold Adaptation"
    desc: "The woolly rhinoceros treats environmental cold effects as if they were one step less extreme."
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horn +16 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d12+6 piercing"
  - name: "Melee strike"
    desc: "Foot +16 (`pf2:1`) (unarmed), **Damage** 2d8+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Rhinoceros Charge"
    desc: "`pf2:2` The woolly rhinoceros Strides twice, then makes a horn Strike. As long as the woolly rhinoceros moved at least 20 feet, the Strike's damage increases to @Damage[(3d12+6)[piercing]] damage. A Medium or smaller creature struck by this attack must succeed at a DC 24 [[Reflex]] save or be automatically [[Shoved]] back 5 feet and knocked [[Prone]] by the force of the blow."
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, foot, DC 21 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Even bulkier than their non-woolly cousins, these rhinoceroses have a shaggy pelt of long, thick fur and a huge, crescent-shaped horn. Woolly rhinos inhabit areas of arid tundra and cold steppes, spending much of their day grazing for sustenance.

This hefty animal is easily recognizable by the distinctive upward-thrusting horn on its snout. Rhinoceroses are herbivorous and, in spite of their hulking size, can run at considerable speed. While rhinos have good hearing and a keen sense of smell, their eyesight is relatively poor.

```statblock
creature: "Woolly Rhinoceros"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
