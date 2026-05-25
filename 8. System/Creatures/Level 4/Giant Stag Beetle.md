---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Stag Beetle"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +13"
abilityMods: ["+5", "+1", "+5", "-5", "+2", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "22; **Fort** +13, **Ref** +9, **Will** +8"
health:
  - name: HP
    desc: "55"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +13 (`pf2:1`), **Damage** 2d8+5 piercing"
  - name: "Melee strike"
    desc: "Foot +11 (`pf2:1`) (unarmed), **Damage** 1d10+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, foot, DC 21 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The giant stag beetle is larger than a horse, and the sight of one flying (if slowly and somewhat clumsily) on great buzzing wings is unnerving. Its enormous mandibles are used to impress mates, intimidate rivals, and discourage predators, for they can deliver deadly blows. While giant stag beetles are deadly predators, skilled wranglers can domesticate them. In such a capacity, these beetles serve well as beasts of burden or even as mounts.

Giant stag beetles can be a serious menace in marshes, cavern complexes, and heavy forests. More than one logging camp has attracted a cluster of giant stag beetles and had to be completely abandoned, yielding all its lumber to the hunger of the giant insects.

Not all beetles are harmless creatures that can be easily crushed underfoot. Oversized and ravenous giant beetles can be found throughout the temperate and tropical regions of the world. They are often benign creatures, though when threatened or roused, giant beetles are quite dangerous. Their powerful mandibles and tough exoskeletons make for a challenging combatant.

```statblock
creature: "Giant Stag Beetle"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
