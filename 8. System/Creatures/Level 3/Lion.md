---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lion"
level: "3"
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
    desc: "+9; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +9, Stealth +10"
abilityMods: ["+4", "+3", "+2", "-4", "+2", "-2"]
abilities_top:
  - name: "Pack Attack"
    desc: "The lion deals 1d4 extra damage to any creature that's within reach of at least two of the lion's allies."
  - name: "Sneak Attack"
    desc: "The lion deals 1d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "45"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (unarmed), **Damage** 1d10+6 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +11 (`pf2:1`) (agile, unarmed), **Damage** 1d8+6 slashing"
spellcasting: []
abilities_bot:
  - name: "Pounce"
    desc: "`pf2:1` The lion Strides and makes a Strike at the end of that movement. If the lion began this action [[Hidden]], it remains hidden until after this ability's Strike."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Lions are cooperative hunters, ambushing dangerous prey in groups of lionesses that work in tandem to trap and kill their prey. Male lions are typically larger, with long manes, and when they hunt, they tend to do so on their own.

Few predators of the natural world can match the cat's talent for stalking and stealth. Large cats can be found in almost any environment, usually keeping their distance from settlements. When civilization encroaches onto a big cat's hunting grounds, the animals are often driven to making desperate attacks against unwary travelers.

```statblock
creature: "Lion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
