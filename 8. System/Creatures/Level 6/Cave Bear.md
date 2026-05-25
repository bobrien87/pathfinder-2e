---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cave Bear"
level: "6"
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
    desc: "+13; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +16, Survival +11"
abilityMods: ["+6", "+1", "+6", "-4", "+1", "-1"]
abilities_top:
  - name: "Mauler"
    desc: "The bear gains a +4 circumstance bonus to damage rolls against creatures it has [[Grabbed]]."
armorclass:
  - name: AC
    desc: "24; **Fort** +16, **Ref** +11, **Will** +13"
health:
  - name: HP
    desc: "95"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +16 (`pf2:1`) (unarmed), **Damage** 2d10+6 piercing"
  - name: "Melee strike"
    desc: "Claw +16 (`pf2:1`) (agile, unarmed), **Damage** 2d8+6 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Rush"
    desc: "`pf2:2` The cave bear Strides and makes a Strike at the end of that movement. During the Stride, it gains a +10-foot circumstance bonus to its Speed."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Larger, stronger, and far more aggressive than its smaller cousins, the cave bear is a behemoth that avoids civilized lands, preferring to dwell in remote places. As its name might suggest, the cave bear makes its den in natural caves, and like the grizzly bear, it is fiercely territorial. Unlike a grizzly bear, however, a cave bear is short tempered and will make sure its foe is dead before moving on, usually feasting on its prey's soft flesh once it has been incapacitated. Cave bears are often regarded as powerful guardian spirits by remotedwelling people, though they are also utilized as beasts of war by orcs or even giants. Stone giants in particular have an affinity for keeping trained cave bears as pets or guardians for their homes.

Bears are ferocious predators typically found in cold or temperate woodlands and hills. Many species of bear exist in addition to the two presented below, such as the smaller black bear or the arctic-dwelling polar bear.

```statblock
creature: "Cave Bear"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
