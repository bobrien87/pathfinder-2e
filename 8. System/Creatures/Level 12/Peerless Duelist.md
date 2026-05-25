---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Peerless Duelist"
level: "12"
rare_01: "Uncommon"
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
    desc: "+24; [[Tremorsense]] (imprecise) 30 feet"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +23, Crafting +22, Deception +24, Intimidation +26, Dueling Lore +25"
abilityMods: ["+3", "+5", "+3", "+0", "+3", "+2"]
abilities_top:
  - name: "I See You"
    desc: "The peerless duelist's Perception checks and firearm Strikes ignore lesser cover and the [[Concealed]] condition."
  - name: "Ace Shooter"
    desc: "The peerless duelist deals an extra die of damage on any firearm Strike they attempt. This extra damage is already included in their *dueling pistol* Strike."
armorclass:
  - name: AC
    desc: "33; **Fort** +21, **Ref** +25, **Will** +21"
health:
  - name: HP
    desc: "200"
abilities_mid:
  - name: "+3 to Initiative with Perception"
    desc: ""
  - name: "Shoot First"
    desc: "`pf2:r` **Trigger** An attacker the duelist can see targets them with a Strike or spell <br>  <br> **Requirements** The duelist is holding a loaded firearm <br>  <br> **Effect** The duelist makes a firearm Strike against the triggering creature. On a critical hit, they disrupt the triggering action."
  - name: "Threatening Aura"
    desc: "60 feet. DC 30 [[Will]] save. The duelist's presence makes foes hesitate. Any enemy that enters or starts its turn in the aura must succeed at the Will save or be [[Stunned]] 1. Regardless of the result of its save, the creature is temporarily immune for 1 day."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +25 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+11 bludgeoning"
  - name: "Ranged strike"
    desc: "Dueling Pistol +26 (`pf2:1`) (concealable, concussive, fatal d10, magical, reload 1, range 60 ft.), **Damage** 2d6+13 piercing"
spellcasting: []
abilities_bot:
  - name: "Disarming Shot"
    desc: "`pf2:1` The duelist fires a dueling pistol to attempt a [[Disarm]] an enemy at range with the bullet. The duelist attempts an attack roll with the dueling pistol instead of an Athletics check, taking any penalty appropriate for the firearm's range increment. The duelist doesn't have to meet the requirements of the Disarm action. <br>  <br> Instead of Disarming, the duelist can use Disarming Shot to attempt an [[Escape]] action for the benefit of themself or an ally within range."
  - name: "Double Reload"
    desc: "`pf2:1` **Requirements** The peerless duelist has an empty dueling pistol in each hand <br>  <br> **Effect** The peerless duelist Interacts to reload both dueling pistols."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Rumors circulate in the saloons that an undefeated master duelist roams the roads, waiting for their next contest.

These lone wolves have an aura of mystery, bravado, and swagger.

```statblock
creature: "Peerless Duelist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
