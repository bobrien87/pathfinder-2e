---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Siegebreaker"
level: "14"
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
    desc: "+24"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +23, Crafting +27, Stealth +25, Thievery +23, Engineering Lore +29, Siege Lore +29"
abilityMods: ["+2", "+5", "+4", "+5", "+2", "+0"]
abilities_top:
  - name: "Alchemical Grenades"
    desc: "A siegebreaker carries 15 alchemical grenades that deal either acid, cold, or fire damage plus 10 persistent damage and 10 splash damage of the same type (typically five of each damage type). They replenish these grenades each day."
  - name: "Expanded Splash"
    desc: "The siegebreaker's grenades deal splash damage in a @Template[emanation|distance:10]{10-foot radius}."
  - name: "The Wall Must Fall"
    desc: "**Requirements** The siegebreaker is at the base of a fortified wall <br>  <br> **Effect** The siegebreaker has studied for years to gain exact knowledge of how to combine the alchemical ingredients in their grenades to exponentially multiply their power, creating a terrifying siege-ender bomb that can break open a city wall. The siegebreaker spends 10 minutes combining the ingredients from 9 different alchemical grenades of their choice. The siegebreaker then sets a fuse timer up to 1 minute long. When time's up, the bomb explodes in a concentrated @Template[type:burst|distance:20], dealing @Damage[20d6[acid]|options:area-damage], @Damage[20d6[cold]|options:area-damage]{cold}, or @Damage[20d6[fire]|options:area-damage]{fire} damage that ignores up to 10 Hardness of structures. Any creature in the area can reduce the damage they take with a DC 37 [[Reflex]] save."
armorclass:
  - name: AC
    desc: "34; **Fort** +25, **Ref** +28, **Will** +23"
health:
  - name: HP
    desc: "300"
abilities_mid:
  - name: "Explosive Compounds"
    desc: "When an attacker scores a critical hit against the siegebreaker, one of the siegebreaker's alchemical grenades bursts. The GM determines the grenade randomly. The siegebreaker takes damage from the grenade as though they were hit by the grenade (applying their resistance normally), and any creature in a @Template[type:emanation|distance:10] takes the splash damage."
  - name: "Resistance 10 to Alchemical Items"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Light Mace +27 (`pf2:1`) (agile, finesse, magical, shove), **Damage** 2d4+18 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +25 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+18 bludgeoning"
  - name: "Ranged strike"
    desc: "Alchemical Grenade +27 (`pf2:1`) (splash, range 60 ft.), **Damage** 3d6 untyped plus 10 untyped plus 10 untyped"
spellcasting: []
abilities_bot:
  - name: "Quick Grenadier"
    desc: "`pf2:1` The siegebreaker Interacts to draw a grenade, then Strikes with it."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

When a well-constructed or magically warded fortification repels every assault, a siegebreaker is called in. These masters of alchemical destruction find that the bigger and more protected the wall, the more satisfying it is to break it.

Whether they're hired to wage war, protect a caravan, or infiltrate an impenetrable fortress, there's ample work for mercenaries all over Golarion.

```statblock
creature: "Siegebreaker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
