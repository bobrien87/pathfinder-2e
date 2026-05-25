---
type: creature
group: ["Humanoid", "Kobold"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kobold Egg Guardian"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: "Common, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +11, Deception +9, Diplomacy +9"
abilityMods: ["+3", "+3", "+1", "+0", "+0", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "19; **Fort** +9, **Ref** +12, **Will** +6"
health:
  - name: HP
    desc: "48"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longspear +12 (`pf2:1`) (reach 10 ft.), **Damage** 1d8+5 piercing"
  - name: "Melee strike"
    desc: "Claw +12 (`pf2:1`) (agile, unarmed), **Damage** 1d4+5 slashing"
  - name: "Ranged strike"
    desc: "Crossbow +12 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Immobilizing Thrust"
    desc: "`pf2:2` The kobold egg guardian makes a longspear Strike. If the Strike hits, the target must attempt a DC 20 [[Reflex]] save. On a failure, the creature is [[Immobilized]] until the kobold egg guardian moves, attacks with the longspear, or is no longer wielding the longspear."
  - name: "Luring Retreat"
    desc: "`pf2:2` The kobold egg guardian screams and Strides up to their Speed. Each enemy who sees or hears the kobold egg guardian must succeed at a DC 17 [[Will]] save or be [[Fascinated]] by the egg guardian for 1 round. On the creature's turn, it must use at least 1 action (or 2 actions on a critical failure) to move closer to the kobold egg guardian (while avoiding obvious dangers). Regardless of the result of the save, targets are then immune to Luring Retreat for 24 hours."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Kobold egg guardians are some of the best warriors in a tribe, tasked with protecting the next generation. They pledge to give their lives to protect the tribe's eggs, though not before exhausting all their tricks.

Kobolds are drawn to beings and objects of power, establishing their communities near them. Once a warren has been formed, the resident kobolds construct traps and set up ambushes to deter interlopers.

```statblock
creature: "Kobold Egg Guardian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
