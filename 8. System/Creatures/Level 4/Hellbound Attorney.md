---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hellbound Attorney"
level: "4"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Human"
trait_04: "Humanoid"
trait_05: "Unholy"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Greater Darkvision]]"
languages: "Common, Diabolic"
skills:
  - name: Skills
    desc: "Acrobatics +10, Deception +11, Diplomacy +11, Intimidation +11, Society +12, Legal Lore +14"
abilityMods: ["+1", "+2", "+0", "+4", "+1", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +9, **Ref** +12, **Will** +13"
health:
  - name: HP
    desc: "60; **Weaknesses** holy 2; **Resistances** fire 4"
abilities_mid:
  - name: "Abrogation of Consequences"
    desc: "`pf2:r` **Trigger** The Hellbound attorney rolls a success or critical failure on a saving throw against a linguistic effect. <br>  <br> **Effect** The attorney finds a loophole in the wording of the effect, turning the success into a critical success or a critical failure into a normal failure."
  - name: "Opening Statement"
    desc: "`pf2:0` **Trigger** The Hellbound attorney's turn begins. <br>  <br> **Effect** The attorney enumerates the alleged crimes of a creature they can see and attempts a Legal lore check against that creature's Will DC. <br>  <br> On a success, the attorney's Strikes deal an additional 2d6 precision damage (4d6 precision damage on a critical success) to the creature until the end of the attorney's turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Elegant Cane +12 (`pf2:1`) (agile, finesse, shove, unholy), **Damage** 1d4+3 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21, attack +13<br>**1st** [[Breathe Fire]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The Hellbound attorney sought the assistance of a [[Phistophilus]]-one of Hell's contract devils-to bolster her legalistic ability on the Universe.

There are countless legions of lawful fiends in the nine layers of Hell, warring against the celestial planes and scouring the Material Plane for souls to corrupt.

```statblock
creature: "Hellbound Attorney"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
