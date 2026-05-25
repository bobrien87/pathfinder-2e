---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Messenger"
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
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +5, Diplomacy +6, Society +7, Survival +4"
abilityMods: ["+0", "+3", "+4", "+0", "+1", "+1"]
abilities_top:
  - name: "Don't Shoot the Messenger"
    desc: "Messengers get a +2 circumstance bonus to [[Diplomacy]] check to convince another creature not to blame them for any news they deliver."
  - name: "Express Messenger"
    desc: "Allies traveling with the messenger gain a +5-foot circumstance bonus to travel Speed, to a maximum of the messenger's travel Speed. If they use the [[Hustle]] activity, they can Hustle for a minimum of 1 hour instead of the usual amount."
  - name: "Road Runner"
    desc: "Messengers can use Society in place of Survival to `act sense-direction skill=society` when they're on a road."
armorclass:
  - name: AC
    desc: "16; **Fort** +7, **Ref** +10, **Will** +4"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +8 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +8 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Fist +8 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +8 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+2 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Special Delivery"
    desc: "`pf2:2` The messenger Interacts to take an item of light Bulk or less held by a willing ally within reach, Strides, then delivers the item to a willing ally in reach at their new location."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

When a message, mail, or package needs to be delivered, messengers make deliveries—typically from large towns and cities or to other towns and cities.

Society is built upon the backs of laborers.

```statblock
creature: "Messenger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
