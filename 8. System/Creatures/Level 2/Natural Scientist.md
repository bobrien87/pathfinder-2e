---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Natural Scientist"
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
    desc: "+11"
languages: "Common"
skills:
  - name: Skills
    desc: "Diplomacy +5, Nature +8, Stealth +5, Survival +8, Scouting Lore +10"
abilityMods: ["+1", "+1", "+2", "+2", "+4", "+1"]
abilities_top:
  - name: "Never Lost"
    desc: "The natural scientist can always tell true north and gains a +4 circumstance bonus to Survival checks to `act sense-direction`. They don't take a –2 item penalty to the check if they don't have a compass."
  - name: "Trained Observer"
    desc: "The natural scientist is accustomed to blending into their surroundings and taking notes, giving them a +2 circumstance bonus to `act gather-information`."
armorclass:
  - name: AC
    desc: "16; **Fort** +8, **Ref** +5, **Will** +11"
health:
  - name: HP
    desc: "25"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +7 (`pf2:1`) (two hand d8), **Damage** 1d4+3 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Melee strike"
    desc: "Rock +7 (`pf2:1`) (thrown 10), **Damage** 1d4+3 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

If there's a mystery of nature that requires firsthand evidence to solve, natural scientists collect that data. They spend months documenting and observing events and creatures in the natural world before returning to their academies, labs, and royal studies.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Natural Scientist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
