---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Terror Shrike"
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
    desc: "+11; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +12"
abilityMods: ["+5", "+4", "+3", "-4", "+1", "+0"]
abilities_top:
  - name: "Tearing Clutch"
    desc: "The terror shrike's powerful beak can tear through flesh. On a successful beak Strike, the target takes 1 persistent bleed damage. This bleed damage increases to 1d8 on a critical hit."
armorclass:
  - name: AC
    desc: "20; **Fort** +13, **Ref** +12, **Will** +7"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +12 (`pf2:1`) (reach 10 ft.), **Damage** 2d8+5 piercing plus [[Tearing Clutch]]"
  - name: "Melee strike"
    desc: "Talon +12 (`pf2:1`) (agile), **Damage** 2d6+5 piercing plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Sprint"
    desc: "`pf2:2` **Frequency** once per minute <br>  <br> **Effect** The terror shrike Strides three times in a straight line"
  - name: "Stunning Screech"
    desc: "`pf2:1` The terror shrike unleashes a haunting screech that causes prey to freeze in fear. Each non–terror bird creature in a @Template[type:emanation|distance:30] must attempt a DC 19 [[Will]] save. Regardless of the result, creatures are then temporarily immune for 1 minute. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature is [[Stunned]] 1. <br> - **Critical Failure** The creature is [[Stunned]] 2."
  - name: "Sudden Charge"
    desc: "`pf2:2` The terror shrike Strides twice. If it ends its movement within melee reach of one creature, it can make a melee Strike against that creature."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`



```statblock
creature: "Terror Shrike"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
