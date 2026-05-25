---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Penitent of Calistria"
level: "0"
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
    desc: "+4"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +6, Deception +5, Intimidation +3, Religion +4, Calistria Lore +6"
abilityMods: ["+2", "+1", "+2", "+0", "+2", "+1"]
abilities_top:
  - name: "Agonizing Drive"
    desc: "The penitent ignores the penalty to attack rolls from being [[Frightened]] and gains a status bonus to damage rolls equal to their frightened value."
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +5, **Will** +6"
health:
  - name: HP
    desc: "18"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Whip +6 (`pf2:1`) (disarm, nonlethal, reach, trip), **Damage** 1d4+2 slashing"
  - name: "Melee strike"
    desc: "Dagger +6 (`pf2:1`) (agile, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +5 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Repentant Defiance"
    desc: "`pf2:2` The penitent Strikes, then increases their own [[Frightened]] value by 2 and deals 3 slashing damage to themselves, bypassing resistance. The penitent then gains resistance 3 to physical damage until the start of their next turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Atonement is seen as an ultimate act of supplication for those who have wronged their faith. Repentance takes several forms—acts of service, a pilgrimage, flagellation, or divine quests.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Penitent of Calistria"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
