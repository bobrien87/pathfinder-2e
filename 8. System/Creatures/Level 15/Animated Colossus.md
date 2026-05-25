---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Animated Colossus"
level: "15"
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
    desc: "+23; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +27"
abilityMods: ["+9", "+2", "+8", "-5", "+0", "-5"]
abilities_top:
  - name: "Colossus's Grasp"
    desc: "The colossus can [[Grab]] a creature using only one hand. <br>  <br> It can move normally with a creature [[Grabbed]] or [[Restrained]] in its fist, carrying the creature along. If it has two creatures grabbed in this way, it can't use its fist Strike."
armorclass:
  - name: AC
    desc: "39 (35 when broken); construct armor; **Fort** +31, **Ref** +21, **Will** +19"
health:
  - name: HP
    desc: "245"
abilities_mid:
  - name: "Construct Armor (Hardness 15)"
    desc: "Like normal objects, an animated colossus has Hardness. This Hardness reduces any damage the colossus takes by an amount equal to the Hardness. Once an animated colossus is reduced to fewer than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 35."
  - name: "Enormous"
    desc: "An animated colossus takes up a space of 6 squares by 6 squares (30 feet by 30 feet) and is 100 feet tall."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +32 (`pf2:1`) (magical, reach 30 ft., unarmed), **Damage** 3d12+17 bludgeoning plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Foot +32 (`pf2:1`) (agile, magical, reach 20 ft., unarmed), **Damage** 3d8+17 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(3d12+11)[bludgeoning]], DC 36 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, foot, DC 36 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Animating a 100-foot-tall statue is worth the cost for spellcasters guarding immense dungeons.

Many animated objects have useful functions but become dangers when uncontrolled.

```statblock
creature: "Animated Colossus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
