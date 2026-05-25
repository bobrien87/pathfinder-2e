---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Smoke Creeper"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Air"
trait_02: "Elemental"
trait_03: "Evil"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Sussuran"
skills:
  - name: Skills
    desc: "Acrobatics +15, Stealth +15"
abilityMods: ["+1", "+5", "+3", "-2", "+4", "+0"]
abilities_top:
  - name: "Smoke Vision"
    desc: "The smoke creeper ignores the [[Concealed]] condition from smoke."
armorclass:
  - name: AC
    desc: "24; **Fort** +13, **Ref** +17, **Will** +11"
health:
  - name: HP
    desc: "80; **Immunities** bleed, paralyzed, poison, precision, sleep; **Resistances** fire 5"
abilities_mid:
  - name: "Smoke Form"
    desc: "The smoke creeper can move through the spaces of other creatures but can't end its movement in the same space."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Smoke Mandibles +17 (`pf2:1`) (agile, finesse), **Damage** 1d6 poison plus 2d8+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Choking Swoop"
    desc: "`pf2:3` The smoke creeper Flies up to its Speed, moving through the spaces of other creatures and leaving traces of itself behind. Each breathing creature it passes through must attempt a DC 23 [[Fortitude]] save. On a failure, the creature inhales part of the elemental and is [[Immobilized]] for 1 minute by the pain of the smoke rasping in its throat and lungs. A creature can attempt to end this condition by spending an action coughing and succeeding at a DC 23 [[Fortitude]] save."
  - name: "Painful Exhalations"
    desc: "`pf2:2` **Requirements** At least one creature within 40 feet is [[Immobilized]] from the smoke creeper's Choking Swoop <br>  <br> **Effect** The smoke creeper flaps its wings, violently drawing the lingering smoke free from all creatures immobilized from its Choking Swoop within 40 feet. Each target must attempt a DC 23 [[Fortitude]] save. On a failure, the creature is [[Enfeebled]] 1 for 1 minute and [[Sickened]] 1 ([[Enfeebled]] 2 and [[Sickened]] 2 on a critical failure). Regardless of the result, the creature is no longer immobilized from the smoke creeper's Choking Swoop."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Smoke creepers shift and modify their appearance as they float through the Plane of Air, but they prefer to take on a vaguely insectile form with wings trailing choking fumes and glowing red eyes.

Some elementals embody aspects of air, such as smoke, lightning, and fog.

```statblock
creature: "Smoke Creeper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
