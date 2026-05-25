---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Guard"
level: "1"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +7, Intimidation +5, Legal Lore +3"
abilityMods: ["+3", "+2", "+2", "+0", "+2", "-1"]
abilities_top:
  - name: "+1 Bonus on Perception to Find concealed objects"
    desc: ""
armorclass:
  - name: AC
    desc: "16; **Fort** +7, **Ref** +5, **Will** +5"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Melee strike"
    desc: "Sap +7 (`pf2:1`) (agile, nonlethal), **Damage** 1d6+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +6 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Guards are rank-and-file members of a town watch or city guard, trained to look for trouble, take down criminals, and follow orders.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Guard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
