---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Traveling Priest of Desna"
level: "9"
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
    desc: "+19"
languages: "Common, Elven, Empyrean"
skills:
  - name: Skills
    desc: "Acrobatics +17, Diplomacy +17, Religion +21, Society +16, Survival +19"
abilityMods: ["+2", "+4", "+1", "+1", "+4", "+2"]
abilities_top:
  - name: "Path of the Faithful"
    desc: "The pilgrim can evangelize their religious teachings to use their Religion modifier instead of Diplomacy to `act gather-information skill=religion` or `act make-an-impression skill=religion`."
  - name: "Traveler's Lesson"
    desc: "Creatures that engage in conversation with the traveling priest gain a +2 circumstance bonus to all [[Recall Knowledge]] checks and [[Gather Information]] checks for 4 hours related to any topics discussed with the traveling priest."
  - name: "Blessing of Travel"
    desc: "If the traveling priest takes an action with the move trait, their Strikes deal an extra 2d8 spirit damage until the end of their turn."
armorclass:
  - name: AC
    desc: "27; **Fort** +16, **Ref** +19, **Will** +19"
health:
  - name: HP
    desc: "140"
abilities_mid:
  - name: "Messenger's Amnesty"
    desc: "A traveling priest with a message to deliver is continually protected by a DC 25 [[Sanctuary]] spell. If the traveling priest breaks the *sanctuary*, the effect returns if the traveling priest ceases hostility for 10 minutes."
  - name: "Zealous Rush"
    desc: "`pf2:r` **Trigger** The traveling priest casts a spell that takes 1 or more actions and affects only them <br>  <br> **Effect** The traveling priest Strides up to 10 feet, or up to their full Speed if the triggering spell took 2 actions or more to cast."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Starknife +20 (`pf2:1`) (agile, deadly d6, finesse, magical, versatile s), **Damage** 2d4+8 piercing"
  - name: "Melee strike"
    desc: "Starknife +20 (`pf2:1`) (agile, deadly d6, magical, thrown 20, versatile s), **Damage** 2d4+8 piercing"
  - name: "Melee strike"
    desc: "Fist +19 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 27, attack +19<br>**5th** (7 slots) [[Heal]], [[Heal]], [[Heal]], [[Heal]], [[Heal]], [[Translocate]], [[Sending]]<br>**4th** (3 slots) [[Sleep]], [[Spiritual Armament]], [[Unfettered Movement]]<br>**3rd** (3 slots) [[Dream Message]], [[Holy Light]], [[Safe Passage]]<br>**2nd** (3 slots) [[Create Food]], [[Environmental Endurance]], [[Silence]]<br>**1st** (3 slots) [[Alarm]], [[Create Water]], [[Ventriloquism]]<br>**Cantrips** [[Detect Magic]], [[Divine Lance]], [[Know the Way]], [[Light]], [[Read Aura]]"
  - name: "Cleric Domain Spells"
    desc: "DC 27, attack +19<br>**4th** [[Traveler's Transit]]<br>**1st** [[Agile Feet]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Deities and their religions are only as strong as the belief of their faithful. Traveling priests spread word to all corners of Golarion, building the numbers devoted to their denomination through their journeys. No matter where they may be headed or found, a traveling priest is likely to be healing someone with a spell, delivering a message, or simply trying to ensure their faith is spread.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Traveling Priest of Desna"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
