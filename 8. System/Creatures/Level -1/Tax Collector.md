---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tax Collector"
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
    desc: "Deception +8, Diplomacy +8, Intimidation +8, Society +9, Thievery +6, Legal Lore +9, Mercantile Lore +10"
abilityMods: ["+0", "+1", "+0", "+3", "+2", "+2"]
abilities_top:
  - name: "DC 19 Against Stealing"
    desc: ""
  - name: "Financial Specialist"
    desc: "When dealing with matters of taxes and finance, the tax collector is a 3rd-level challenge."
armorclass:
  - name: AC
    desc: "14; **Fort** +2, **Ref** +3, **Will** +8"
health:
  - name: HP
    desc: "6"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +5 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4 piercing"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +5 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8 piercing"
spellcasting: []
abilities_bot:
  - name: "Glittering Distraction"
    desc: "`pf2:1` The tax collector Strides. At any point during this movement, they can Interact to hurl coins. If there are Commoners about, this typically causes a scene. Crowds are usually difficult terrain and have other effects."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Ledgers and marks, positive and negative flows, and levies and allotments are a tax collector's daily bread. Where coin is gained, from whom it's collected, and to whom it's disbursed are their concerns—not who can afford the taxes.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Tax Collector"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
