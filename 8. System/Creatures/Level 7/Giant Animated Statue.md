---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Animated Statue"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +17"
abilityMods: ["+6", "-1", "+6", "-5", "+0", "-5"]
abilities_top:
  - name: "Brazier"
    desc: "The statue carries a wide brazier full of hot coals. To make flaming coal Strikes or use Burn Alive, the statue must have the brazier held in one hand or otherwise have it within reach. <br>  <br> Instead of targeting the statue with an attack, a creature can target the brazier directly. The brazier has the same AC and saves as the statue. <br>  <br> Dealing 15 cold damage to the brazier or dousing it with at least 2 gallons of water extinguishes the coals. This prevents the statue from using Burn Alive and causes its ranged attacks to no longer deal fire damage."
armorclass:
  - name: AC
    desc: "26 (22 when broken); construct armor; **Fort** +17, **Ref** +10, **Will** +9"
health:
  - name: HP
    desc: "100"
abilities_mid:
  - name: "Construct Armor (Hardness 10)"
    desc: "Like normal objects, a giant animated statue has Hardness. This Hardness reduces any damage it takes by an amount equal to the Hardness. Once a giant animated statue is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks and its Armor Class is reduced to 22."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Stone Fist +19 (`pf2:1`) (magical), **Damage** 2d12+6 bludgeoning plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Flaming Coal +12 (`pf2:1`) (fire, magical, range 80 ft.), **Damage** 2d6+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Burn Alive"
    desc: "`pf2:1` The statue grinds a creature it has [[Grabbed]] or [[Restrained]] into the red-hot coals of its brazier. The target takes @Damage[3d8[fire],1d8[persistent,fire]] damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Giant animated statues' increased size and power make them most useful in large vaults, spacious chambers, or outdoor locations. Tasks beyond their capabilities typically require a more advanced construct, not an animated object.

Granted a semblance of life through the use of rituals or other strange magic, animated objects take many forms and serve a variety of uses. A few examples of typical animated objects are listed below. Many of these creatures serve as guardians, surprising unsuspecting adventurers when they suddenly attack. Others serve as idle distractions for the exceptionally rich, simple servants created to handle odd jobs, and the like.

```statblock
creature: "Giant Animated Statue"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
