---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rhinoceros"
level: "4"
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
    desc: "+9; [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +12, Survival +10"
abilityMods: ["+6", "+0", "+4", "-4", "+3", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "22; **Fort** +14, **Ref** +8, **Will** +11"
health:
  - name: HP
    desc: "70"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horn +14 (`pf2:1`) (unarmed), **Damage** 2d8+6 piercing"
  - name: "Melee strike"
    desc: "Foot +12 (`pf2:1`) (unarmed), **Damage** 2d6+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Rhinoceros Charge"
    desc: "`pf2:2` The rhinoceros Strides twice, then makes a horn Strike. As long as the rhinoceros moved at least 20 feet, the Strike's damage increases to @Damage[(3d8+6)[piercing]] damage. A Medium or smaller creature struck by this attack must succeed at a DC 21 [[Reflex]] save or be automatically [[Shoved]] back 5 feet and knocked [[Prone]] by the force of the blow."
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, foot, DC 18 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Rhinoceroses are short-tempered, territorial, and easily startled, and these traits combined with their innate ferocity means their natural instinct when disturbed is to attack. When intruders disturb or surprise rhinoceroses, they respond by charging directly at the interlopers and then lashing out with their mighty horns.

This hefty animal is easily recognizable by the distinctive upward-thrusting horn on its snout. Rhinoceroses are herbivorous and, in spite of their hulking size, can run at considerable speed. While rhinos have good hearing and a keen sense of smell, their eyesight is relatively poor.

```statblock
creature: "Rhinoceros"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
