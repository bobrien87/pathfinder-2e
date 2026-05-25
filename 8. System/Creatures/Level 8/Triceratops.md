---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Triceratops"
level: "8"
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
    desc: "+16; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +21"
abilityMods: ["+7", "+0", "+4", "-4", "+2", "-1"]
abilities_top:
  - name: "Vicious Gore"
    desc: "A triceratops deals 2d6 extra persistent bleed damage to [[Prone]] targets it hits with its horns."
armorclass:
  - name: AC
    desc: "26; **Fort** +18, **Ref** +12, **Will** +14"
health:
  - name: HP
    desc: "140"
abilities_mid:
  - name: "Frill Defense"
    desc: "`pf2:r` **Trigger** The rider is targeted with an attack. <br>  <br> **Requirements** A creature must be mounted on the triceratops. <br>  <br> **Effect** The triceratops intercepts the attack with its bony frill. The rider gains a +2 circumstance bonus to its AC against the triggering attack. <br>  <br> > [!danger] Effect: Frill Defense"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horns +19 (`pf2:1`) (reach 15 ft.), **Damage** 2d8+9 piercing plus [[Knockdown]]"
  - name: "Melee strike"
    desc: "Foot +19 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d6+9 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Lumbering Charge"
    desc: "`pf2:1` The triceratops Strides up to 10 feet and then makes a Strike."
  - name: "Trample"
    desc: "`pf2:3` Large or smaller, foot, DC 26 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Triceratopses are muscular quadrupeds with powerful short legs, thick necks, and heads crowned by a wide, bony frill. Though they bear three large horns, they use these bony protrusions only to defend themselves or fight for dominance. Short-tempered and obstinate, triceratopses are unlikely to back down from a fight unless they are hopelessly outmatched, and the creatures are known to fight to the death for no apparent reason beyond stubbornness. Triceratopses often serve as mounts for humanoids, particularly giants, who can comfortably ride behind the dinosaurs' protective bone frills. A triceratops is 30 feet long and weighs as much as 10 tons.

Remnants from the world's primeval era, these enormous reptilian animals still exist in large numbers in remote wildernesses or underground in magical Darklands caverns. Lizardfolk, orcs, giants, and other humanoids who live near dinosaurs use the animals as mounts, guards, or hunting beasts. Occasionally, rich nobles will collect dinosaurs to display them in menageries, which almost inevitably leads to cast-offs being nursed back to health by druids and other champions of nature. When dinosaurs establish themselves in regions outside their normal habitats, it's often the result of a large collection being released.

```statblock
creature: "Triceratops"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
