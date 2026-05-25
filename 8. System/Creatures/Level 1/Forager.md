---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Forager"
level: "1"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Medicine +6, Nature +10, Stealth +3, Survival +10, Local Lore +5"
abilityMods: ["+1", "+3", "+1", "+0", "+4", "+0"]
abilities_top:
  - name: "+4 to Notice Flora and Fauna"
    desc: ""
  - name: "Expert Subsistence"
    desc: "While using Survival to `act subsist statistic=survival`, if the forager rolls any result worse than a success, they get a success. On a success, they can provide subsistence living for themselves and four additional creatures, and on a critical success, they can take care of twice as many creatures as on a success."
  - name: "Natural Specialist"
    desc: "For encounters involving Nature or Survival, the forager is a 3rd-level challenge."
armorclass:
  - name: AC
    desc: "15; **Fort** +5, **Ref** +8, **Will** +8"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
  - name: "Melee strike"
    desc: "Fruit or Vegetable +7 (`pf2:1`) (thrown 20), **Damage** 1d4+1 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Local Poison"
    desc: "`pf2:1` The forager coats their dagger in a diluted, locally sourced poison. Until the end of their turn, Strikes with their dagger deal an additional 2 persistent poison damage."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Foragers know the areas they live and work in like no other. They can tell you exactly where to find a rare medicinal fern, when to harvest it, and how to use it; just don't expect them to be up-to-date on the latest town gossip. They spend as much time in the wilderness as they can, filling their baskets with a variety of useful plants.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Forager"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
