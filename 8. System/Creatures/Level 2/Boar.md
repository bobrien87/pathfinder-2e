---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Boar"
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
    desc: "+8; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +8, Survival +8"
abilityMods: ["+4", "+1", "+4", "-4", "+2", "-3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +10, **Ref** +5, **Will** +8"
health:
  - name: HP
    desc: "40"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tusk +10 (`pf2:1`) (unarmed), **Damage** 2d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Boar Charge"
    desc: "`pf2:2` The boar Strides twice and then makes a tusk Strike. As long as it moved at least 20 feet, it gains a +2 circumstance bonus to its attack roll."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Boars are omnivorous mammals, hunted heavily because their meat is considered a delicacy. Boars are most likely to attack humanoids either in self-defense or during their mating season in the winter months, when the males grow an extra inch of tissue to protect their organs as they fight off rivals. Of course, in some cultures, boars are trained to become much more aggressive so they can fill the roles of warbeast and guardian. When such boars escape back into the wild, they can become true terrors in the region.

While domesticated pigs are a staple of farm life, wild boars are much more dangerous. Foul-tempered warthogs are relatively common, while the lumbering, primeval beasts known as daeodons are less so. Voracious boars can ravage the countryside in which they live, making them a particular nuisance to farmers. Boars breed freely, and a pair of boars can rapidly grow to a large family.

```statblock
creature: "Boar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
