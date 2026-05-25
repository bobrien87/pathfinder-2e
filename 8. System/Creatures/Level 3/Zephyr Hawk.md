---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zephyr Hawk"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
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
    desc: "Acrobatics +13, Stealth +11"
abilityMods: ["+2", "+4", "+1", "-4", "+0", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +13, **Will** +7"
health:
  - name: HP
    desc: "36; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Wing +11 (`pf2:1`) (agile, finesse), **Damage** 1d8+4 slashing"
spellcasting: []
abilities_bot:
  - name: "Circling Attack"
    desc: "`pf2:2` The zephyr hawk Flies up to half its Speed, makes two wing Strikes, then Flies up to half its Speed again to return to its original location. The second half of this movement doesn't trigger reactions. Both attacks count toward the zephyr hawk's multiple attack penalty, but the penalty doesn't increase until after it makes both attacks."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Zephyr hawks drift among the currents of the Plane of Air in great flocks. They delight in riding the air currents with no destination in mind.

Hailing from the Plane of Air, these beings appear in a variety of sizes and shapes. They're noted for being elusive, swift, and often difficult to detect due to being composed primarily of air.

```statblock
creature: "Zephyr Hawk"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
