---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Munsahir"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Common, Pyric"
skills:
  - name: Skills
    desc: "Athletics +7, Crafting +10, Intimidation +4, Plane of Fire Lore +6"
abilityMods: ["+3", "+1", "+4", "+2", "+2", "+0"]
abilities_top:
  - name: "Burning Touch"
    desc: "The munsahir's Strikes deal an extra 1d6 fire damage (included above). When the munsahir successfully performs a [[Grapple]], [[Reposition]], or [[Shove]], they also deal 1d6 fire damage to their target."
armorclass:
  - name: AC
    desc: "17; **Fort** +10, **Ref** +5, **Will** +8"
health:
  - name: HP
    desc: "40; **Immunities** fire; **Weaknesses** cold 4"
abilities_mid:
  - name: "Heat of the Forge"
    desc: "10 feet. A munsahir's skin radiates heat like forge fire. A creature that starts its turn in the area must succeed at a DC 16 [[Fortitude]] save or become [[Fatigued]] while it remains in the area. Creatures immune to environmental heat effects or with any fire resistance are immune."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Warhammer +9 (`pf2:1`) (shove), **Damage** 1d8+3 bludgeoning"
  - name: "Melee strike"
    desc: "Light Hammer +9 (`pf2:1`) (agile), **Damage** 1d6+3 bludgeoning"
  - name: "Melee strike"
    desc: "Light Hammer +7 (`pf2:1`) (agile, thrown 20), **Damage** 1d6+3 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Scorch"
    desc: "`pf2:2` **Requirements** The munsahir is wielding a light hammer <br>  <br> **Effect** The munsahir shrouds the light hammer in flames and hurls it forward, dealing @Damage[2d6[fire]|options:area-damage] damage to each creature in a @Template[type:line|distance:20] (DC 16 [[Reflex]] save)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Munsahirs are an elemental people living on the Plane of Fire, often crudely described by mortals as brassy dwarves. They have stout, wide bodies with broad shoulders, shining metallic skin, and heads wreathed in flame.

Munsahir society is organized into traditional roles inherited along their familial lines, and a munsahir's role is indicated clearly by the metals they wear in their armored kilts. Their culture focuses on tradition and history, placing high value on obedience and conformity within one's community, and as a result it's slow to change. Many munsahirs take pride in their ancestral roles and in fulfilling their inherited duties, providing needed services within their communities.

Long ago, traditional munsahir values of self-sufficiency and close community led them to build mighty fortresses across the Plane of Fire, where they isolated themselves from other planar denizens and even other munsahir communities. These values, sadly, also led to their downfall. Without any connections to or regular communication with other settlements, these fortresses were easily conquered by the ifrits of Medina Mudii'a, the dominant power on the Plane of Fire. Now most munsahir fortresses lie abandoned and ruined, with free holds so few and far between that most think them all lost.

Munsahirs born within the ifrits' Dominion of Flame belong to the populations that were conquered and assimilated into the empire ages ago. They live in perpetual service to the empire, disconnected from their history and culture, yet have formed their own close-knit society in Medina Mudii'a under the fire genies' harsh rule. A handful of munsahir communities have escaped ifrit conquest, most often by [[Fleeing]] far from the genies' realms. Some of these munsahirs now reside in hot, volcanic areas of the Darklands on Golarion, while others have fled to the remote depths within the Plane of Fire. Prying outsiders nevertheless perpetually seek out these settlements, longing for legendary munsahir-crafted goods.

```statblock
creature: "Munsahir"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
