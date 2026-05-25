---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Druid Initiate"
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
languages: "Common, Wildsong"
skills:
  - name: Skills
    desc: "Diplomacy +3, Medicine +7, Nature +7, Stealth +4, Survival +7"
abilityMods: ["+2", "+1", "+2", "+0", "+4", "+0"]
abilities_top:
  - name: "Plant Empathy"
    desc: "The druid initiate can ask questions of, receive answers from, and use the Diplomacy skill with plants and fungus."
armorclass:
  - name: AC
    desc: "15; **Fort** +5, **Ref** +4, **Will** +9"
health:
  - name: HP
    desc: "18"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +7 (`pf2:1`) (two hand d8), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +6 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+1 bludgeoning"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 17, attack +0<br>**1st** (2 slots) [[Heal]], [[Thunderstrike]]<br>**Cantrips** [[Detect Magic]], [[Ignition]], [[Know the Way]], [[Light]], [[Tangle Vine]]"
  - name: "Druid Order Spells"
    desc: "DC 17, attack +0<br>**1st** [[Cornucopia]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A neophyte druid learns basic techniques and spellcasting soon after being initiated into their druidic order. The druid initiate has already learned much from their mentors—elders among the order—but hasn't had a chance to develop their own identity.

A primalist is a wielder of primal energies and magic, sometimes taught by forces of primal power, including powerful elementals or fey of the First World. Primalists protect the natural world, offering strong medicine to those in need while facing suspicion from those who don't understand their ways.

A great many primalists belong to druidic circles, and even those who aren't members tend to be familiar with the most prominent ones in their homeland.

```statblock
creature: "Druid Initiate"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
