---
type: creature
group: ["Elf", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Elf Ranger"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Elf"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]]"
languages: "Common, Elven"
skills:
  - name: Skills
    desc: "Acrobatics +7, Arcana +3, Deception +3, Nature +6, Stealth +7, Survival +6"
abilityMods: ["+1", "+4", "+1", "+3", "+3", "+1"]
abilities_top:
  - name: "Unimpeded Journey"
    desc: "The elf ranger ignores difficult terrain."
armorclass:
  - name: AC
    desc: "16; **Fort** +4, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "17"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+2 piercing"
  - name: "Ranged strike"
    desc: "Shortbow +9 (`pf2:1`) (deadly d8, range 60 ft.), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Double Shot"
    desc: "`pf2:1` The elf ranger makes two shortbow Strikes targeting two different creatures within the shortbow's first range increment. Both Strikes uses the elf's current multiple attack penalty, but each strike takes a –2 penalty."
  - name: "Elf Step"
    desc: "`pf2:1` The elf Steps twice."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Many elves learn the bow before even picking up their first blade. Because of this, many elves act as rangers at some point in their long lives.

Elves are mysterious and intelligent, and graceful and cunning in battle.

```statblock
creature: "Elf Ranger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
