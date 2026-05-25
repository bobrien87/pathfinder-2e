---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fence"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +10, Crafting +13, Deception +13, Diplomacy +11, Intimidation +11, Society +11, Stealth +10, Thievery +10, Accounting Lore +13, Underworld Lore +15"
abilityMods: ["+0", "+3", "+0", "+4", "+2", "+4"]
abilities_top:
  - name: "Fence's Eye"
    desc: "Fences can use Underworld lore check to identify an item's value and [[Identify Magic]] on an item. They gain a +2 circumstance bonus to Underworld Lore checks when doing so, and to all Underworld Lore checks related to stolen items."
  - name: "Sneak Attack"
    desc: "The fence deals an extra 2d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "20; **Fort** +9, **Ref** +12, **Will** +15"
health:
  - name: HP
    desc: "70"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +14 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+6 piercing"
  - name: "Melee strike"
    desc: "Dagger +14 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+6 piercing"
  - name: "Melee strike"
    desc: "Shortsword +14 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+6 piercing"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Fence's Feint"
    desc: "`pf2:1` The fence Feints, then can Step. If the feint succeeds, the target is [[Off Guard]] against the fence's melee attacks until the end of the fence's next turn (or to all melee attacks on a critical success)."
  - name: "Quick Rummage"
    desc: "`pf2:1` The fence always has a few items close at hand. The fence Interacts to draw a weapon or an item that takes a single action to activate, and then Strikes with the weapon or Activates the Item."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Fences make themselves indispensable to the underworld by paying for stolen goods only to resell them later, whether through a seemingly legitimate business or to a closed group of elite buyers.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Fence"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
