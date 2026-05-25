---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Poacher"
level: "2"
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
    desc: "+9"
languages: "Common"
skills:
  - name: Skills
    desc: "Crafting +4, Deception +4, Nature +7, Stealth +8, Survival +7"
abilityMods: ["+2", "+4", "+1", "+0", "+3", "+0"]
abilities_top:
  - name: "Expert Subsistence"
    desc: "While using Survival to `act subsist statistic=survival`, if the poacher rolls any result worse than a success, they get a success. On a success, they can provide subsistence living for themselves and four additional creatures, and on a critical success, they can take care of twice as many creatures as on a success."
  - name: "Snare Crafting"
    desc: "The poacher knows how to craft the following snares: <br>  <br> - [[Alarm Snare]] <br> - [[Hampering Snare]] <br> - [[Marking Snare]] <br> - [[Signaling Snare]] <br>  <br> The poacher can create up to four snares each day without paying for the materials, using 3 Interact actions to deploy a snare. The snare becomes inert after 24 hours."
armorclass:
  - name: AC
    desc: "18; **Fort** +7, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Light Mace +11 (`pf2:1`), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Shortbow +11 (`pf2:1`) (deadly d10, propulsive, reload 0, range 60 ft.), **Damage** 1d6+3 piercing"
spellcasting: []
abilities_bot:
  - name: "On the Hunt"
    desc: "`pf2:1` The poacher designates one creature they're observing or tracking as their prey. The poacher gains a +2 circumstance bonus to Perception checks to `act seek` the prey and to Survival checks to `act track` the prey. The first time the poacher hits the designated prey in a round, they deal an additional 1d4 precision damage. These effects last until the poacher uses On the Hunt again."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Rules against hunting may insulate the private reserves of nobles or guard the viability of animal populations in shared forests during specific seasons. Poachers violate those laws—sometimes out of greed, sometimes out of desperation, and sometimes for sport.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Poacher"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
