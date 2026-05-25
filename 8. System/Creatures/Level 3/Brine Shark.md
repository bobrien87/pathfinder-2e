---
type: creature
group: ["Aquatic", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Brine Shark"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
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
    desc: "Athletics +10, Stealth +11, Survival +8"
abilityMods: ["+3", "+2", "+2", "-4", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "19; **Fort** +9, **Ref** +11, **Will** +6"
health:
  - name: HP
    desc: "45; **Immunities** bleed, paralyzed, poison, sleep; **Resistances** fire 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (unarmed), **Damage** 1d12+7 piercing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Deep Plunge"
    desc: "`pf2:1` The brine shark dives straight down into the water, moving up to twice its swim Speed in a straight vertical line. It can use this ability while grabbing a creature."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Brine sharks are deadly elementals that roam the endless oceans of the Plane of Water. They often slip into mortal oceans as well, competing with natural predators or even joining schools of flesh and blood sharks.

Water elementals can be very destructive, but often not intentionally so; just as water can bring life to mortals in need, its waves can pound shores and rains can flood cities. Water elementals are similarly difficult to predict.

```statblock
creature: "Brine Shark"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
