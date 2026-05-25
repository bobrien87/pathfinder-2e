---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Merchant"
level: "-1"
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
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +10, Diplomacy +12, Performance +8, Society +8, Mercantile Lore +12"
abilityMods: ["+2", "+0", "-1", "+2", "+2", "+3"]
abilities_top:
  - name: "Appraising Eye"
    desc: "The merchant can use Mercantile Lore to [[Recall Knowledge]] about items, including determining their value. They can also attempt to [[Identify Magic]] using Mercantile Lore and can do so without first knowing whether the item is magical."
  - name: "Sales Specialist"
    desc: "For encounters involving negotiation or mercantile skill, a merchant is a 4th-level challenge."
armorclass:
  - name: AC
    desc: "13; **Fort** +1, **Ref** +2, **Will** +10"
health:
  - name: HP
    desc: "7"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +4 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Club +4 (`pf2:1`), **Damage** 1d6+2 bludgeoning"
  - name: "Melee strike"
    desc: "Club +4 (`pf2:1`) (thrown 10), **Damage** 1d6+2 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Small settlements can typically support one or two generalist merchants, and larger cities house multiple specialists—experts in one type of product. Merchants range from vendors hustling in the public square to wealthy tycoons running entire commercial organizations. A merchant might have an additional Lore skill about a specific category of item (such as jewelry or magic weapons), with a skill modifier equal to their Mercantile Lore.

Expertise is forged through years of effort and often tedious work. Artisans are masters of their craft, able to create works both practical and beautiful.

```statblock
creature: "Merchant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
