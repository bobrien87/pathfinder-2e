---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Badger"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +4, Stealth +6"
abilityMods: ["+0", "+1", "+2", "-5", "+2", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +8, **Ref** +5, **Will** +6"
health:
  - name: HP
    desc: "15"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is [[Wounded]] 3, it can no longer use this ability"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +8 (`pf2:1`) (unarmed), **Damage** 1d8 piercing"
  - name: "Melee strike"
    desc: "Claw +8 (`pf2:1`) (agile, unarmed), **Damage** 1d6 slashing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The typical badger has dark, brownish-gray fur highlighted with white markings, particularly on the head, giving it a striped mask of fur around its eyes. A threatened badger can swiftly become a ferocious combatant that typically fights until slain.

```statblock
creature: "Badger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
