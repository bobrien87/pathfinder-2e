---
type: creature
group: ["Humanoid", "Tengu"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jinx Eater"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Tengu"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Low-Light Vision]]"
languages: "Common, Tengu (plus two others)"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +9, Deception +12, Intimidation +12, Occultism +10, Sailing Lore +12"
abilityMods: ["+2", "+4", "+1", "+1", "+1", "+2"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The jinx eater deals 1d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "21; **Fort** +8, **Ref** +14, **Will** +11"
health:
  - name: HP
    desc: "65"
abilities_mid:
  - name: "Eat Fortune"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** A creature within 60 feet uses a fortune or misfortune effect <br>  <br> **Effect** The tengu negates the attempt to manipulate fate and fortune. Eat Fortune gains the opposing trait, and the triggering effect is disrupted."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tengu Gale Blade +13 (`pf2:1`) (agile, disarm, finesse), **Damage** 1d6+4 slashing"
  - name: "Melee strike"
    desc: "Beak +13 (`pf2:1`) (finesse, unarmed), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Jinxed Call"
    desc: "`pf2:2` The jinx eater gives an eerie croak. Each non-tengu in a @Template[type:emanation|distance:30] must succeed at a DC 21 [[Will]] save or be [[Clumsy]] 1 for 1 round (or 1 minute on a critical failure). Regardless of the results, each creature is then temporarily immune to Jinxed Call for 1 minute."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Whether kidnapped, conscripted, or having entered voluntary service, a tengu in the role of jinx eater on a ship's crew is tasked with keeping the crew free of misfortune. Those with the necessary skill to do so often achieve a respected and privileged position on board.

Originally hailing from the continent of Tian Xia, tengu have spread across the globe. Though some staunchly uphold traditions, gazing at the sky from the tallest mountaintops, other tengu remain on the ground, adapting and blending into the societies in which they settle.

```statblock
creature: "Jinx Eater"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
