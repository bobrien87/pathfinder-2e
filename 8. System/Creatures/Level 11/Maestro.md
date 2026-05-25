---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Maestro"
level: "11"
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
    desc: "+22"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +21, Deception +23, Diplomacy +23, Intimidation +23, Occultism +19, Performance +30, Society +21, Bardic Lore +19, Music Lore +21"
abilityMods: ["+2", "+4", "+1", "+2", "+3", "+5"]
abilities_top:
  - name: "Bardic Lore"
    desc: "The maestro can [[Recall Knowledge]] on any subject with a +19 modifier."
  - name: "Performing Specialist"
    desc: "For encounters involving acting, music, or storytelling, the maestro is a 15th-level challenge."
  - name: "Resonating Weaponry"
    desc: "The maestro funnels musical energy from their compositions into attacks, dealing additional 1d6 sonic damage with their weapon Strikes on any turn they cast a composition spell."
armorclass:
  - name: AC
    desc: "30; **Fort** +18, **Ref** +24, **Will** +21"
health:
  - name: HP
    desc: "180"
abilities_mid:
  - name: "+1 circumstance bonus to saves vs. auditory, illusion, linguistic, sonic, or visual"
    desc: ""
  - name: "Resolve"
    desc: "When the maestro rolls a success on a Will save, they get a critical success instead."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +24 (`pf2:1`) (deadly d8, disarm, finesse, magical), **Damage** 2d6+10 piercing plus [[Resonating Weaponry]]"
  - name: "Melee strike"
    desc: "Fist +23 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Shortbow +24 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, range 60 ft.), **Damage** 2d6+9 piercing plus [[Resonating Weaponry]]"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 30, attack +22<br>**6th** (2 slots) [[Spirit Blast]], [[Vibrant Pattern]]<br>**5th** (3 slots) [[Illusory Scene]], [[Truespeech]], [[Wave of Despair]]<br>**4th** (3 slots) [[Fly]], [[Translocate]]<br>**2nd** [[Shatter]]<br>**1st** [[Figment]], [[Light]], [[Message]], [[Summon Instrument]], [[Telekinetic Projectile]]"
  - name: "Bard Composition Spells"
    desc: "DC 30, attack +22<br>**3rd** [[Dirge of Doom]]<br>**1st** [[Counter Performance]], [[Courageous Anthem]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A maestro is a performer who has achieved true excellence. These virtuosos can inspire those around them to greater heights or strike fear in their enemies' hearts.

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Maestro"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
