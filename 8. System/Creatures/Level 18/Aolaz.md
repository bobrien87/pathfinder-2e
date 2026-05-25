---
type: creature
group: ["Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aolaz"
level: "18"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Construct"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+33; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +35"
abilityMods: ["+9", "+4", "+8", "-4", "+6", "+3"]
abilities_top:
  - name: "Flawless Hearing"
    desc: "An aolaz has an incredible sense of hearing. It can hear any sound made within 1,000 feet as though it were only 5 feet away from the source of the sound, and any sound within 1 mile as though it were only 30 feet away from the source of the sound. An aolaz's hearing is a precise sense."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "42; **Fort** +35, **Ref** +27, **Will** +31"
health:
  - name: HP
    desc: "255; **Immunities** sonic; **Resistances** physical 15 except adamantine"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trunk +35 (`pf2:1`) (magical, reach 20 ft., sweep, trip), **Damage** 5d10+17 bludgeoning plus [[Grab]]"
  - name: "Melee strike"
    desc: "Foot +33 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 5d8+15 bludgeoning"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 40, attack +30<br>**4th** [[Fly]] (Constant)<br>**2nd** [[Water Walk]] (Constant)"
abilities_bot:
  - name: "Roll"
    desc: "`pf2:1` The aolaz tucks its head down and rolls up into an armored sphere. While Rolling, an aolaz has AC 44, Fort +37, Ref +29, Will +33, and Speed 100 feet, but it can't use its trunk Strikes or its Ultrasonic Blast. It can make foot Strikes while rolling, but only as part of a [[Trample]]. The aolaz can use this action again to unroll and resume its standing form."
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, foot, DC 40 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Ultrasonic Blast"
    desc: "`pf2:1` The aolaz releases a tremendous blast of sonic energy from its trunk in a @Template[line|distance:150], dealing @Damage[12d10[sonic]|options:area-damage] damage. The frequency of this sound is such that it is completely imperceptible to humanoids, but the damage it wreaks is all too evident. Each creature in the area must attempt a DC 40 [[Fortitude]] save. <br>  <br> The aolaz can't use Ultrasonic Blast again for 1d4 rounds. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature takes half damage and is [[Stunned]] 1. <br> - **Failure** The creature takes full damage and is [[Stunned]] 2. <br> - **Critical Failure** The creature takes double damage and is [[Stunned]] 3."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Aolazes are great beasts carved from stone and metal and magically imbued with the essence of life. The exact means of their creation is a long-lost secret, and they are so rare that scholars have little opportunity to study active specimens. The best-known aolazes are museum pieces or battlefield relics destroyed or deactivated centuries ago, though fragmented records suggest that many more were made and might remain, yet to be unearthed.

Most aolazes are built in the shape of great land-bound beasts, such as elephants, rhinoceroses, or dinosaurs. Regardless of the specific creature an aolaz has been constructed to resemble, it is not bound to walk the earth like its inspirations are—it's imbued with the magical ability to pursue across water and even through the air. Few can escape an aolaz's wrath once it is earned.

```statblock
creature: "Aolaz"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
