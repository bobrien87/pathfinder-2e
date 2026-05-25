---
type: creature
group: ["Mindless", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kugaptee's Blessing"
level: "2"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Zombie"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +11"
abilityMods: ["+5", "-3", "+4", "-5", "+0", "-2"]
abilities_top:
  - name: "Slow"
    desc: "A zombie is permanently [[Slowed]] 1 and can't use reactions."
armorclass:
  - name: AC
    desc: "15; **Fort** +10, **Ref** +3, **Will** +6"
health:
  - name: HP
    desc: "70; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Weaknesses** vitality 10, slashing 10"
abilities_mid:
  - name: "Improved Push"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Improved Push lists a distance, change the distance the creature is pushed on a success to that distance."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 1d12+5 bludgeoning plus [[Improved Push]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Necromantic augmentations have granted this zombie increased size and power.

A zombie's only desire is to consume the living. Unthinking and ever-shambling harbingers of death, zombies stop only when they're destroyed.

```statblock
creature: "Kugaptee's Blessing"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
