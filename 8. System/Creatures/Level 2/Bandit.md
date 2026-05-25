---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bandit"
level: "2"
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
    desc: "Athletics +6, Deception +5, Intimidation +6, Stealth +8, Survival +6, Thievery +8, Forest Lore +4"
abilityMods: ["+3", "+3", "+1", "+0", "+2", "+1"]
abilities_top:
  - name: "Bandit's Ambush"
    desc: "When the bandit rolls initiative using Deception or Stealth, they can attempt to `act demoralize` one creature as a free action."
  - name: "Dread Striker"
    desc: "[[Frightened]] creatures are [[Off Guard]] to the bandit."
  - name: "Forest Passage"
    desc: "The bandit ignores any difficult terrain caused by plants, such as bushes, vines, and undergrowth."
armorclass:
  - name: AC
    desc: "19; **Fort** +7, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Machete +9 (`pf2:1`) (deadly d8, sweep), **Damage** 1d6+5 slashing"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, versatile s), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +9 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+3 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Bandits waylay travelers and plunder their valuables before disappearing back to their wilderness hideouts. Many bandits seek only to steal and release their victims alive, though a few prefer to leave no witnesses.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Bandit"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
