---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tracker"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12"
languages: "Common"
skills:
  - name: Skills
    desc: "Nature +11, Stealth +9, Survival +13, Forest Lore +5"
abilityMods: ["+2", "+4", "+2", "+0", "+4", "+0"]
abilities_top:
  - name: "Expert Subsistence"
    desc: "While using Survival to `act subsist statistic=survival`, if the tracker rolls any result worse than a success, they get a success. On a success, they can provide subsistence living for themselves and 8 additional creatures, and on a critical success, they can take care of twice as many creatures as on a success."
  - name: "Master Tracker"
    desc: "The tracker can [[Track]] while moving at full speed."
armorclass:
  - name: AC
    desc: "19; **Fort** +7, **Ref** +11, **Will** +9"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +11 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+6 piercing"
  - name: "Melee strike"
    desc: "Dagger +11 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+6 piercing"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Longbow +11 (`pf2:1`) (deadly d10, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 1d8+5 piercing"
spellcasting: []
abilities_bot:
  - name: "On the Hunt"
    desc: "`pf2:1` The tracker designates one creature they're observing or tracking as their prey. <br>  <br> The tracker gains a +2 circumstance bonus to Perception checks to `act seek` the prey and to Survival checks to `act track` the prey. <br>  <br> The first time the tracker hits the designated prey in a round, they deal an additional 1d4 precision damage. These effects last until the tracker uses On the Hunt again."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

An untrained eye might spot a sign or two of a wild creature's passing, but only a skilled tracker can identify several such signs and discern their relationship to each other, connecting one to the next until they form a trail of prints, scat, fur, feathers, and blood that leads to the quarry's lair.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Tracker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
