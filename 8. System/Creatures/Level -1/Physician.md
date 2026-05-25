---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Physician"
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
    desc: "Diplomacy +6, Medicine +12, Society +5"
abilityMods: ["-1", "+1", "+1", "+4", "+2", "+2"]
abilities_top:
  - name: "+2 Bonus on Perception to Notice Ailments"
    desc: ""
  - name: "Bedside Manner"
    desc: "A physician has a +4 circumstance bonus to Diplomacy checks to `act make-an-impression options=bedside-manner` on or make a `act request options=bedside-manner` of a diseased, poisoned, or wounded creature."
  - name: "Doctor's Hand"
    desc: "When the physician rolls a critical failure on a check to [[Treat Disease]], [[Treat Poison]], or [[Treat Wounds]], they get a failure instead."
armorclass:
  - name: AC
    desc: "13; **Fort** +9, **Ref** +3, **Will** +8"
health:
  - name: HP
    desc: "8"
abilities_mid:
  - name: "Medical Specialist"
    desc: "For medical matters, the physician is a 4th-level challenge."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4-1 bludgeoning"
  - name: "Melee strike"
    desc: "Medical Textbook +5 (`pf2:1`) (nonlethal, thrown 10), **Damage** 1d4-1 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The art of medicine is a blend of the intellectual and the practical, concerned with how diseases work and how to prevent them. The physician can be found consulting well-thumbed tomes while meticulously examining patients to better understand their condition, before determining the most effective treatment.

The world is a dangerous place. Thankfully, there are those who devote their lives to easing the pain and suffering of others.

```statblock
creature: "Physician"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
