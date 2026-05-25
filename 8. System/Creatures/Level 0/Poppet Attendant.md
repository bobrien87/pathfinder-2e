---
type: creature
group: ["Construct", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Poppet Attendant"
level: "0"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Construct"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Common (one language their creator speaks)"
skills:
  - name: Skills
    desc: "Crafting +6, Deception +5, Diplomacy +5, Stealth +6"
abilityMods: ["+2", "+0", "+2", "+0", "+1", "+3"]
abilities_top:
  - name: "Simple Doll"
    desc: "The poppet attendant looks like an ordinary doll, fooling others into leaving them alone. When they're in their place of business, the poppet attendant can `act hide` without cover or concealment. Once a creature realizes that the poppet attendant is alive, the attendant can't Hide from them in this way again."
armorclass:
  - name: AC
    desc: "15; **Fort** +9, **Ref** +3, **Will** +6"
health:
  - name: HP
    desc: "17; **Weaknesses** fire 2"
abilities_mid:
  - name: "Pincushion"
    desc: "`pf2:r` **Trigger** The poppet attendant would take piercing damage <br>  <br> **Effect** The poppet directs the implement to a soft part of its body, gaining resistance 5 against the triggering piercing damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shears +8 (`pf2:1`) (deadly d8, finesse, versatile p), **Damage** 1d4+2 slashing"
  - name: "Melee strike"
    desc: "Fist +8 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +6 (`pf2:1`) (propulsive, range 50 ft.), **Damage** 1d6+1 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Poppet attendants are among the most common form of poppets. Most attendants can be found in creative trades, especially among tailors and cobblers.

Poppets are simple constructs made to assist their creators with basic tasks.

```statblock
creature: "Poppet Attendant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
