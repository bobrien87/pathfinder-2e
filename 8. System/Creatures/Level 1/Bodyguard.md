---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bodyguard"
level: "1"
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
    desc: "Athletics +7, Intimidation +6, Society +2"
abilityMods: ["+4", "+2", "+3", "-1", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +8, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "25"
abilities_mid:
  - name: "Bodyguard's Reprisal"
    desc: "`pf2:r` **Trigger** A creature attacks the subject of bodyguard's defense <br>  <br> **Effect** The bodyguard makes a Strike against the triggering creature."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Greatclub +7 (`pf2:1`) (backswing, shove), **Damage** 1d10+4 bludgeoning"
  - name: "Melee strike"
    desc: "Sap +7 (`pf2:1`) (agile, nonlethal), **Damage** 1d6+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +5 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+2 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Bodyguard's Defense"
    desc: "`pf2:1` The bodyguard grants an adjacent ally a +2 circumstance bonus to AC. This lasts until the start of the bodyguard's next turn or until the ally is no longer adjacent, whichever comes first. <br>  <br> > [!danger] Effect: Bodyguard's Defense"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Hired to protect someone famous or powerful, bodyguards use intimidation, quick wits, and martial skill to keep their charges safe. Such mercenaries might be auxiliaries to a noble's personal guards, but with special directives to safeguard their patrons.

Whether they're hired to wage war, protect a caravan, or infiltrate an impenetrable fortress, there's ample work for mercenaries all over Golarion.

```statblock
creature: "Bodyguard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
