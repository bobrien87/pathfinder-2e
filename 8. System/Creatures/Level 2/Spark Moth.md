---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Spark Moth"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Air"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +9, Stealth +9"
abilityMods: ["+0", "+3", "+1", "-4", "+1", "+0"]
abilities_top:
  - name: "Arc Lightning"
    desc: "The spark moth transforms into lightning that arcs to a large piece of metal within 100 feet, such as a suit of metal armor or metal weapon. The elemental then returns to its normal form in a space adjacent to the metal. This movement doesn't trigger reactions."
armorclass:
  - name: AC
    desc: "18; **Fort** +5, **Ref** +11, **Will** +7"
health:
  - name: HP
    desc: "20; **Immunities** bleed, electricity, paralyzed, poison, sleep"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Wing +11 (`pf2:1`) (agile, finesse), **Damage** 1d4+5 electricity"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Spark bats congregate around volatile weather in the Plane of Air.

Some elementals embody aspects of air, such as smoke, lightning, and fog.

```statblock
creature: "Spark Moth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
