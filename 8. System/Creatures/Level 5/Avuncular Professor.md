---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Avuncular Professor"
level: "5"
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
    desc: "+12"
languages: "Common (up to 4 additional languages, including at least one obscure or long-dead language that the avuncular professor likes to quote)"
skills:
  - name: Skills
    desc: "Deception +18, Diplomacy +18, Occultism +12, Performance +18, Society +16, Academia Lore +16, One Additional Lore +18"
abilityMods: ["+0", "+0", "+1", "+4", "+3", "+4"]
abilities_top:
  - name: "Academic Politics Specialist"
    desc: "When it comes to wining and dining or other social situations, the avuncular professor is an 8th-level challenge."
  - name: "Duelist of Wits"
    desc: "The avuncular professor may cultivate the appearance of an unworldly academic, but they know how to stick the rhetorical knife in. Once per hour, if the avuncular professor succeeds at a Deception or Diplomacy check, they can choose to roll a Society or Academia Lore check at the same DC—if they succeed on the second check, the initial success is upgraded to a critical success, though if they fail the second check, their initial success also turns into a failure."
armorclass:
  - name: AC
    desc: "21; **Fort** +12, **Ref** +11, **Will** +15"
health:
  - name: HP
    desc: "75"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sword Cane +11 (`pf2:1`) (agile, concealable), **Damage** 1d6+6 piercing"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 22, attack +14<br>**3rd** (2 slots) [[Enthrall]], [[Hypnotize]]<br>**2nd** (3 slots) [[Calm]], [[Laughing Fit]], [[Translate]]<br>**1st** (3 slots) [[Command]], [[Detect Magic]], [[Fear]], [[Figment]], [[Light]], [[Prestidigitation]], [[Sigil]], [[Ventriloquism]]"
  - name: "Bard Composition Spells"
    desc: "DC 22, attack +14<br>**1st** [[Uplifting Overture]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

These world-wise scholars know that there's more to life than just research. There are also good meals at the university refectory, comfortable beds, and captive audiences of students.

True power comes from knowledge—the power to shape the growth of kingdoms by mere whispers, stay three steps ahead of adversaries, or even know which flora is best for creating untraceable poisons.

```statblock
creature: "Avuncular Professor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
