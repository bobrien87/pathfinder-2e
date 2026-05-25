---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Combat Engineer"
level: "1"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +8, Crafting +13, Engineering Lore +15, Warfare Lore +13"
abilityMods: ["+3", "+2", "+1", "+4", "+2", "+1"]
abilities_top:
  - name: "Logistics Specialist"
    desc: "In situations involving battlefield engineering or logistics, the combat engineer is a 5th-level challenge."
  - name: "Fortify"
    desc: "The combat engineer digs trenches and constructs earthen barricades at a rate of one 5-foot cube per hour. A combat engineer can instead direct the work of four allied Small or larger creatures to quadruple this rate."
armorclass:
  - name: AC
    desc: "15; **Fort** +8, **Ref** +5, **Will** +7"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Entrenching Tool +8 (`pf2:1`) (fatal d10), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Fist +8 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Heavy Crossbow +7 (`pf2:1`) (reload 2, range 120 ft.), **Damage** 1d10 piercing"
spellcasting: []
abilities_bot:
  - name: "Improvised Barricade"
    desc: "`pf2:2` **Requirements** The combat engineer has at least 5 Bulk of loose items or material within reach <br>  <br> **Effect** The combat engineer slaps together a 5-foot high barrier in an adjacent square. The barrier is an object with 10 Hit Points, 5 Hardness, AC 10, and it provides standard cover. After 1 minute, the barrier collapses under its own weight."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Be it a bridge to get a battalion across a river, watchtowers to pierce the fog of war, or fortifications to secure territory, armies have always needed those who can build. The combat engineer is a soldier specializing in these sorts of constructions.

A military serves to defend and fight on behalf of nations and can be trained and deployed in various ways.

```statblock
creature: "Combat Engineer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
