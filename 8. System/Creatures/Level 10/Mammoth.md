---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mammoth"
level: "10"
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
    desc: "+18; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +22, Survival +19"
abilityMods: ["+8", "+1", "+5", "-4", "+1", "-2"]
abilities_top:
  - name: "Grabbing Trunk"
    desc: "A Medium or smaller creature hit by the mammoth's trunk is [[Grabbed]]. If the mammoth moves, it can bring the Grabbed creature along with it."
armorclass:
  - name: AC
    desc: "29; **Fort** +21, **Ref** +15, **Will** +18"
health:
  - name: HP
    desc: "190"
abilities_mid:
  - name: "+2 Status to All Saves vs. Cold"
    desc: ""
  - name: "Cold Adaptation"
    desc: "The mammoth reduces the effects it suffers from cold environments by one step."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tusk +22 (`pf2:1`) (reach 15 ft., unarmed), **Damage** 3d8+12 piercing"
  - name: "Melee strike"
    desc: "Trunk +22 (`pf2:1`) (reach 15 ft.), **Damage**  plus [[Grabbing Trunk]]"
  - name: "Melee strike"
    desc: "Foot +22 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d10+12 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Dual Tusks"
    desc: "`pf2:1` The mammoth makes two tusk Strikes, each against a different creature. This counts as one attack for the mammoth's multiple attack penalty, and the penalty doesn't increase until after both attacks."
  - name: "Trample"
    desc: "`pf2:3` Large or smaller, foot, DC 28 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Found mostly in colder climates, mammoths are accustomed to dealing with desperate and dangerous predators, trampling and crushing their enemies while using their larger tusks to greater effect. Humanoids dwelling in harsh, frost-bound lands rely on the mammoth's strength to help them survive.

Immediately recognizable by their long, prehensile trunks and impressive tusks, elephants have different characteristics depending on where they are found. Elephants are used as beasts of burden in many regions, but they are extremely clever and must be handled with great care.

```statblock
creature: "Mammoth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
