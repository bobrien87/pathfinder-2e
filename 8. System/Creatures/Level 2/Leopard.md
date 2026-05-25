---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Leopard"
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
    desc: "+7; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +7, Stealth +8"
abilityMods: ["+3", "+4", "+2", "-4", "+1", "-2"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The leopard deals 1d4 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +10, **Will** +5"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (finesse, unarmed), **Damage** 1d10+3 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +10 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d6+3 slashing"
spellcasting: []
abilities_bot:
  - name: "Maul"
    desc: "`pf2:1` The leopard makes two claw Strikes against a creature it has [[Grabbed]]. Both count toward its multiple attack penalty, but the penalty increases only after both attacks are made."
  - name: "Pounce"
    desc: "`pf2:1` The leopard Strides and makes a Strike at the end of that movement. If the leopard began this action [[Hidden]], it remains hidden until after this ability's Strike."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Leopards are among the smallest of the big cats, yet they are still dangerous creatures to tangle with. Leopard statistics can also be used for black panthers, white-spotted snow leopards, or tawny-coated cougars.

Few predators of the natural world can match the cat's talent for stalking and stealth. Large cats can be found in almost any environment, usually keeping their distance from settlements. When civilization encroaches onto a big cat's hunting grounds, the animals are often driven to making desperate attacks against unwary travelers.

```statblock
creature: "Leopard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
