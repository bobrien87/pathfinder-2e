---
type: creature
group: ["Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Scarecrow"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Construct"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +12"
abilityMods: ["+5", "+2", "+3", "-4", "+3", "-2"]
abilities_top:
  - name: "Clawing Fear"
    desc: "The scarecrow's strikes deal an additional 1d6 mental damage to [[Frightened]] creatures."
armorclass:
  - name: AC
    desc: "19; **Fort** +13, **Ref** +8, **Will** +11"
health:
  - name: HP
    desc: "60; **Immunities** fear effects; **Weaknesses** fire 5; **Resistances** physical 5 except slashing"
abilities_mid:
  - name: "Scarecrow's Leer"
    desc: "40 feet. <br>  <br> The scarecrow's eyes flicker with an unnerving glow. A creature can't reduce its [[Frightened]] condition below 1 as long as it is in the aura's emanation. When a creature enters or starts its turn in the aura, it must attempt a DC 18 [[Will]] save. Birds and other avian creatures take a -2 circumstance penalty to this save. <br> - **Critical Success** The creature is unaffected and is then temporarily immune for 24 hours. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2 and is [[Fascinated]] by the scarecrow until the end of its next turn. <br> - **Critical Failure** As failure, but [[Frightened]] 3."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +13 (`pf2:1`) (unarmed, versatile s), **Damage** 2d6+7 bludgeoning plus [[Clawing Fear]]"
spellcasting: []
abilities_bot:
  - name: "Baleful Glow"
    desc: "`pf2:0` The scarecrow's head bursts into ghostly, heatless flame that sheds bright light in a @Template[emanation|distance:20] (and dim light to the next 20 feet). If the scarecrow uses this ability on the first round of combat, any creature that has not acted yet is startled and becomes [[Off Guard]] against the scarecrow for 1 round. It can suppress the light by using this action again."
  - name: "Mundane Appearance"
    desc: "`pf2:1` Until it acts, the scarecrow resembles an ordinary scarecrow. It has an automatic result of 32 on Deception checks and DCs to pass as an ordinary scarecrow."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A ramshackle collection of materials in a human shape, the scarecrow construct is indistinguishable from a normal scarecrow until it slowly creaks to life. As it animates, its carved pumpkin or sackcloth face bursts into eldritch flame, sending fear creeping into the air around it. Each scarecrow is handcrafted and unique in its appearance, though most are 5 to 6 feet tall and constructed of a combination of wood, cloth, rope, straw, sawdust, discarded husks and cobs, and similar materials, all dressed in ragged pastoral garments. This rudimentary construction makes a scarecrow somewhat fragile, prone to snapping limbs in the crush of battle. Yet its structure is adaptable, allowing it to reshape another piece of itself into a clawed limb or grip a severed portion of itself to swat at its foes.

When a scarecrow is created, it must be anointed with a drop of its creator's blood into each of its eyes. This blood soaks into the material and siphons a tiny sliver of the creator's soul away—not enough to harm the creator, but more than enough to imbue the scarecrow with an instinctive intellect that allows it to follow commands as eagerly as a well-trained (if ill-tempered) guard dog. When a scarecrow is destroyed, the blood leaks back out from its eyes, but the portion of the creator's soul never returns.

```statblock
creature: "Scarecrow"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
