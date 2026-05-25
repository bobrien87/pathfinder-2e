---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Toymaker"
level: "3"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Crafting +10, Diplomacy +9, Performance +9, Society +8, Toys Lore +12"
abilityMods: ["+0", "+3", "+1", "+3", "+2", "+2"]
abilities_top:
  - name: "Punchout Bolts"
    desc: "The toymaker's crossbow bolts are specially constructed with heavy, sap-like heads instead of piercing tips. Strikes with these bolts deal bludgeoning damage instead of piercing and have the nonlethal trait. <br>  <br> In addition, a creature hit by one must succeed a DC 20 [[Fortitude]] save saving throw or be pushed 10 feet back (or 20 feet on a critical failure)."
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +10, **Will** +10"
health:
  - name: HP
    desc: "45"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +12 (`pf2:1`) (nonlethal, reload 1, range 60 ft.), **Damage** 1d6+5 bludgeoning plus [[Punchout Bolts]]"
spellcasting: []
abilities_bot:
  - name: "Scatter Blocks"
    desc: "`pf2:1` The toymaker throws out a handful of toy building blocks of various sizes 20 feet away in a @Template[type:burst|distance:5]. The area becomes difficult terrain and hazardous terrain. A creature that moves on the ground through the area takes 1 piercing damage for every square of that area it moves into."
  - name: "Wind-Up Soldier"
    desc: "`pf2:2` The toymaker releases a wind-up soldier that Strides 15 feet in a straight line. Whenever the soldier moves adjacent to a creature or a creature moves into a space adjacent to the soldier, the creature takes 2d8 slashing damage with a DC 20 [[Reflex]] save as the soldier wildly slashes its sword. A creature can take damage from the wind-up soldier only once per round. At the start of each of the toymaker's turns, the solder Strides 15 feet further along the same path. The soldier falls apart after it moves three times."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The whimsy of a toymaker is only matched by their ruthlessness when cornered. Most of their creations are designed solely for the enjoyment of others. However, every toymaker knows—whether through failed designs or intentional creations—how to turn their toys into dangerous weapons. They are often hesitant to use toys in such ways, and more often than not, they will attempt to solve problems with diplomacy first. Some toymakers have fully turned to the profession of making deadly toys. They often have dangerous patrons or nefarious intentions. Some use dangerous toys as a means of vigilantism, while others use them as a means to sneak weapons into guarded areas.

Although relatively uncommon across much of Golarion, the frequently eccentric but undeniably brilliant minds who create elaborate devices of clockwork, gunpowder, and steam often loom much larger in the public eye than their numbers would suggest.

```statblock
creature: "Toymaker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
