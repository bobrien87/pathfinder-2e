---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mime"
level: "3"
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
    desc: "+11"
languages: "Common (sign language)"
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +8, Deception +10, Performance +10, Stealth +10"
abilityMods: ["+1", "+3", "+0", "+1", "+2", "+4"]
abilities_top:
  - name: "Mimicry Specialist"
    desc: "For encounters involving mimicry or pantomime, the mime is a 6th-level challenge."
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +9, **Will** +12"
health:
  - name: HP
    desc: "45; **Resistances** sonic 5"
abilities_mid:
  - name: "Skill Mimicry"
    desc: "The mime receives a +1 circumstance bonus to skill checks to perform actions they have witnessed another creature successfully perform in the last minute, or +2 if they witness a creature critically succeed instead."
  - name: "Versatile Performance"
    desc: "The mime can use Performance instead of Diplomacy to `act make-an-impression statistic=performance`, instead of Intimidation to `act demoralize statistic=performance`, and instead of Deception to `act impersonate statistic=performance`."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Mimic Assault"
    desc: "`pf2:2` **Frequency** once per round <br>  <br> **Requirements** A creature damaged the mime with a weapon Strike since their previous turn <br>  <br> **Effect** The mime makes a Performance check against the Perception DC of the creature who damaged them, gesturing as if making an attack with the same weapon. On a success, the mime deals two dice of damage to the creature, using the same type and die size as the required weapon Strike."
  - name: "Pantomime"
    desc: "`pf2:2` The mime uses exaggerated movements to emulate one of the following effects, which lasts until the end of their next turn. Any creature who sees this ability can attempt to disbelieve this ability as it is used with a DC 14 [[Will]] save. Creatures that disbelieve are temporarily immune to pantomime for 1 minute. <br>  <br> *Barrier*: The mime creates an invisible @Template[square|distance:10]{10-foot-by-10-foot} stretch of wall adjacent to them and within their reach. The wall has AC 10, 5 hardness, and 10 HP. If the mime Sustains this effect, they can add an additional wall in the same manner. <br>  <br> *Rope*: The mime tugs an invisible rope, trying to knock over or pull at a creature within 15 feet. If the creature fails to disbelieve the pantomime, the mime can choose to either knock the creature [[Prone]] or to move it 5 feet towards them. <br>  <br> *Wind*: The mime creates a @Template[type:line|distance:30] of imaginary wind. Creatures who don't disbelieve the pantomime treat this area as difficult terrain, and if they enter or begin their turn in the area, they fall prone."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Mimes are performers who use movement, gestures, and expressions without any speech to act out a scene or situation for onlookers.

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Mime"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
