---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hippopotamus"
level: "5"
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
    desc: "+11; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +13, Stealth +11, Survival +11"
abilityMods: ["+6", "+2", "+6", "-4", "+4", "-2"]
abilities_top:
  - name: "Deep Breath"
    desc: "The hippopotamus can hold its breath for 5 minutes."
armorclass:
  - name: AC
    desc: "21; **Fort** +15, **Ref** +9, **Will** +11"
health:
  - name: HP
    desc: "85"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +15 (`pf2:1`) (deadly d10), **Damage** 2d8+8 piercing"
  - name: "Melee strike"
    desc: "Foot +15 (`pf2:1`), **Damage** 1d10+8 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "`pf2:1` 30 feet <br>  <br> **Requirements** The monster is hiding in water and a creature that hasn't detected it is within the listed number of feet. <br>  <br> **Effect** The monster moves up to its swim Speed + 10 feet toward the triggering creature, traveling on water and on land. Once the creature is in reach, the monster makes a Strike against it. The creature is [[Off-Guard]] against this Strike."
  - name: "Capsize"
    desc: "`pf2:1` The hippopotamus tries to capsize an adjacent aquatic vessel of its size or smaller. The hippopotamus must succeed at an Athletics check with a DC of 25 (reduced by 5 for each size smaller the vessel is than the hippo) or the pilot's Sailing Lore DC, whichever is higher."
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, foot, DC 22 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Typical adult hippos move quickly on land and attack stealthily in the water.

Hippopotamuses, or hippos for short, are semiaquatic animals that spend most of their time in rivers and lakes, but can thrive on land.

```statblock
creature: "Hippopotamus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
