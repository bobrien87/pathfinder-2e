---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Animated Armor"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +9"
abilityMods: ["+3", "-3", "+4", "-5", "+0", "-5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17 (13 when broken); construct armor; **Fort** +10, **Ref** +3, **Will** +4"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Construct Armor (Hardness 9)"
    desc: "Like normal objects, an animated armor has Hardness. This Hardness reduces any damage it takes by an amount equal to the Hardness. Once an animated armor is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks and its Armor Class is reduced to 13."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Glaive +10 (`pf2:1`) (deadly d8, forceful, magical, reach 10 ft.), **Damage** 1d8+4 slashing"
  - name: "Melee strike"
    desc: "Gauntlet +9 (`pf2:1`) (agile, free hand, magical), **Damage** 1d6+4 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Suits of animated armor see use both as guardians and as training partners in high-end martial academies able to afford the extravagance. Often, a warrior's old suit of armor can be turned into animated armor once it accrues too much battle damage to provide adequate protection. They're found most often in wizard laboratories and ancient dungeons.

Granted a semblance of life through the use of rituals or other strange magic, animated objects take many forms and serve a variety of uses. A few examples of typical animated objects are listed below. Many of these creatures serve as guardians, surprising unsuspecting adventurers when they suddenly attack. Others serve as idle distractions for the exceptionally rich, simple servants created to handle odd jobs, and the like.

```statblock
creature: "Animated Armor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
