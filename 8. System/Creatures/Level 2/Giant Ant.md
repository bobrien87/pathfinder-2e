---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Ant"
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
    desc: "+7; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +8, Survival +7"
abilityMods: ["+4", "+1", "+4", "-5", "+1", "-4"]
abilities_top:
  - name: "Giant Ant Venom"
    desc: "**Saving Throw** DC 18 [[Fortitude]] save <br>  <br> **Maximum Duration** 4 rounds <br>  <br> **Stage 1** 1d8 poison and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 1d10 poison and [[Enfeebled]] 2 (1 round) <br>  <br> **Stage 3** 1d12 poison and [[Enfeebled]] 3 (1 round)"
armorclass:
  - name: AC
    desc: "18; **Fort** +10, **Ref** +7, **Will** +5"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +9 (`pf2:1`), **Damage** 1d8+4 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Stinger +9 (`pf2:1`) (agile), **Damage** 1d6+4 piercing plus [[Giant Ant Venom]]"
spellcasting: []
abilities_bot:
  - name: "Haul Away"
    desc: "`pf2:1` **Requirements** The giant ant has a Large or smaller creature grabbed <br>  <br> **Effect** The giant ant Strides up to its full Speed, carrying the grabbed creature with it. It is [[Encumbered]] if the grabbed creature is Medium or larger."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Giant ants are much like their smaller kin in their industrious habits, though growing to the size of ponies makes them much deadlier.

Ants are industrious insects that aid the natural processes of decay and renewal.

```statblock
creature: "Giant Ant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
