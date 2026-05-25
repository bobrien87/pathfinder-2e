---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Blasphemer of Zon-Kuthon"
level: "2"
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
languages: "Common, Shadowtongue"
skills:
  - name: Skills
    desc: "Deception +9, Intimidation +7, Performance +7, Religion +6, Society +7"
abilityMods: ["+3", "+1", "+0", "+1", "+2", "+3"]
abilities_top:
  - name: "Twisted Faith"
    desc: "When attempting a Religion skill check, the blasphemer can roll [[Deception]] check instead, so long as they have an intelligent creature around as a witness. If the creature is a follower of the blasphemer's faith, the blasphemer receives a +2 circumstance bonus to the check."
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +7, **Will** +10"
health:
  - name: HP
    desc: "35"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spiked Chain +9 (`pf2:1`) (disarm, trip), **Damage** 1d8+5 slashing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +7 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot:
  - name: "False Blessing"
    desc: "`pf2:1` The blasphemer attempts a DC 15 [[Religion]] check to attempt to cast the 1st-rank spell their deity grants to clerics ([[Phantom Pain]] for Zon-Kuthon). The spell must take 1, 2, or 3 actions to Cast. The blasphemer can use twisted faith to roll DC 15 [[Deception]] check instead if they have a witness, as normal. <br> - **Critical Success** The blasphemer successfully Casts the Spell, then is [[Stunned]] with a value equal to the number of actions the spell takes – 1. <br> - **Success** As critical success, plus the blasphemer takes 1d6 mental damage. <br> - **Failure** The blasphemer fails to Cast the Spell and takes 1d6 mental damage. <br> - **Critical Failure** The blasphemer fails to Cast the Spell, takes 2d6 mental damage, and is [[Stunned]] 1."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Blasphemers spread messages contrary to the tenets of their faith, often out of the belief that the gods are specifically targeting them to spread this message. In some cultures, such as Nidal, this is a heretical crime and can send a blasphemer on the run from the law.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Blasphemer of Zon-Kuthon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
