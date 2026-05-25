---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tiger"
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
    desc: "Acrobatics +11, Athletics +13, Stealth +13"
abilityMods: ["+5", "+3", "+3", "-4", "+2", "-2"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The tiger deals 1d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "21; **Fort** +13, **Ref** +11, **Will** +8"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +13 (`pf2:1`) (unarmed), **Damage** 1d10+7 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +13 (`pf2:1`) (agile, unarmed), **Damage** 1d8+7 slashing"
spellcasting: []
abilities_bot:
  - name: "Pounce"
    desc: "`pf2:1` The tiger Strides and makes a Strike at the end of that movement. If the tiger began this action [[Hidden]], it remains hidden until after this ability's Strike."
  - name: "Wrestle"
    desc: "`pf2:1` The tiger makes a claw Strike against a creature it is [[Grabbing]]. If the attack hits, that creature is knocked [[Prone]]."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Tigers are solitary and territorial hunters, using their striped hides to blend into the forests and jungles they call home and preferring to attack with surprise.

Few predators of the natural world can match the cat's talent for stalking and stealth. Large cats can be found in almost any environment, usually keeping their distance from settlements. When civilization encroaches onto a big cat's hunting grounds, the animals are often driven to making desperate attacks against unwary travelers.

```statblock
creature: "Tiger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
