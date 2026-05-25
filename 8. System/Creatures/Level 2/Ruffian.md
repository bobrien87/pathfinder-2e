---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ruffian"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +7, Intimidation +6, Stealth +6"
abilityMods: ["+3", "+2", "+3", "-1", "+2", "+0"]
abilities_top:
  - name: "Brutal Beating"
    desc: "The ruffian's brutality shakes foes' confidence. <br>  <br> When the ruffian deals damage on a critical hit, the target is [[Frightened]] 1, and the ruffian can push the target up to 10 feet."
  - name: "Sneak Attack"
    desc: "The ruffian deals an extra 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "30"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Combat Grab"
    desc: "`pf2:1` **Trigger** The ruffian has one hand free <br>  <br> **Effect** The ruffian makes a melee Strike while keeping one hand free. If this Strike hits, the ruffian Grabs the target using their free hand. The creature remains [[Grabbed]] until the end of the ruffian's next turn or until it [[Escapes]], whichever comes first."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +9 (`pf2:1`), **Damage** 1d6+5 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
  - name: "Melee strike"
    desc: "Club +8 (`pf2:1`) (thrown 10), **Damage** 1d6+5 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +8 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+5 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Ruffians often work as bodyguards and enforcers for powerful criminals, using their strength to bully others into submission.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Ruffian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
