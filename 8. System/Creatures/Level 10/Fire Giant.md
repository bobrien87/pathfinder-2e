---
type: creature
group: ["Fire", "Giant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fire Giant"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Fire"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]]"
languages: "Common, Jotun, Pyric"
skills:
  - name: Skills
    desc: "Athletics +25, Crafting +22, Intimidation +23, Nature +18"
abilityMods: ["+7", "+0", "+5", "+2", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "31; **Fort** +23, **Ref** +16, **Will** +18"
health:
  - name: HP
    desc: "175; **Immunities** fire; **Weaknesses** cold 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatsword +24 (`pf2:1`) (magical, reach 10 ft., versatile p), **Damage** 2d12+13 slashing"
  - name: "Melee strike"
    desc: "Fist +23 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d8+13 bludgeoning"
  - name: "Ranged strike"
    desc: "Flame +21 (`pf2:1`) (fire, primal), **Damage** 4d6 fire plus 2d6 fire"
spellcasting: []
abilities_bot:
  - name: "Flaming Stroke"
    desc: "`pf2:2` The fire giant imbues their blade with flames and makes a greatsword Strike with a –2 circumstance penalty against each creature in a @Template[line|distance:15]. They make one attack roll only and compare the result to each creature's AC. This Strike deals an additional 1d6 fire damage and counts as one attack for the fire giant's multiple attack penalty"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The most militaristic of giants, fire giants focus obsessively on learning combat techniques, mastering the arts of forging weapons and armor, and finding new ways to dominate their enemies. Most fire giant communities are built around elemental rifts, hot springs, or volcanic calderas and cannot be moved easily, inspiring unwavering defense against any intruders. As a result, their social and political structures are grounded firmly in martial hierarchies, with a strict emphasis on following the orders of one's superior.

As soon as a fire giant can walk, they are fitted with their first suit of forged armor. This armor is constantly remolded and replaced as the giant matures. Beyond what they can forge in their volcanic furnaces, fire giants also look to tame dinosaurs, drakes, and hell hounds as tools of war.

Fire giants are usually identified by their powerful stature and bright orange hair that flickers and dances as if aflame. A typical fire giant stands about 14 feet tall, weighs around 7,000 pounds, and lives to be 350 years old.

Giants are massive humanoid creatures who live in remote regions throughout the world. They vary widely but are united in their hunger, requiring sustenance of their own element along with the feasts one would expect from such a massive humanoid. Although a simple matter for some giants, more esoteric types find this need a harsh reality. While a massive fistful of ice or snow alongside their meal will satisfy a frost giant, shadow giants hunger for the coagulated shadows of the Netherworld.

```statblock
creature: "Fire Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
