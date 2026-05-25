---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jailer"
level: "3"
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
    desc: "+9"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +11, Diplomacy +5, Intimidation +7"
abilityMods: ["+4", "+3", "+1", "+0", "+2", "+0"]
abilities_top:
  - name: "+1 Bonus on Perception to Find Concealed Objects"
    desc: ""
  - name: "Subdue Prisoners"
    desc: "The jailer doesn't take the normal penalty for making a nonlethal attack when attacking with their club."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "45"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +11 (`pf2:1`), **Damage** 1d6+8 bludgeoning"
  - name: "Melee strike"
    desc: "Club +10 (`pf2:1`) (thrown 10), **Damage** 1d6+8 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +10 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Efficient Capture"
    desc: "`pf2:3` **Requirements** The jailer has manacles in hand and is adjacent to a creature <br>  <br> **Effect** The jailer attempts to bind the creature's wrists or ankles with the manacles. If the jailer succeeds at an attack roll with a +9 modifier against the target's AC, they apply the manacles."
  - name: "Intimidating Strike"
    desc: "`pf2:2` The jailer makes a melee Strike. If it hits and deals damage, the target is [[Frightened]] 1, or [[Frightened]] 2 on a critical hit."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A jailer's primary responsibility is to keep prisoners from escaping. Jailers must often use force, or the threat of force, to keep their charges in line, as even the most carefully crafted cells, manacles, or chains can fail with time and persistence when the prisoners have the will to attempt an escape.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Jailer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
