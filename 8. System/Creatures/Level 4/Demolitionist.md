---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Demolitionist"
level: "4"
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
    desc: "+10"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +9, Crafting +12, Intimidation +10, Thievery +11, Explosive Lore +14"
abilityMods: ["+1", "+3", "+3", "+4", "+0", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +11, **Ref** +13, **Will** +6"
health:
  - name: HP
    desc: "60; **Resistances** fire 5"
abilities_mid:
  - name: "Explosive Demise"
    desc: "When the demolitionist is reduced to 0 Hit Points while they have any explosives still in their bag, the remaining explosives detonate, unleashing an explosion of fire upon all creatures in a @Template[type:emanation|distance:30]. Each creature in the area takes @Damage[3d6[fire]|options:area-damage] damage with a DC 19 [[Reflex]] save."
  - name: "Replenish Explosives"
    desc: "The demolitionist can replenish their stock of explosives with 4 hours of downtime."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Light Mace +13 (`pf2:1`) (agile, finesse, shove), **Damage** 1d4+7 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +13 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Plant Mine"
    desc: "`pf2:1` `pf2:1` to `pf2:2` <br>  <br> The demolitionist plants a mine in an adjacent square. If a creature moves onto a space with a mine, the mine explodes. This deals 3d8 fire damage to the creature with a DC 21 [[Reflex]] save. The demolitionist can use 2 actions to Plant a Mine to hide the mine, granting it a Stealth DC of 21. Creatures that didn't see the mine as it was planted must actively search for it (using the [[Search]] activity while exploring or the [[Seek]] action in an encounter)."
  - name: "Toss Dynamite"
    desc: "`pf2:2` The demolitionist quickly throws a stick of dynamite up to 20 feet away that explodes in @Template[type:burst|distance:5]. Creatures within the burst take @Damage[4d4[fire]|options:area-damage] damage with a DC 21 [[Reflex]] save."
  - name: "Wall Charge"
    desc: "`pf2:3` The demolitionist plants a powerful wall charge on a flat surface such as a door or wall. Once the charge is planted, it explodes after 1 minute, dealing 60 fire damage to the surface and ignoring up to 15 of the surface's Hardness. The explosive also deals @Damage[5d6[fire]|options:area-damage] damage to creatures within @Template[burst|distance:30]{30 feet} of the explosive with a DC 25 [[Reflex]] save."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

While most engineers take immense pride in their work constructing something that may survive many lifetimes, the demolitionist takes pride in destroying such pompous things in the most spectacular way possible. Every design has a flaw, and that flaw usually involves large quantities of explosives. Demolitionists are often pragmatic and calculated, taking great care to destroy whatever lies before them as efficiently as possible.

Although relatively uncommon across much of Golarion, the frequently eccentric but undeniably brilliant minds who create elaborate devices of clockwork, gunpowder, and steam often loom much larger in the public eye than their numbers would suggest.

```statblock
creature: "Demolitionist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
