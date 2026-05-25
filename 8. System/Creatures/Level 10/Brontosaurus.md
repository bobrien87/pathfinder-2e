---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Brontosaurus"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +23"
abilityMods: ["+9", "+0", "+5", "-4", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "28; **Fort** +21, **Ref** +14, **Will** +16"
health:
  - name: HP
    desc: "220"
abilities_mid:
  - name: "Improved Knockdown"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature as a free action. This attempt neither applies nor counts toward the monster's multiple attack penalty."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tail +23 (`pf2:1`) (reach 20 ft., sweep), **Damage** 2d10+13 bludgeoning plus [[Improved Knockdown]]"
  - name: "Melee strike"
    desc: "Foot +23 (`pf2:1`) (reach 15 ft., unarmed), **Damage** 2d8+13 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Tail Sweep"
    desc: "`pf2:2` The brontosaurus makes a tail Strike and compares the attack roll to the AC of up to three foes, each of whom must be within its tail's melee reach and adjacent to at least one other target. It rolls damage only once and applies it to each creature hit. <br>  <br> A Tail Sweep counts as two attacks for its multiple attack penalty."
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, foot, DC 29 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Brontosauruses are truly gigantic behemoths, herbivores large enough to be unafraid of all but the most massive predators. Brontosauruses have stout bodies and long, sinuous necks and tails. Although their feet are capable of crushing entire buildings, these herbivores are generally considerate of where they step.

Remnants from the world's primeval era, these enormous reptilian animals still exist in large numbers in remote wildernesses or underground in magical Darklands caverns. Lizardfolk, orcs, giants, and other humanoids who live near dinosaurs use the animals as mounts, guards, or hunting beasts. Occasionally, rich nobles will collect dinosaurs to display them in menageries, which almost inevitably leads to cast-offs being nursed back to health by druids and other champions of nature. When dinosaurs establish themselves in regions outside their normal habitats, it's often the result of a large collection being released.

```statblock
creature: "Brontosaurus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
