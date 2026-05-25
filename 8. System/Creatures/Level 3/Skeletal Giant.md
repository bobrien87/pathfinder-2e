---
type: creature
group: ["Mindless", "Skeleton"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skeletal Giant"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +12, Intimidation +9"
abilityMods: ["+5", "+1", "+3", "-5", "+0", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +8, **Will** +7"
health:
  - name: HP
    desc: "50; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** cold 5, electricity 5, fire 5, piercing 5, slashing 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Glaive +12 (`pf2:1`) (deadly d8, forceful, reach 15 ft.), **Damage** 1d8+7 slashing"
  - name: "Melee strike"
    desc: "Horns +12 (`pf2:1`) (agile), **Damage** 1d10+5 piercing"
spellcasting: []
abilities_bot:
  - name: "Broad Swipe"
    desc: "`pf2:2` The giant makes two Strikes with its glaive against two adjacent foes, both of whom are within its reach. Both attacks count toward the giant's multiple attack penalty, but the penalty doesn't increase until after both attacks."
  - name: "Terrifying Charge"
    desc: "`pf2:2` The giant Strides and makes a horns Strike with a +4 circumstance bonus to damage. <br>  <br> If the strike hits, the giant attempts to `act demoralize` the target."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The reanimated bones of giants make excellent necromantic thralls.

Animated skeletons are among the most common types of undead.

```statblock
creature: "Skeletal Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
