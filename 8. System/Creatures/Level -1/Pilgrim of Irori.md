---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pilgrim of Irori"
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
    desc: "+5"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +5, Religion +5, Society +4, Survival +5, Irori Lore +6"
abilityMods: ["+1", "+0", "+2", "+0", "+3", "+1"]
abilities_top:
  - name: "Ambulatory Oration"
    desc: "Creatures that engage in conversation with the pilgrim gain a +1 circumstance bonus to all [[Recall Knowledge]] checks and [[Gather Information]] checks for 4 hours related to any topics discussed with the pilgrim."
  - name: "Path of the Faithful"
    desc: "The pilgrim can use their Religion modifier instead of their Diplomacy modifier to `act gather-information skill=religion` or `act make-an-impression skill=religion` as long as the pilgrim includes their religious teachings."
armorclass:
  - name: AC
    desc: "14; **Fort** +4, **Ref** +4, **Will** +7"
health:
  - name: HP
    desc: "9"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +5 (`pf2:1`) (two hand d8), **Damage** 1d4+1 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d6+1 bludgeoning"
  - name: "Melee strike"
    desc: "Rock +4 (`pf2:1`) (thrown 10), **Damage** 1d4+1 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Pilgrims traverse the lands spurred on by some holy reason, be it to visit a sacred place or follow a prophetic vision.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Pilgrim of Irori"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
