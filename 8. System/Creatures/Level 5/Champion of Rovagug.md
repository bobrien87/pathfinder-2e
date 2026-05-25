---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Champion of Rovagug"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +13, Deception +10, Intimidation +12, Religion +8, Survival +8"
abilityMods: ["+4", "+1", "+3", "+0", "+1", "+3"]
abilities_top:
  - name: "Fearsome Armament"
    desc: "The champion grants their greataxe the [[Fearsome]] rune while they wield it."
armorclass:
  - name: AC
    desc: "25; **Fort** +12, **Ref** +8, **Will** +10"
health:
  - name: HP
    desc: "70"
abilities_mid:
  - name: "Champion's Aura"
    desc: "15 feet. Any follower of [[Rovagug]] in the aura knows the champion is a champion of Rovagug. Enemies in the aura take a –1 circumstance penalty to saves against fear, and an enemy that ends its turn in the aura can't reduce the value of its [[Frightened]] condition below 1. The aura can be suppressed or resumed with a single action, which has the concentrate trait, and ends if the champion falls [[Unconscious]]."
  - name: "Destructive Vengeance"
    desc: "`pf2:r` **Trigger** An enemy in the champion's aura damages the champion <br>  <br> **Effect** The champion increases the amount of damage they take by 2d6 and deals 2d6 spirit damage to the triggering enemy. In addition, until the end of the champion's next turn, the champion's Strikes against the triggering creature deals 2 extra spirit damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fearsome Greataxe +13 (`pf2:1`) (magical, sweep), **Damage** 1d12+8 slashing"
  - name: "Melee strike"
    desc: "Javelin +10 (`pf2:1`) (thrown 30), **Damage** 1d6+8 piercing"
  - name: "Melee strike"
    desc: "Gauntlet +13 (`pf2:1`) (agile, free hand), **Damage** 1d4+8 bludgeoning"
spellcasting:
  - name: "Champion Devotion Spells"
    desc: "DC 20, attack +12<br>**1st** [[Touch of the Void]]"
abilities_bot:
  - name: "Axe Swipe"
    desc: "`pf2:2` The champion makes a melee Strike with a +1 circumstance bonus to the attack roll and compares the roll to the AC of up to two foes that are in reach and adjacent to each other. The champion rolls damage only once and applies it to each creature they hit. This counts as two attacks toward their multiple attack penalty."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

There are perhaps no mortals more anathematic to peace than champions of Rovagug or other destructive deities.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Champion of Rovagug"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
