---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hero Hunter"
level: "13"
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
    desc: "+25"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +23, Athletics +26, Crafting +24, Deception +19, Nature +21, Stealth +27, Survival +25"
abilityMods: ["+5", "+4", "+3", "+3", "+2", "+0"]
abilities_top:
  - name: "Prepared Trapper"
    desc: "A hero hunter carries the materials to Craft two Alarm Snares, two Grasping Snares, one [[Snagging Hook Snare]], and one [[Stunning Snare]]. The hero hunter replenishes any used supplies each time they make their daily preparations."
armorclass:
  - name: AC
    desc: "33; **Fort** +22, **Ref** +25, **Will** +21"
health:
  - name: HP
    desc: "230"
abilities_mid:
  - name: "Nimble Dodge"
    desc: "`pf2:r` **Trigger** The hero hunter is targeted with a melee or ranged attack by an attacker they can see <br>  <br> **Effect** The hero hunter gains a +2 circumstance bonus to AC against the triggering attack."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greataxe +27 (`pf2:1`) (magical, sweep), **Damage** 2d12+13 slashing plus [[Hunters Precision]]"
  - name: "Melee strike"
    desc: "Fist +26 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+13 bludgeoning plus [[Hunters Precision]]"
  - name: "Ranged strike"
    desc: "Hand Crossbow +26 (`pf2:1`) (magical, reload 1, range 60 ft.), **Damage** 2d6+8 piercing plus [[Hunters Precision]]"
spellcasting: []
abilities_bot:
  - name: "Deadly Snares"
    desc: "`pf2:3` The hero hunter Crafts a snare that would normally take 1 minute or less to Craft. The Stealth DC to locate the snare and DC to disable it with Thievery are equal to the hero hunter's Crafting DC if it's higher than the snare's DC."
  - name: "Felling Shot"
    desc: "`pf2:1` The hero hunter makes a ranged Strike. If it hits and deals damage to a flying target, the target falls up to 120 feet but takes no damage from the fall. The creature can't Fly, [[Leap]], levitate or otherwise leave the ground until the end of the hero hunter's next turn."
  - name: "Hunter's Precision"
    desc: "`pf2:1` The hero hunter knows how to hunt and kill any game. While in this stance, all the hero hunter's Strikes deal an additional 2d8 precision damage, and the range increment for their ranged weapon Strikes is 20 feet longer than normal. If the hunter gets a critical hit with a weapon Strike, the target also takes 2d6 persistent bleed damage."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Some hunters grow bored of simple beasts and monsters. For them, a battle-tested warrior is the finest prey.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Hero Hunter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
