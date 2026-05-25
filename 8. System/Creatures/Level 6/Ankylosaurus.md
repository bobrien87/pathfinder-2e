---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ankylosaurus"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +17"
abilityMods: ["+7", "+0", "+4", "-4", "+2", "-1"]
abilities_top:
  - name: "Punishing Tail"
    desc: "A creature struck by the ankylosaurus's tail must attempt a DC 24 [[Fortitude]] save. <br>  <br> On a failure, it's [[Stunned]] 1; on a critical failure, it's [[Stunned]] 3."
armorclass:
  - name: AC
    desc: "26; **Fort** +16, **Ref** +10, **Will** +12"
health:
  - name: HP
    desc: "90"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tail +17 (`pf2:1`) (backswing, reach 15 ft.), **Damage** 2d8+7 bludgeoning plus [[Punishing Tail]]"
  - name: "Melee strike"
    desc: "Foot +17 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d6+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, foot, DC 24 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Squat, heavily armored quadrupeds, ankylosauruses are stubborn and irascible. Although they're herbivores, ankylosauruses have been known to attack trespassers simply out of ill temper.

Ankylosauruses have few natural predators, as their bony hides are covered in spiked nubs that jut in many different directions to discourage larger creatures from biting them. An ankylosaurus is about 30 feet long, 10 feet tall at the shoulder, and weighs over 3 tons.

Remnants from the world's primeval era, these enormous reptilian animals still exist in large numbers in remote wildernesses or underground in magical Darklands caverns. Lizardfolk, orcs, giants, and other humanoids who live near dinosaurs use the animals as mounts, guards, or hunting beasts. Occasionally, rich nobles will collect dinosaurs to display them in menageries, which almost inevitably leads to cast-offs being nursed back to health by druids and other champions of nature. When dinosaurs establish themselves in regions outside their normal habitats, it's often the result of a large collection being released.

```statblock
creature: "Ankylosaurus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
