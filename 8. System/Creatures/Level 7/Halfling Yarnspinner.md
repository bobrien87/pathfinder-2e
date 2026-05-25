---
type: creature
group: ["Halfling", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Halfling Yarnspinner"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Halfling"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14"
languages: "Common, Halfling"
skills:
  - name: Skills
    desc: "Arcana +16, Deception +16, Diplomacy +16, Intimidation +14, Occultism +17, Performance +19, Religion +15, Society +15, History Lore +19"
abilityMods: ["-1", "+4", "+0", "+4", "+3", "+5"]
abilities_top:
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the [[Seek]] action to find [[Hidden]] or [[Undetected]] creatures within 30 feet of them. Whenever the halfling targets a creature that is [[Concealed]] or hidden from them, reduce the DC of the flat check to DC 3 flat check for a concealed target or DC 9 flat check for a hidden one."
  - name: "Tale Specialist"
    desc: "For encounters involving storytelling, local history, or lore, the yarnspinner is a 10th-level challenge."
  - name: "Resonant Weapons"
    desc: "If the yarnspinner's Mesmerizing Tale aura is active or they have cast a spell within the last round, their Strikes with magic weapons deal an additional 2d10 sonic damage."
armorclass:
  - name: AC
    desc: "24; **Fort** +11, **Ref** +15, **Will** +18"
health:
  - name: HP
    desc: "110"
abilities_mid:
  - name: "Guidance Through Tales"
    desc: "`pf2:r` **Trigger** An ally the yarnspinner can see fails a skill check <br>  <br> **Effect** The yarnspinner offers a brief reminder about a legendary hero, granting their ally a +2 circumstance bonus to the triggering skill check, potentially turning the failure into a success."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +16 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 1d6+3 piercing plus [[Resonant Weapons]]"
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Halfling Sling Staff +16 (`pf2:1`) (magical, propulsive, reload 1, range 30 ft.), **Damage** 1d10+3 bludgeoning plus [[Resonant Weapons]]"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 26, attack +18<br>**4th** (3 slots) [[Confusion]], [[Honeyed Words]], [[Translocate]]<br>**3rd** (4 slots) [[Haste]], [[Heroism]], [[Ring of Truth]]<br>**2nd** (4 slots) [[Invisibility]], [[Laughing Fit]], [[Revealing Light]]<br>**1st** (4 slots) [[Daze]], [[Detect Magic]], [[Figment]], [[Illusory Disguise]], [[Illusory Object]], [[Light]], [[Mindlink]], [[Read Aura]], [[Soothe]], [[Soothe]], [[Ventriloquism]]"
abilities_bot:
  - name: "Mesmerizing Tale"
    desc: "`pf2:2` The yarnspinner weaves a long-winded but captivating narrative that enchants those nearby. Any creature that's in a @Template[type:emanation|distance:20] or starts its turn in the aura must attempt a DC 24 [[Will]] save. The Mesmerizing Tale lasts until the end of the yarnspinner's next turn, but can be Sustained. The first time the yarnspinner Sustains the aura on subsequent rounds, the aura expands by 10 feet, to a maximum of 60 feet. <br> - **Critical Success** The creature is unaffected, and is temporarily immune for 24 hours. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature becomes [[Fascinated]] with the yarnspinner until the start of its next turn, and must spend all its actions to move closer to the yarnspinner and listen to the tale."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Yarnspinners weave captivating tales that entertain, educate, and preserve the rich heritage of the halfling people across generations.

Halflings thrive on simple pleasures—having a pint at the pub or warming their feet by the hearth.

```statblock
creature: "Halfling Yarnspinner"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
