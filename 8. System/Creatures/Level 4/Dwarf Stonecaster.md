---
type: creature
group: ["Dwarf", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dwarf Stonecaster"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Dwarf"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]], [[Tremorsense]] (imprecise) 10 feet"
languages: "Common, Dwarven, Petran"
skills:
  - name: Skills
    desc: "Athletics +11, Crafting +8, Nature +12, Dwarven Lore +8"
abilityMods: ["+4", "+2", "+3", "+2", "+5", "-1"]
abilities_top:
  - name: "Dwarven Doughtiness"
    desc: "A dwarf is often calm and collected in the face of imminent danger. At the end of this dwarf's turn, reduce their frightened condition by 2 instead of 1."
armorclass:
  - name: AC
    desc: "20; **Fort** +11, **Ref** +8, **Will** +14"
health:
  - name: HP
    desc: "70"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +12 (`pf2:1`) (two hand d8), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Clan Dagger +12 (`pf2:1`) (agile, parry, versatile b), **Damage** 1d4+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Boulder Roll"
    desc: "`pf2:2` The stonecaster conjures a rolling boulder that deals @Damage[5d6[bludgeoning]|options:area-damage] damage to each creature in a @Template[line|distance:60] with a DC 21 [[Reflex]] save. <br>  <br> The stonecaster can't use Boulder Roll again for 1d4 rounds."
  - name: "Tremor"
    desc: "`pf2:1` The stonecaster causes the earth below to tremble. Each creature on the ground in a @Template[emanation|distance:10] takes @Damage[2d8[bludgeoning]|options:area-damage] damage with a DC 21 [[Fortitude]] save. A creature that critically fails is knocked [[Prone]]."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

All dwarves share a connection to the earth, but stonecasters have focused and polished that connection. Their years of meditation have granted them the ability to create boulders and shake the very earth. These elemental specialists are often highly respected in their community, which prizes their art of geomancy. Young dwarves who show a stronger than normal connection to the earth might be sent to a stonecaster to train at an early age.

A dwarf's strength comes from their stoic determination, quality equipment, and their ability to hold grudges for centuries.

```statblock
creature: "Dwarf Stonecaster"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
