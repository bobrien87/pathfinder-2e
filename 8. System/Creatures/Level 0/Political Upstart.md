---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Political Upstart"
level: "0"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +8, Diplomacy +10, Performance +10, Society +11, Legal Lore +11"
abilityMods: ["+0", "+1", "+0", "+2", "+2", "+3"]
abilities_top:
  - name: "Rhetoric Specialist"
    desc: "For social encounters involving debate and legal logic, the political upstart is a 3rd-level challenge."
armorclass:
  - name: AC
    desc: "14; **Fort** +4, **Ref** +7, **Will** +10"
health:
  - name: HP
    desc: "15"
abilities_mid:
  - name: "+3 to Sense Motive"
    desc: ""
  - name: "Retort"
    desc: "`pf2:r` A creature fails a Charisma-based skill check against the political upstart <br>  <br> **Effect** The political upstart targets the creature with Fiery Rhetoric."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Fascinating Speech"
    desc: "`pf2:2` The political upstart begins a rousing speech which they can Sustain up to 1 minute. Any creature within 30 feet that can hear the speech, must attempt a DC 17 [[Will]] save. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature is [[Fascinated]] with the upstart for 1 round. <br> - **Critical Failure** The creature is fascinated with the upstart as long as the speech lasts."
  - name: "Fiery Rhetoric"
    desc: "`pf2:1` The upstart rattles off talking points at an enemy within 30 feet. The target takes a –2 status penalty to Perception and Will saves for 1 minute. <br>  <br> > [!danger] Effect: Fiery Rhetoric"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Fiery and heady, a political upstart actively pushes against the status quo.

These lone wolves have an aura of mystery, bravado, and swagger.

```statblock
creature: "Political Upstart"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
