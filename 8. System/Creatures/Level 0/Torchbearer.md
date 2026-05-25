---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Torchbearer"
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
    desc: "+5"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +4, Stealth +5, Survival +3, Architecture Lore +2"
abilityMods: ["+2", "+3", "+1", "+0", "+1", "+1"]
abilities_top:
  - name: "Torch Combatant"
    desc: "A torchbearer is adept at attacking with torches and deals 1 persistent fire damage when they critically hit with a [[Torch]]."
armorclass:
  - name: AC
    desc: "15; **Fort** +5, **Ref** +9, **Will** +4"
health:
  - name: HP
    desc: "15"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Torch +5 (`pf2:1`), **Damage** 1d6+2 bludgeoning plus 1 fire"
  - name: "Melee strike"
    desc: "Dagger +6 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +6 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +6 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Torchbearers carry light sources for seasoned explorers.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Torchbearer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
