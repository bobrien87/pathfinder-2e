---
type: creature
group: ["Humanoid", "Lizardfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lizardfolk Scout"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Lizardfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8"
languages: "Common, Draconic, Iruxi"
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +5, Diplomacy +4, Nature +6, Stealth +6, Survival +8"
abilityMods: ["+2", "+3", "+1", "-1", "+3", "+1"]
abilities_top:
  - name: "Deep Breath"
    desc: "A lizardfolk scout can hold their breath for 150 rounds (15 minutes)."
  - name: "Giant Centipede Venom"
    desc: "**Saving Throw** DC 14 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage (1 round) <br>  <br> **Stage 2** 1d4 poison damage and [[Off Guard]] (1 round) <br>  <br> **Stage 3** 1d4 poison damage, [[Clumsy]] 1, and [[Fatigued]] (1 round)"
  - name: "Hidden Movement"
    desc: "If the lizardfolk scout starts its turn [[Hidden]] from or undetected by a creature, that creature is [[Off Guard]] against the scout's attacks until the end of the turn."
  - name: "Sneak Attack"
    desc: "The lizardfolk scout deals an extra 1d6 precision damage to [[Off Guard]] creatures."
  - name: "Terrain Advantage"
    desc: "Non-lizardfolk creatures that are in difficult terrain or are in water and lack a swim Speed are [[Off Guard]] to the lizardfolk defender."
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "17"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`) (unarmed), **Damage** 1d6+2 piercing"
  - name: "Melee strike"
    desc: "Tail +8 (`pf2:1`) (agile, finesse), **Damage** 1d4+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Blowgun +8 (`pf2:1`) (agile, nonlethal, reload 1, range 20 ft.), **Damage** 1 piercing plus [[Giant Centipede Venom]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Iruxi scouts are the lizardfolk most often encountered by adventurers, for these unsentimental explorers and hunters spend most of their lives on the move, constantly patrolling the territories held by their enclave. If intruders are driven off, it is the responsibility of iruxi scouts to track them, observe them, and learn their ways and weaknesses so as to report back to the community and aid in the defense against potential reprisals.

Capable and adaptable predators, the reptilian beings known as lizardfolk are heirs to truly ancient civilizations. Their oral traditions cover thousands of years, and they revere the bones of their ancestors. Fossilized lizardfolk are even built into the walls of lizardfolk's stone and glass cities, to allow these predecessors to watch over their kin. Lizardfolk likewise have longstanding traditions of religious worship and astrology, with eyes on the past, the future, and the stars whenever they make a large decision. Their long history has taught them to be patient in all things, though this has seen them losing ground to hastier peoples in modern times.

Lizardfolk refer to themselves as "iruxi," though they have taken their common moniker among other peoples in stride. Most of their settlements are entirely communal, with hatchlings raised by anyone with the time and temperament for such a role. Iruxis dwell and thrive in all tropical and temperate biomes, but they are most at home in swamplands, coastal regions, and river lands. They are talented swimmers, and many of their major cities are partially submerged to take advantage of this fact, causing them to often be overlooked by others. Fish and aquatic plants make up a large part of their preferred diets.

```statblock
creature: "Lizardfolk Scout"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
