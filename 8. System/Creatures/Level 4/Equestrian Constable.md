---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Equestrian Constable"
level: "4"
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
    desc: "+11"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +12, Nature +10, Settlement Lore +8"
abilityMods: ["+4", "+1", "+3", "+0", "+2", "+1"]
abilities_top:
  - name: "Trained Animal"
    desc: "The equestrian constable rides a trained mount of their level or lower, usually a [[War Horse]] or, for elite equestrian constables, a [[Veteran War Horse]]. The animal has the standard number of actions, uses its normal stat block, and counts toward the encounter's XP budget normally."
armorclass:
  - name: AC
    desc: "21; **Fort** +14, **Ref** +8, **Will** +10"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Opportune Maneuver"
    desc: "`pf2:r` **Trigger** A creature within 10 feet uses an action with the move trait or leaves a space within the constable's reach during its move action <br>  <br> **Effect** The constable attempts to `act trip` the triggering creature. On a success, the triggering action is disrupted."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Guisarme +14 (`pf2:1`) (reach 10 ft., trip), **Damage** 1d8+8 slashing plus [[Knockdown]]"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +11 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Vigilant Vantage"
    desc: "`pf2:1` The equestrian constable Seeks or [[Points Out]] a target. They can Interact to draw an item or [[Command an Animal]] to approach or attack the target."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Equestrian constables patrol for criminals on horseback in wealthy areas or serve as reeves to enforce court orders. Some patrol major roads far from the protection of the city guard.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Equestrian Constable"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
