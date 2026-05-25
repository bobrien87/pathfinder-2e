---
type: creature
group: ["Dwarf", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dwarf Warrior"
level: "1"
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
    desc: "+7; [[Darkvision]]"
languages: "Common, Dwarven"
skills:
  - name: Skills
    desc: "Athletics +7, Crafting +5, Diplomacy +3, Dwarven Lore +5"
abilityMods: ["+4", "+1", "+3", "+1", "+3", "-1"]
abilities_top:
  - name: "Dwarven Doughtiness"
    desc: "A dwarf is often calm and collected in the face of imminent danger. At the end of this dwarf's turn, reduce their frightened condition by 2 instead of 1."
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +3, **Will** +5"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Warhammer +8 (`pf2:1`) (shove), **Damage** 1d8+2 bludgeoning"
  - name: "Melee strike"
    desc: "Clan Dagger +8 (`pf2:1`) (agile, parry, versatile b), **Damage** 1d4+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Shielded Charge"
    desc: "`pf2:2` The dwarf warrior Raises a Shield and Strides twice."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Between their finely crafted equipment and natural bravery, a dwarf warrior can hold their ground against mighty foes. If respected, these warriors can become life-long allies; if slighted, they can become a thorn in one's side for the remainder of one's life.

A dwarf's strength comes from their stoic determination, quality equipment, and their ability to hold grudges for centuries.

```statblock
creature: "Dwarf Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
