---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tournament Combatant"
level: "5"
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
    desc: "+12"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +12, Intimidation +11, Performance +11"
abilityMods: ["+3", "+5", "+1", "+0", "+1", "+2"]
abilities_top:
  - name: "Powerful Fists"
    desc: "The tournament combatant's fist Strikes don't take penalties when making lethal attacks."
armorclass:
  - name: AC
    desc: "21; **Fort** +10, **Ref** +15, **Will** +10"
health:
  - name: HP
    desc: "75"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d8+5 bludgeoning"
  - name: "Melee strike"
    desc: "Nunchaku +14 (`pf2:1`) (backswing, disarm, finesse), **Damage** 1d6+5 bludgeoning"
  - name: "Melee strike"
    desc: "Shuriken +14 (`pf2:1`) (agile, reload 0, thrown 20), **Damage** 1d6+5 piercing"
spellcasting: []
abilities_bot:
  - name: "Work the Crowd"
    desc: "`pf2:1` **Frequency** once per 10 minutes <br>  <br> **Requirements** The combatant is within 50 feet of at least three spectators <br>  <br> **Effect** With a flashy flurry of moves, the tournament combatant elicits cheers. The tournament combatant is [[Quickened]] for 1 minute. They can use the extra action only to Strike or Stride."
  - name: "Flying Attack"
    desc: "`pf2:2` The tournament combatant makes a [[Leap]], [[High Jump]], or [[Long Jump]]. At any point during the jump, if they're adjacent to an enemy, they can Strike that enemy with a fist or nunchaku Strike, even in midair. The combatant falls to the ground after the Strike. If the distance they fall is no more than the height of their jump, they land upright and take no damage."
  - name: "Somersault Attack"
    desc: "`pf2:1` The tournament combatant attempts to `act tumble-through` a target's space. If they succeed on their Acrobatics check, the tournament combatant can make a fist or nunchaku Strike against that target while moving through its space."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Tournaments attract martial artists like moths to a flame, with participants crossing vast distances for the chance to test their might.

Martial artists strive to master the art of hand-to-hand fighting.

```statblock
creature: "Tournament Combatant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
