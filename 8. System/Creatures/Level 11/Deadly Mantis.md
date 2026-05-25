---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Deadly Mantis"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +18, Athletics +25, Stealth +22"
abilityMods: ["+8", "+3", "+5", "-5", "+3", "-2"]
abilities_top:
  - name: "Sudden Strike"
    desc: "On the first round of combat, creatures that haven't acted are [[Off Guard]] to the deadly mantis."
armorclass:
  - name: AC
    desc: "31; **Fort** +24, **Ref** +20, **Will** +18"
health:
  - name: HP
    desc: "220"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +25 (`pf2:1`) (reach 10 ft.), **Damage** 2d12+14 piercing"
  - name: "Melee strike"
    desc: "Leg +24 (`pf2:1`) (agile, reach 20 ft.), **Damage** 2d10+14 piercing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Fling"
    desc: "`pf2:1` The deadly mantis flings a [[Grabbed]] creature into the air, up to 30 feet overhead and up to 30 feet away from the mantis (the creature takes damage from the fall as normal). If the flung creature lands on another creature, the creature it lands on takes the same amount of bludgeoning damage with a DC 31 [[Reflex]] save."
  - name: "Leaping Grab"
    desc: "`pf2:2` The mantis Leaps up to 40 feet vertically and 20 feet horizontally. At any point during the jump, it can make a leg Strike. If it hits, it automatically [[Grab|Grabs]] the target, bringing the creature along until the end of the jump."
  - name: "Rending Mandibles"
    desc: "`pf2:1` The mantis makes a mandibles Strike against a creature it has [[Grabbed]]. If that Strike hits and the creature is wearing armor with Hardness 12 or lower, the armor is broken. This Strike doesn't further damage armor that's already broken."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These gigantic mantids make their homes within prehistoric forests.

These predators possess lightning-quick forelegs and a bone-breaking bite.

```statblock
creature: "Deadly Mantis"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
