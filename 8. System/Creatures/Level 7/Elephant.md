---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Elephant"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: ""
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
    desc: "Athletics +17, Survival +15"
abilityMods: ["+7", "+0", "+4", "-4", "+2", "-2"]
abilities_top:
  - name: "Grabbing Trunk"
    desc: "A Medium or smaller creature hit by the elephant's trunk is [[Grabbed]]. If the elephant moves, it can bring the Grabbed creature along with it."
armorclass:
  - name: AC
    desc: "23; **Fort** +18, **Ref** +11, **Will** +13"
health:
  - name: HP
    desc: "130"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tusk +16 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 3d8+9 piercing"
  - name: "Melee strike"
    desc: "Trunk +18 (`pf2:1`) (reach 15 ft.), **Damage**  plus [[Grabbing Trunk]]"
  - name: "Melee strike"
    desc: "Foot +16 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d10+9 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Trample"
    desc: "`pf2:3` Large or smaller, foot, DC 24 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Those who live near elephants have learned to be wary of angering the beasts, but even with precautions in place, elephants sometimes still rampage. There is little an individual person can do when even a single elephant becomes enraged. Furthermore, a herd of angry or frightened elephants can easily destroy an entire village.

Immediately recognizable by their long, prehensile trunks and impressive tusks, elephants have different characteristics depending on where they are found. Elephants are used as beasts of burden in many regions, but they are extremely clever and must be handled with great care.

```statblock
creature: "Elephant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
