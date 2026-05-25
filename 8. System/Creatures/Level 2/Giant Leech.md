---
type: creature
group: ["Amphibious", "Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Leech"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Animal"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Tremorsense]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +8, Stealth +7"
abilityMods: ["+4", "+1", "+3", "-5", "+1", "-5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +9, **Ref** +7, **Will** +5"
health:
  - name: HP
    desc: "32; **Weaknesses** salt 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mouth +10 (`pf2:1`), **Damage** 1d4+6 piercing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Blood Drain"
    desc: "`pf2:1` **Requirements** The giant leech has a living creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The giant leech drains blood from the creature it has grabbed or restrained. This deals 2d4 piercing damage (DC 18 [[Fortitude]] save). A creature that takes any damage from having its blood drained by a giant leech is [[Drained]] 1 until it receives any kind or amount of healing."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Capable of growing to lengths of nearly 5 feet, giant leeches have circular maws filled with hook-like teeth. They prefer to dwell in stagnant or slow-moving shallow water or in damp, moist undergrowth. Horses and larger animals are their favorite prey, but they won't balk at a chance to latch onto a human- or halfling-sized meal.

```statblock
creature: "Giant Leech"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
