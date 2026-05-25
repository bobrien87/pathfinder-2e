---
type: creature
group: ["Mindless", "Skeleton"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skeletal Hulk"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +20, Intimidation +15"
abilityMods: ["+7", "+2", "+4", "-5", "+2", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "25; **Fort** +15, **Ref** +15, **Will** +13"
health:
  - name: HP
    desc: "105; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** cold 5, electricity 5, fire 5, piercing 5, slashing 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d6+11 slashing"
spellcasting: []
abilities_bot:
  - name: "Broad Swipe"
    desc: "`pf2:2` The giant makes two Strikes with its claw against two adjacent foes, both of whom are within its reach. Both attacks count toward the giant's multiple attack penalty, but the penalty doesn't increase until after both attacks.."
  - name: "Massive Rush"
    desc: "`pf2:2` The hulk Strides and makes a claw Strike with a +4 circumstance bonus to damage. If the strike hits, the hulk automatically pushes the target 10 feet."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Huge giants and other enormous creatures make powerful skeletons.

Animated skeletons are among the most common types of undead.

```statblock
creature: "Skeletal Hulk"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
