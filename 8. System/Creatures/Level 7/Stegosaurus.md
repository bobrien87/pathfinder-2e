---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Stegosaurus"
level: "7"
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
    desc: "+15; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +20"
abilityMods: ["+7", "+2", "+4", "-4", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +17, **Ref** +13, **Will** +13"
health:
  - name: HP
    desc: "125"
abilities_mid:
  - name: "Dorsal Deflection"
    desc: "`pf2:r` **Trigger** The stegosaurus is targeted with a melee attack. <br>  <br> **Effect** The stegosaurus leans its dorsal plates into the attack, gaining a +2 circumstance bonus to its AC against the triggering attack. If the attack misses, the stegosaurus Steps after the attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tail +18 (`pf2:1`) (reach 15 ft., sweep), **Damage** 2d8+9 piercing"
  - name: "Melee strike"
    desc: "Foot +18 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d6+9 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Trample"
    desc: "`pf2:3` Large or smaller, foot, DC 25 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The stegosaurus is easily recognized by its twin rows of diamond-shaped dorsal plates that run down its spine and thick tail adorned with four large spikes. This configuration protects the herbivore, the plates deflecting attacks while it gores predators with its tail.

The stegosaurus is generally even-tempered and gentle, despite its size. This combination makes it even more popular as a trained pet or guard, but even then one should take care to not annoy the dinosaur—an angry stegosaurus can lash out with little warning.

Remnants from the world's primeval era, these enormous reptilian animals still exist in large numbers in remote wildernesses or underground in magical Darklands caverns. Lizardfolk, orcs, giants, and other humanoids who live near dinosaurs use the animals as mounts, guards, or hunting beasts. Occasionally, rich nobles will collect dinosaurs to display them in menageries, which almost inevitably leads to cast-offs being nursed back to health by druids and other champions of nature. When dinosaurs establish themselves in regions outside their normal habitats, it's often the result of a large collection being released.

```statblock
creature: "Stegosaurus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
