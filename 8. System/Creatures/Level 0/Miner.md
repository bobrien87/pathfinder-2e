---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Miner"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +3, Athletics +6, Survival +4, Mining Lore +4"
abilityMods: ["+2", "+1", "+3", "+0", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "14; **Fort** +7, **Ref** +5, **Will** +4"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pick +6 (`pf2:1`) (fatal d10), **Damage** 1d6+2 piercing"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Piton Pin"
    desc: "`pf2:1` **Requirements** The miner has their hammer in hand <br>  <br> **Effect** The miner Interacts to draw a piton, then hammers it into a creature to pin them in place, attempting an [[Athletics]] check against the target's Reflex DC. On a hit, the target is [[Immobilized]] until it removes the piton with a successful DC 10 [[Athletics]] check made as an Interact action."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Miners explore deep underground in search of minerals and rare ores, taking numerous precautions to keep themselves safe.

Society is built upon the backs of laborers.

```statblock
creature: "Miner"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
