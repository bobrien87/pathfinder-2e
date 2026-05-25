---
type: creature
group: ["Beast", "Eidolon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Beast Eidolon"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Beast"
trait_02: "Eidolon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]], [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: "Fey"
skills:
  - name: Skills
    desc: "Acrobatics +16, Athletics +21, Intimidation +22, Nature +15"
abilityMods: ["+5", "+2", "+4", "-1", "+3", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "29; **Fort** +19, **Ref** +18, **Will** +19"
health:
  - name: HP
    desc: "180; **Resistances** cold 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horn +22 (`pf2:1`) (unarmed), **Damage** 2d8+11 piercing plus 1d6 bleed plus [[Grab]]"
  - name: "Melee strike"
    desc: "Hoof +22 (`pf2:1`) (agile, unarmed), **Damage** 2d6+11 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Furious Charge"
    desc: "`pf2:2` The eidolon Strides twice and then makes a Strike. As long as it moved at least 20 feet, it gains a +2 circumstance bonus to the attack roll."
  - name: "Primal Roar"
    desc: "`pf2:2` The eidolon attempts to [[Demoralize]] each enemy within 30 feet; these Demoralize attempts don't take any penalty for not sharing a language."
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

This creature is intended to be used as the eidolon accompanying a Sarkorian god caller, but it can be used or adapted into any aggressive beast eidolon for a summoner.

```statblock
creature: "Beast Eidolon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
