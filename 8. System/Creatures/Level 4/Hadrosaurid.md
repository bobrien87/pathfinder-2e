---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hadrosaurid"
level: "4"
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
    desc: "+13; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +12, Stealth +10"
abilityMods: ["+6", "+2", "+3", "-4", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +12, **Ref** +10, **Will** +11"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tail +14 (`pf2:1`) (reach 15 ft.), **Damage** 2d6+8 bludgeoning"
  - name: "Melee strike"
    desc: "Foot +12 (`pf2:1`) (reach 15 ft., unarmed), **Damage** 2d4+8 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Sprint"
    desc: "`pf2:2` **Frequency** once per minute <br>  <br> **Effect** The hadrosaurid Strides twice. It has a +20-foot circumstance bonus to its Speed during these Strides."
  - name: "Trample"
    desc: "`pf2:3` Large or smaller, foot, DC 21 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Hadrosaurids are a broad grouping of herbivorous dinosaurs that share characteristic flat snouts filled with rows of grinding teeth well suited for feeding on vegetation. Also known as "duck-billed dinosaurs" due to the unusual shape of their jaws, hadrosaurids are lumbering creatures that can rival an elephant in size, although they tend to be much less aggressive and are prone to flight when confronted with danger. Many species of hadrosaurids have uniquely shaped crests on their heads, making them easily recognizable even to amateur dinosaur watchers.

Giants and other oversized creatures have been known to domesticate hadrosaurids to serve as livestock. Despite their ability to sprint quickly, they don't make particularly viable mounts due to their timid natures, but a panicked herd of hadrosaurids can wreak great damage.

Remnants from the world's primeval era, these enormous reptilian animals still exist in large numbers in remote wildernesses or underground in magical Darklands caverns. Lizardfolk, orcs, giants, and other humanoids who live near dinosaurs use the animals as mounts, guards, or hunting beasts. Occasionally, rich nobles will collect dinosaurs to display them in menageries, which almost inevitably leads to cast-offs being nursed back to health by druids and other champions of nature. When dinosaurs establish themselves in regions outside their normal habitats, it's often the result of a large collection being released.

```statblock
creature: "Hadrosaurid"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
