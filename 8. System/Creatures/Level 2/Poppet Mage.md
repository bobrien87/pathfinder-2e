---
type: creature
group: ["Construct", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Poppet Mage"
level: "2"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Construct"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Common (two languages their creator speaks)"
skills:
  - name: Skills
    desc: "Arcana +8, Crafting +8, Diplomacy +6, Occultism +8"
abilityMods: ["+1", "+1", "+0", "+4", "+3", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +5, **Will** +11"
health:
  - name: HP
    desc: "30; **Weaknesses** fire 3"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +9 (`pf2:1`) (two hand d8), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal), **Damage** 1d4+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +9 (`pf2:1`) (range 60 ft.), **Damage** 1d6+3 piercing"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 18, attack +10<br>**1st** (3 slots) [[Dizzying Colors]], [[Mending]], [[Sleep]]<br>**Cantrips** [[Daze]], [[Figment]], [[Prestidigitation]], [[Shield]], [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Magic Hat"
    desc: "`pf2:2` **Frequency** one per day <br>  <br> **Requirements** The poppet mage has a free hand <br>  <br> **Effect** The poppet mage pulls off their hat, and with a jaunty display, pulls one of the following items from their hat: a lesser glue bomb, a lesser smoke ball, or a minor healing potion. This consumable lasts for 1 hour before becoming inert."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

With extra time, care, and patience, poppets can be woven with magic, making them talented little spellcasters.

Poppets are simple constructs made to assist their creators with basic tasks.

```statblock
creature: "Poppet Mage"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
