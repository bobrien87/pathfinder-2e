---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Farmer"
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
    desc: "Athletics +5, Nature +4, Survival +4, Farming Lore +6"
abilityMods: ["+3", "+1", "+3", "+0", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "14; **Fort** +7, **Ref** +5, **Will** +4"
health:
  - name: HP
    desc: "18"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pitchfork +6 (`pf2:1`) (reach 10 ft.), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Apple +5 (`pf2:1`) (agile, nonlethal, thrown 20), **Damage** 1d4+3 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Pitch Bale"
    desc: "`pf2:1` **Requirements** The farmer's last action was a successful pitchfork Strike <br>  <br> **Effect** The farmer moves the creature they hit with their pitchfork up to 5 feet, and the target falls [[Prone]]. The target can attempt a DC 13 [[Reflex]] save to avoid falling prone and avoids being moved altogether on a critical success."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Workers of the fields, vineyards, and orchards of the world, farmers are known for their rugged endurance and skill with plants and animals.

Society is built upon the backs of laborers.

```statblock
creature: "Farmer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
