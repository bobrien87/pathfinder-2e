---
type: creature
group: ["Aiuvarin", "Elf"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aiuvarin Translator"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aiuvarin"
trait_02: "Elf"
trait_03: "Human"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Low-Light Vision]]"
languages: "Common, Elven (two other common or uncommon languages)"
skills:
  - name: Skills
    desc: "Arcana +7, Diplomacy +8, Occultism +7, Performance +6, Religion +5, Society +7"
abilityMods: ["+0", "+2", "+0", "+3", "+1", "+2"]
abilities_top:
  - name: "Linguistic Mastery"
    desc: "The translator gains a +5 circumstance bonus to skill checks involving translating or deciphering languages. If the translator rolls a critical failure on a check to [[Decipher Writing]], they get a failure instead."
  - name: "Translation Specialist"
    desc: "For encounters involving translating or deciphering languages, the translator is a 4th-level challenge."
armorclass:
  - name: AC
    desc: "14; **Fort** +2, **Ref** +6, **Will** +9"
health:
  - name: HP
    desc: "12"
abilities_mid:
  - name: "Crosstalk"
    desc: "`pf2:r` **Trigger** A creature within 20 feet of the translator would be targeted by or in the area of an ability with the linguistic trait <br>  <br> **Effect** The translator attempts a Performance check with a +5 circumstance bonus against the Will DC of the creature. On a success, the creature is unaffected by the linguistic effect, and the translator can choose to make the creature [[Confused]] until the end of the creature's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +4 (`pf2:1`) (two hand d8), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Quill Pen +6 (`pf2:1`) (agile, thrown 20), **Damage** 1d4+2 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Many societies recognize aiuvarins' skills as adept translators.

Elves' long lives give them centuries to delve into studies, artistry, or exploration.

```statblock
creature: "Aiuvarin Translator"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
