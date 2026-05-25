---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Reckless Scientist"
level: "6"
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
    desc: "+12"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +12, Crafting +16, Deception +9, Medicine +10, Stealth +14, Engineering Lore +14, Underworld Lore +14"
abilityMods: ["+1", "+4", "+4", "+4", "+2", "-1"]
abilities_top:
  - name: "Unstable Collection"
    desc: "A reckless scientist carries a collection of poorly stowed alchemical items: 3 elixirs of life and 6 alchemical grenades. The scientist replenishes these items each day using scavenged materials. The alchemical grenades deal either acid, cold, or fire damage plus 2 persistent damage and 2 splash damage of the same type (typically the collection contains two of each grenade)."
armorclass:
  - name: AC
    desc: "23; **Fort** +16, **Ref** +14, **Will** +10"
health:
  - name: HP
    desc: "95; **Resistances** poison 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Poison"
    desc: ""
  - name: "Unstable Explosion"
    desc: "When an attacker scores a critical hit against the reckless scientist, one of the scientist's alchemical items bursts. The GM determines the item randomly. If it was a bomb, the alchemist takes damage from the bomb, and any creature adjacent to the alchemist takes the splash damage. Any other item is wasted."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sickle +17 (`pf2:1`) (agile, finesse, magical, trip), **Damage** 1d4+7 slashing"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning"
  - name: "Ranged strike"
    desc: "Alchemical Grenade +16 (`pf2:1`) (splash, range 20 ft.), **Damage** 2 untyped plus 2 untyped plus 2d6 untyped"
spellcasting: []
abilities_bot:
  - name: "Quick Grenadier"
    desc: "`pf2:1` The reckless scientist Interacts to draw an alchemical grenade with an Interact action and throws it as a ranged Strike."
  - name: "Reckless Alchemy"
    desc: "`pf2:2` The reckless scientist attempts to combine two alchemical grenades or two elixirs of life into one item. They can Interact to draw the items if necessary. They attempt a DC 22 [[Crafting]] check, destroying both component items to create one new item. <br> - **Success** The new item has the full effect of both component items, and the reckless scientist can Activate it. If they don't Activate it before the end of their turn, the item explodes (as critical failure). <br> - **Failure** The new item is inert. <br> - **Critical Failure** The unstable item explodes, dealing 3d6 piercing damage to the reckless scientist."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

It's the reckless scientist's job to break the rules of reality, no matter the cost.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Reckless Scientist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
