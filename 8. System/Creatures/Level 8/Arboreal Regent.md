---
type: creature
group: ["Plant", "Wood"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Arboreal Regent"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Plant"
trait_02: "Wood"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]]"
languages: "Arboreal, Common, Fey (Speak with Plants)"
skills:
  - name: Skills
    desc: "Athletics +19, Diplomacy +16, Intimidation +16, Nature +18, Stealth +11"
abilityMods: ["+7", "-1", "+6", "+1", "+4", "+2"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Sunder Objects"
    desc: "When an arboreal regent damages an item or structure, it deals an additional 2d10 damage to that item or structure."
armorclass:
  - name: AC
    desc: "26; **Fort** +20, **Ref** +11, **Will** +16"
health:
  - name: HP
    desc: "150; **Weaknesses** axe vulnerability 5, fire 10; **Resistances** bludgeoning 5, piercing 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Branch +19 (`pf2:1`) (reach 15 ft.), **Damage** 2d12+7 bludgeoning"
  - name: "Melee strike"
    desc: "Root +19 (`pf2:1`) (trip), **Damage** 2d8+7 bludgeoning"
  - name: "Ranged strike"
    desc: "Rock +19 (`pf2:1`) (brutal, range 120 ft.), **Damage** 2d10+7 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 26, attack +18<br>**3rd** [[Speak with Plants]] (Constant)"
abilities_bot:
  - name: "Awaken Tree"
    desc: "`pf2:2` The arboreal regent causes a tree within 180 feet to uproot itself and fight as a minion using the statistics for an [[Awakened Tree]]. The arboreal regent can control up to two awakened trees at a time, and they can issue commands to both trees as a single action, which has the concentrate and auditory traits."
  - name: "Throw Rock"
    desc: "`pf2:1` The monster picks up a rock within reach or retrieves a stowed rock and throws it, making a ranged Strike."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Arboreal regents are lumbering, solitary creatures responsible for guarding an entire forest. They take an especially long view of affairs and never act brashly or without much deliberation. They occasionally come together in small groups called groves to share news and pass their wisdom down to the arboreal wardens that have sprouted under their watch. In times of grave danger, all the groves in a region may gather for a great months-long meeting to plan and, eventually, act upon a threat.

The typical arboreal regent is 30 feet tall, has a trunk 2 feet in diameter, and weighs 4,500 pounds.

Arboreals are guardians of the forest and representatives of the trees. As long-lived as the woods they watch over, arboreals consider themselves parents and shepherds of trees rather than their gardeners. Consequently, while arboreals tend to be slow and methodical, they are terrifyingly swift when forced to fight in defense of the woods. Though they rarely seek out the companionship of short-lived folk—even elves are fugacious in the eyes of arboreals—and have an inherent distrust of change, arboreals have been known to tolerate those who seek to learn from their long-winded, rambling monologues, especially if such pupils also express a desire to protect the timberlands. Against those who threaten their realm, such as loggers eager to harvest lumber or settlers aiming to establish croplands or a town, arboreals' wrath is unwavering and devastating. Perhaps ironically, arboreals are gifted at tearing down what others build—a trait that serves vengeful members of their kind well.

```statblock
creature: "Arboreal Regent"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
