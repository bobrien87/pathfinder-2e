---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Mantis"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +10, Stealth +12"
abilityMods: ["+5", "+3", "+3", "-5", "+2", "+0"]
abilities_top:
  - name: "Sudden Strike"
    desc: "On the first round of combat, creatures that haven't acted are [[Off Guard]] to the giant mantis."
armorclass:
  - name: AC
    desc: "18; **Fort** +10, **Ref** +12, **Will** +7"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Leg +12 (`pf2:1`) (agile, reach 10 ft.), **Damage** 1d10+5 piercing"
  - name: "Melee strike"
    desc: "Mandibles +12 (`pf2:1`), **Damage** 1d12+5 piercing"
spellcasting: []
abilities_bot:
  - name: "Capturing Grab"
    desc: "`pf2:1` This ability functions as [[Grab]], plus on a success, the mantis can choose to pull the creature adjacent to it, then makes a mandibles Strike against the creature. This extra benefit doesn't apply when the mantis maintains the Grab."
  - name: "Lunging Strike"
    desc: "`pf2:2` The giant mantis lunges forward, making a leg Strike with an extended reach of 20 feet. If it hits, the mantis can use Capturing Grab after the Strike even if the creature is out of reach."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These massive cousins of praying mantises stand taller than an average human.

These predators possess lightning-quick forelegs and a bone-breaking bite.

```statblock
creature: "Giant Mantis"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
