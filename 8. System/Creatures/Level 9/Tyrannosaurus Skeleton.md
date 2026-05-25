---
type: creature
group: ["Mindless", "Skeleton"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tyrannosaurus Skeleton"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +19"
abilityMods: ["+7", "+0", "+5", "-5", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "27; **Fort** +20, **Ref** +13, **Will** +17"
health:
  - name: HP
    desc: "140; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** cold 10, electricity 10, fire 10, piercing 10, slashing 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (deadly d12, reach 20 ft., unarmed), **Damage** 2d12+9 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Foot +20 (`pf2:1`) (reach 15 ft., unarmed), **Damage** 2d10+9 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Rib Skewer"
    desc: "`pf2:1` The tyrannosaurus skeleton bends down, attempting to skewer one adjacent creature on one of its massive ribs. The creature takes @Damage[(2d10+9)[piercing]] damage (DC 28 [[Reflex]] save). If the creature fails its save and is Medium or smaller, it's also impaled and stuck to the rib. It moves with the skeleton and takes 2d6 bleed until it either Escapes or someone uses `act force-open dc=28` to break the rib (either is DC 28)."
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, foot, DC 28 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A massive dinosaur predator makes for a fearsome skeleton.

Almost any creature that had bones in life and leaves them behind in death can become a shambling, undead skeleton-humanoids, beasts, aberrations, fey, and more.

```statblock
creature: "Tyrannosaurus Skeleton"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
