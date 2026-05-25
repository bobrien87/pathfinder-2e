---
type: creature
group: ["Fey", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sprigjack"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fey"
trait_02: "Plant"
trait_03: "Wood"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +5, Nature +3, Stealth +5"
abilityMods: ["+1", "+3", "+2", "-1", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +5, **Ref** +7, **Will** +3"
health:
  - name: HP
    desc: "10; **Weaknesses** axe vulnerability 2, fire 2"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +7 (`pf2:1`) (agile, finesse, reach 0 ft., unarmed), **Damage** 1d4+1 slashing"
  - name: "Ranged strike"
    desc: "Splinter +7 (`pf2:1`) (range 30 ft.), **Damage** 1d4 piercing"
spellcasting: []
abilities_bot:
  - name: "Bramble Jump"
    desc: "`pf2:3` **Requirements** The twigjack is in undergrowth <br>  <br> **Effect** The twigjack scrambles into the undergrowth and instantly teleports to a square of undergrowth within 60 feet. This movement doesn't trigger reactions."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Weaker twigjacks are often found in cultivated forests and even gardens. They seek to drive away interlopers, growing as their environment runs wild.

Maladjusted forest denizens, twigjacks form from the cruel and prankish combination of fey and the very woods in which they reside. A twigjack's body is made up of prickly brambles woven with vines. Shaggy, mossy growth, not unlike hair, tops a twigjack's head. Its mouth is just a canyon of splintered and broken sticks bisecting its face. Leaves and sprigs of new growth randomly sprout from the creature's body. Many dense forests on Golarion have at least a handful of twigjacks living in the undergrowth.

While truculent and violent, twigjacks care deeply for what they consider to be their forests. These creatures harass outsiders who delve deep into their wooded domains, forcing back even the most determined explorers, foresters, and travelers, especially when those intruders cut roads through the forest. However, they are not terribly territorial when it comes to other forest creatures. When sylvan creatures, especially fey, rally against an outside threat, twigjacks in the area eagerly arrive to fight, even if they were not invited.

```statblock
creature: "Sprigjack"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
