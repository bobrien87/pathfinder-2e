---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mage for Hire"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Arcana +11, Society +9, Stealth +7, Thievery +9"
abilityMods: ["+0", "+2", "+1", "+4", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +9, **Will** +10"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +7 (`pf2:1`) (two hand d8), **Damage** 1d4 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 20, attack +12<br>**2nd** (3 slots) [[Floating Flame]], [[Knock]], [[See the Unseen]]<br>**1st** (4 slots) [[Force Barrage]], [[Grease]], [[Mystic Armor]], [[Sure Strike]]<br>**Cantrips** [[Daze]], [[Detect Magic]], [[Electric Arc]], [[Light]], [[Message]], [[Shield]], [[Telekinetic Hand]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Some mercenaries sell magical talents to earn a living. While there are many types of mages for hire, some of the sneakiest are specialized in scrying, using their skills for infiltration and sabotage.

Whether they're hired to wage war, protect a caravan, or infiltrate an impenetrable fortress, there's ample work for mercenaries all over Golarion.

```statblock
creature: "Mage for Hire"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
