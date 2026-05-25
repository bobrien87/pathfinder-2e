---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Legbreaker"
level: "6"
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
    desc: "+14"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +16, Intimidation +15, Stealth +15, Thievery +13"
abilityMods: ["+4", "+3", "+3", "-1", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +15, **Ref** +15, **Will** +12"
health:
  - name: HP
    desc: "110"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Maul +17 (`pf2:1`) (magical, shove), **Damage** 1d10+10 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Break Legs!"
    desc: "`pf2:2` The legbreaker makes a maul Strike against an adjacent creature. If it hits, the creature is knocked [[Prone]] and becomes [[Clumsy]] 1 for 1 minute. As long as this clumsy condition lasts, the creature also takes a –5-foot penalty to its Speeds and has weakness 5 to the legbreaker's Strikes. <br>  <br> > [!danger] Effect: Break Legs!"
  - name: "Rushing Strike"
    desc: "`pf2:2` The legbreaker Strides twice. If they end their movement within melee reach of an enemy, they can make a melee Strike against that enemy."
  - name: "Stampeding Shove"
    desc: "`pf2:1` The legbreaker Shoves a creature, gaining a +2 circumstance bonus to their Athletics check if the target is [[Prone]]. If the Shove succeeds, the target takes 2d10 bludgeoning damage (double damage on a critical success)."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Criminal organizations are always happy to loan out money at exorbitant rates, and their legbreakers are always happy to collect.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Legbreaker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
