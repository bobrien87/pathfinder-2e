---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Commoner"
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
    desc: "+3"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +5, Society +2, Lore (any one related to their trade) +6"
abilityMods: ["+3", "+1", "+2", "+0", "+1", "+0"]
abilities_top:
  - name: "Power of the Mob"
    desc: "When three or more commoners are adjacent to each other, each commoner gets a +1 circumstance bonus to Athletics checks to `act shove`, attack rolls, and damage rolls."
armorclass:
  - name: AC
    desc: "13; **Fort** +6, **Ref** +3, **Will** +3"
health:
  - name: HP
    desc: "10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sickle +5 (`pf2:1`) (agile, trip), **Damage** 1d4+2 slashing"
  - name: "Melee strike"
    desc: "Rock +3 (`pf2:1`) (thrown 10), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Many commoners live hard lives of toil as they work to keep their families fed and housed in relative comfort.

Society is built upon the backs of laborers.

```statblock
creature: "Commoner"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
