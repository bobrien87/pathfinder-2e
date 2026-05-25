---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sibyl"
level: "3"
rare_01: "Uncommon"
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
    desc: "+9; [[Lifesense]] (precise) 60 feet"
languages: "Common"
skills:
  - name: Skills
    desc: "Diplomacy +9, Occultism +9, Performance +9, Religion +11"
abilityMods: ["+0", "+3", "-1", "+2", "+2", "+4"]
abilities_top:
  - name: "Induce Awe"
    desc: "The sibyl can use Religion instead of Intimidation to `act coerce skill=religion` or `act demoralize skill=religion`."
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +8, **Will** +12"
health:
  - name: HP
    desc: "40"
abilities_mid:
  - name: "Foresight"
    desc: "`pf2:r` **Trigger** The sibyl becomes the target of a spell with the detection, prediction, revelation, or scrying trait <br>  <br> **Effect** The sibyl's oracular awareness alerts them to danger. They gain a +2 circumstance bonus to their saving throw or AC against the spell."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+4 piercing plus 1d6 spirit"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+4 piercing plus 1d6 spirit"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning plus 1d6 spirit"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 19, attack +11<br>**2nd** (3 slots) [[Augury]], [[Darkness]], [[Sudden Blight]]<br>**1st** (4 slots) [[Command]], [[Concordant Choir]], [[Detect Magic]], [[Divine Lance]], [[Fear]], [[Guidance]], [[Haunting Hymn]], [[Know the Way]], [[Mindlink]]"
  - name: "Oracle Focus Spells"
    desc: "DC 19, attack +11<br>**1st** [[Brain Drain]]"
abilities_bot:
  - name: "Divine Frenzy"
    desc: "`pf2:1` **Requirements** The sibyl isn't [[Fatigued]] or in a frenzy <br>  <br> **Effect** The sibyl enters into a divine frenzy that lasts 1 minute. The sibyl can't voluntarily stop frenzying. While in a divine frenzy, the sibyl takes a –2 penalty to Perception checks and Will saves and gains a +2 status bonus to their spell DC and spell attack modifier. During a divine frenzy, the sibyl can't use actions with the concentrate trait unless they're Casting a Spell or Seeking. The frenzy lasts for 1 minute, until the sibyl falls [[Unconscious]], or the encounter ends, whichever comes first. The sibyl can't voluntarily end the frenzy."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Sibyls are oracular diviners who often fall deep into trances with their oracular curses to spur a frenzied mental state. In this trance, they connect with gods and spirits, albeit in a disorganized haze. Some false sibyls will use substances to try and attempt to bring on this same frantic connection, often with deadly results.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Sibyl"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
