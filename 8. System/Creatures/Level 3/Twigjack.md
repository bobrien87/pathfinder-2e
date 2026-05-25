---
type: creature
group: ["Fey", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Twigjack"
level: "3"
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
    desc: "+9; [[Darkvision]]"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +9, Nature +7, Stealth +11"
abilityMods: ["+2", "+4", "+2", "+0", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "19; **Fort** +9, **Ref** +11, **Will** +7"
health:
  - name: HP
    desc: "50; **Weaknesses** fire 5, axe vulnerability 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +11 (`pf2:1`) (agile, finesse, reach 0 ft., unarmed), **Damage** 1d10+4 slashing"
  - name: "Ranged strike"
    desc: "Splinter +11 (`pf2:1`) (deadly d6, range 30 ft.), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Bramble Jump"
    desc: "`pf2:3` **Requirements** The twigjack is in undergrowth <br>  <br> **Effect** The twigjack scrambles into the undergrowth and instantly teleports to a square of undergrowth within 60 feet. This movement doesn't trigger reactions."
  - name: "Splinter Spray"
    desc: "`pf2:2` The twigjack sprays a barrage of splinters and brambles from its body in a @Template[cone|distance:15], dealing @Damage[4d6[piercing]|options:area-damage] damage (DC 20 [[Reflex]] save). <br>  <br> It can't use Splinter Spray again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

"True" twigjacks, as they consider themselves, are found in wild forests alongside the fey they idolize.

Maladjusted forest denizens, twigjacks form from the cruel and prankish combination of fey and the very woods in which they reside. A twigjack's body is made up of prickly brambles woven with vines. Shaggy, mossy growth, not unlike hair, tops a twigjack's head. Its mouth is just a canyon of splintered and broken sticks bisecting its face. Leaves and sprigs of new growth randomly sprout from the creature's body. Many dense forests on Golarion have at least a handful of twigjacks living in the undergrowth.

While truculent and violent, twigjacks care deeply for what they consider to be their forests. These creatures harass outsiders who delve deep into their wooded domains, forcing back even the most determined explorers, foresters, and travelers, especially when those intruders cut roads through the forest. However, they are not terribly territorial when it comes to other forest creatures. When sylvan creatures, especially fey, rally against an outside threat, twigjacks in the area eagerly arrive to fight, even if they were not invited.

```statblock
creature: "Twigjack"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
