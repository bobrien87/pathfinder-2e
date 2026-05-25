---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Teacher"
level: "-1"
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
    desc: "+4"
languages: "Common (up to 3 additional languages)"
skills:
  - name: Skills
    desc: "Diplomacy +5, Intimidation +5, Academia Lore +14, Additional Lore +14"
abilityMods: ["+0", "+0", "-1", "+4", "+2", "+3"]
abilities_top:
  - name: "Academic Specialist"
    desc: "For academic encounters, a teacher is a 4th-level challenge."
  - name: "Font of Knowledge"
    desc: "The teacher can attempt to [[Recall Knowledge]] on any general subject with a +10 modifier."
armorclass:
  - name: AC
    desc: "12; **Fort** +1, **Ref** +2, **Will** +6"
health:
  - name: HP
    desc: "5"
abilities_mid:
  - name: "Inspirational Presence"
    desc: "50 feet. Any of the teacher's students in the aura gains a +1 circumstance bonus to [[Recall Knowledge]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Cane +4 (`pf2:1`) (two hand d8), **Damage** 1d4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +4 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The passing of knowledge and traditions from generation to generation is a time-honored occupation. Teachers exist to strengthen their populations with literacy, history, and advanced sciences, but most of all with inspiration. Most teachers provide general knowledge so their students are well-rounded, but some are experts or even masters of a single discipline.

True power comes from knowledge—the power to shape the growth of kingdoms by mere whispers, stay three steps ahead of adversaries, or even know which flora is best for creating untraceable poisons.

```statblock
creature: "Teacher"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
