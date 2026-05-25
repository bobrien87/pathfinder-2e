---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Abbot of Abadar"
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
languages: "Common, Empyrean, Utopian"
skills:
  - name: Skills
    desc: "Deception +6, Diplomacy +8, Religion +21, Society +7"
abilityMods: ["+1", "+1", "-2", "+2", "+4", "+3"]
abilities_top:
  - name: "Religious Specialist"
    desc: "For encounters involving religious debates or conflicts of doctrine, the abbot is a 9th-level challenge."
  - name: "True Faith"
    desc: "The abbot uses lessons from scripture to foil others trying to deceive them. They can use their Religion modifier to `act sense-motive skill=religion` instead of Perception, and their Religion DC instead of their Perception DC against attempts to [[Lie]] to them."
armorclass:
  - name: AC
    desc: "14; **Fort** +3, **Ref** +4, **Will** +11"
health:
  - name: HP
    desc: "15"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Griffon Cane +6 (`pf2:1`) (two hand d8), **Damage** 1d4+3 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +6 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Divine Protection"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The abbot beseeches their deity to protect someone in their charge, attempting a DC 25 [[Religion]] check. If it succeeds, a divine [[Sanctuary]] spell affects one of the abbot's allies within 60 feet. The Will DC is 17."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Abbots are often the heads of religious institutions less focused on spellcasting, such as orphanages, religious schools, or charities.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Abbot of Abadar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
