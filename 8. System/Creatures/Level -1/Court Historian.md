---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Court Historian"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Society +9, Genealogy Lore +13, Noble Court Lore +13, Scribing Lore +13, Settlement Lore +13"
abilityMods: ["+0", "+1", "-1", "+5", "+3", "+2"]
abilities_top:
  - name: "Historical Specialist"
    desc: "In matters regarding history or court records, the court historian is a 5th-level challenge."
  - name: "Records Don't Lie"
    desc: "The court historian has a Perception DC of 25 against Deception checks asserting false current or historical events."
armorclass:
  - name: AC
    desc: "13; **Fort** +3, **Ref** +5, **Will** +9"
health:
  - name: HP
    desc: "7"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
  - name: "Melee strike"
    desc: "Inkwell +5 (`pf2:1`) (thrown 10), **Damage** 1d4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Distracting Diatribe"
    desc: "`pf2:1` The court historian monotonously recites facts to distract a creature within 30 feet that can hear them. The target is [[Off Guard]] for 1 round."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Amid the political machinations of the court stand the court historians, observing and recording events for future generations. Their loyalty is to the preservation of history, and they will defy even royalty in the name of truth.

The denizens of a noble court are the most powerful people in a civilization, primed with wealth, station, and authority above the common people.

```statblock
creature: "Court Historian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
