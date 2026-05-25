---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pirate"
level: "2"
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
    desc: "Acrobatics +7, Athletics +8, Deception +6, Intimidation +6, Sailing Lore +8"
abilityMods: ["+2", "+3", "+1", "+0", "+2", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "32"
abilities_mid:
  - name: "Bravery"
    desc: "When the pirate rolls a success on a Will save against a fear effect, they get a critical success instead. In addition, any time they gain the [[Frightened]] condition, reduce its value by 1."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Cutlass +10 (`pf2:1`) (forceful, sweep), **Damage** 1d6+5 slashing"
  - name: "Melee strike"
    desc: "Dagger +11 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Dagger +11 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Boarding Action"
    desc: "`pf2:2` The pirate swings on a rope or Strides, moving up to double their Speed. If the pirate boarded or disembarked a boat during this movement, they can make a melee Strike at the end of their movement that deals one extra damage die on a hit."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

These scourges are a threat to anyone who spends time away from land.

Adventurers may need passage on a swift vessel, or they might face danger from raiders at sea or in coastal settlements.

```statblock
creature: "Pirate"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
