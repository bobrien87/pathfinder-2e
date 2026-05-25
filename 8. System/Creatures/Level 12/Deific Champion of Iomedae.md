---
type: creature
group: ["Holy", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Deific Champion of Iomedae"
level: "12"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Holy"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19"
languages: "Common, Empyrean"
skills:
  - name: Skills
    desc: "Athletics +25, Diplomacy +22, Intimidation +26, Religion +23"
abilityMods: ["+5", "+2", "+2", "+0", "+3", "+4"]
abilities_top:
  - name: "Blessed Shield"
    desc: "In the deific champion's hands, a shield gains the *moderate reinforcing rune*, giving it Hardness 8, 84 HP, and BT 42."
  - name: "Deific Reactions"
    desc: "At the start of each of their turns, the deific champion gains an additional reaction they can only use to make a Reactive Strike or to Shield Block."
armorclass:
  - name: AC
    desc: "33; **Fort** +23, **Ref** +19, **Will** +22"
health:
  - name: HP
    desc: "220"
abilities_mid:
  - name: "Champion's Aura"
    desc: "15 feet. <br>  <br> Any follower of [[Iomedae]] in the aura knows the champion is a champion of Iomedae. At the end of the champion's turn, each ally in the aura reduces its [[Frightened]] value by 1. The aura can be suppressed or resumed with a single action, which has the concentrate trait, and ends if the champion falls [[Unconscious]]."
  - name: "Champion's Courage"
    desc: "When the champion becomes [[Frightened]], they reduce the condition value by 1 (to a minimum of 0)."
  - name: "Exalted Retributive Strike"
    desc: "`pf2:r` **Trigger** An enemy damages the deific champion's ally, and both are in the deific champion's aura <br>  <br> **Effect** The ally gains resistance 14 to all damage against the triggering damage. If the enemy is within reach, the deific champion makes a melee Strike against it. Each ally in the champion's aura can spend a reaction to Strike the target with a –5 penalty. <br>  <br> > [!danger] Effect: Exalted Retributive Strike"
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
  - name: "Will Not Fall"
    desc: "`pf2:0` **Trigger** The deific champion's Hit Points are reduced to 0 for the first time that day <br>  <br> **Effect** The champion presses on, refusing to fail their god. They remain standing with 25 Hit Points."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +26 (`pf2:1`) (magical, versatile p), **Damage** 2d8+13 slashing"
  - name: "Melee strike"
    desc: "Fist +25 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+13 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +23 (`pf2:1`) (magical, reload 1, range 120 ft.), **Damage** 2d8+5 piercing"
spellcasting:
  - name: "Divine Focus Spells"
    desc: "DC 30, attack +22<br>**6th** [[Champion's Sacrifice]]<br>**1st** [[Lay on Hands]]"
abilities_bot:
  - name: "Will Not Falter"
    desc: "`pf2:2` **Effect** The deific champion declares their devotion to their deity and their cause. They Stride, then make a melee Strike. If the Strike hits an enemy, all allies within their champion's aura gain a +2 status bonus to attack rolls and saving throws against fear until the start of the deific champion's next turn. <br>  <br> > [!danger] Effect: Will Not Falter"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The deific champion is the paragon of champions, representing the truest form of devotion and dedication to a deity.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Deific Champion of Iomedae"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
