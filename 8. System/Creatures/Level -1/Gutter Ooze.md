---
type: creature
group: ["Mindless", "Ooze"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gutter Ooze"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Mindless"
trait_02: "Ooze"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+2; [[Motion Sense]] (precise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +5, Stealth +2"
abilityMods: ["+0", "+3", "+4", "-5", "+0", "-5"]
abilities_top:
  - name: "Motion Sense"
    desc: "A gutter ooze can sense nearby creatures through vibration and air or water movement."
  - name: "Detritus"
    desc: "Due to all the random trash that collects in a city's gutters, whenever a gutter ooze makes a pseudopod Strike, the type of damage is chosen randomly between bludgeoning, slashing, and piercing."
  - name: "Weak Acid"
    desc: "A gutter ooze's acid damages only organic material—not metal, stone, or other inorganic substances."
armorclass:
  - name: AC
    desc: "7; **Fort** +8, **Ref** +3, **Will** +5"
health:
  - name: HP
    desc: "20; **Immunities** acid, bleed, critical hits, mental, precision, unconscious, visual"
abilities_mid:
  - name: "Slip Up"
    desc: "`pf2:r` **Trigger** An adjacent creature damages the gutter ooze with a melee Strike <br>  <br> **Effect** Some of the gutter ooze's watery protoplasm gushes out beneath the triggering creature's feet. They must succeed at a DC 15 [[Reflex]] save or fall [[Prone]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pseudopod +8 (`pf2:1`) (agile, finesse), **Damage** 1 acid plus 1d4 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These small masses of protoplasm are considered the lesser "cousins" to sewer oozes, emerging from the drainage culverts beneath a city after a rainfall to feed on bits of organic matter that collect in streetside gutters. As they collect just about everything—pebbles, bits of broken glass, and other trash—some cities consider them to be more helpful than detrimental.

```statblock
creature: "Gutter Ooze"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
