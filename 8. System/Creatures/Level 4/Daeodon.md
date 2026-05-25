---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Daeodon"
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
    desc: "+12; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +12, Survival +10"
abilityMods: ["+6", "+0", "+3", "-4", "+2", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +13, **Ref** +9, **Will** +10"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tusk +14 (`pf2:1`) (unarmed), **Damage** 2d8+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Daeodon Charge"
    desc: "`pf2:2` The daeodon Strides twice and then makes a tusk Strike. As long as it moved at least 20 feet, it gains a +2 circumstance bonus to its attack roll. A Medium or smaller creature struck by this attack must succeed at a DC 19 [[Reflex]] save or be knocked [[Prone]] by the force of the blow."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Where the typical boar is merely ill-tempered and generally unfriendly, the towering daeodon is legitimately hateful and ruthlessly violent. Although omnivorous, the daeodon (known in some regions simply as a giant boar) prefers to feed on flesh. While it is primarily a scavenger, the daeodon isn't adverse to attacking creatures it encounters while searching for easier meals, or to protect any perceived encroachment into its lair or feeding grounds. Particularly brave or skilled orcs are fond of using daeodons as mounts or war-trained battle beasts; orc cavalry mounted on daeodons is a fearsome force indeed.

A typical adult daeodon is 10 feet long and 7 feet tall at the shoulder. It weighs approximately 2,000 pounds.

While domesticated pigs are a staple of farm life, wild boars are much more dangerous. Foul-tempered warthogs are relatively common, while the lumbering, primeval beasts known as daeodons are less so. Voracious boars can ravage the countryside in which they live, making them a particular nuisance to farmers. Boars breed freely, and a pair of boars can rapidly grow to a large family.

```statblock
creature: "Daeodon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
