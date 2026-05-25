---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Living Whirlwind"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Air"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Sussuran"
skills:
  - name: Skills
    desc: "Acrobatics +16, Stealth +14"
abilityMods: ["+3", "+5", "+2", "-2", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24; **Fort** +9, **Ref** +16, **Will** +10"
health:
  - name: HP
    desc: "50; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Disperse"
    desc: "`pf2:r` **Trigger** The living whirlwind takes damage from a hostile action; <br>  <br> **Effect** The living whirlwind disperses. Until the end of the current turn, it can't be attacked or targeted, doesn't take up space, and its high winds aura is suppressed. <br>  <br> At the end of the turn, the living whirlwind reforms in any unoccupied space within 25 feet of where it dispersed, and its high winds are restored."
  - name: "High Winds"
    desc: "20 feet. <br>  <br> Air within the emanation is difficult terrain for Flying creatures that don't have the air trait."
  - name: "Swiftness"
    desc: "The living whirlwind's movement doesn't trigger reactions."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Gust +14 (`pf2:1`) (finesse, reach 10 ft.), **Damage** 2d6+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Forceful Winds"
    desc: "`pf2:2` The living whirlwind creates a @Template[line|distance:60] of violent wind. Creatures in the area must succeed at a DC 25 [[Fortitude]] save or be pushed back 10 feet and knocked [[Prone]]."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A living whirlwind resembles a dust devil with a vague mouth and eyes formed among the dust and debris swirling within it.

Hailing from the Plane of Air, these beings appear in a variety of sizes and shapes. They're noted for being elusive, swift, and often difficult to detect due to being composed primarily of air.

```statblock
creature: "Living Whirlwind"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
