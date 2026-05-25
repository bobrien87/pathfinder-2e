---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Animated Trebuchet"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +24"
abilityMods: ["+9", "+2", "+8", "-5", "+0", "-5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "36 (32 when broken); construct armor; **Fort** +29, **Ref** +19, **Will** +17"
health:
  - name: HP
    desc: "200"
abilities_mid:
  - name: "Construct Armor (Hardness 14)"
    desc: "Like normal objects, an animated trebuchet has Hardness. This Hardness reduces any damage the trebuchet takes by an amount equal to the Hardness. Once an animated trebuchet is reduced to fewer than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 32."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Arm +27 (`pf2:1`) (magical, reach 15 ft.), **Damage** 3d12+11 bludgeoning plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Rock +27 (`pf2:1`) (brutal, magical, range 120 ft.), **Damage** 3d10+11 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Launch"
    desc: "`pf2:1` **Requirements** The animated trebuchet has a creature [[Grabbed]] in its arm. <br>  <br> **Effect** The animated trebuchet attempts an [[Athletics]] check against the grabbed creature's Fortitude DC. <br>  <br> On a success, it fires the creature up to 40 feet in height and up to 120 feet away. The creature takes 4d12 bludgeoning damage plus the appropriate falling damage. If the flung creature lands on another creature, the creature it lands on takes the same amount of bludgeoning damage (DC 33 [[Reflex]] save). <br>  <br> On a successful Launch, the animated trebuchet must Interact to reposition its arm into the proper position before it can Launch again."
  - name: "Trample"
    desc: "`pf2:3` Large or smaller, arm, DC 33 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Large armies sometimes pay exorbitant fees to animate their siege weapons.

Many animated objects have useful functions but become dangers when uncontrolled.

```statblock
creature: "Animated Trebuchet"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
