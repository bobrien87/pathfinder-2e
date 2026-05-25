---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Electric Eel"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +6, Stealth +7"
abilityMods: ["+1", "+2", "+2", "-5", "+1", "-1"]
abilities_top:
  - name: "Stunning Shock"
    desc: "A creature critically hit by the electric eel's tail must attempt a DC 17 [[Fortitude]] save. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Stunned]] 1. <br> - **Failure** The creature is [[Stunned]] 2. <br> - **Critical Failure** The creature is [[Stunned]] 3."
armorclass:
  - name: AC
    desc: "16; **Fort** +7, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "18; **Resistances** electricity 7"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +6 (`pf2:1`) (unarmed), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Tail +6 (`pf2:1`) (agile), **Damage** 1d4+1 bludgeoning plus 1d4 electricity plus [[Stunning Shock]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Usually found in freshwater rivers and lakes, an electric eel is not particularly aggressive, but its ability to stun predators and prey alike can be dangerous to larger creatures searching for their next meal. Electric eels are more closely related to catfish than to other eels.

Although these long, narrow fish share similarities in appearance, eels are a diverse group of creatures.

```statblock
creature: "Electric Eel"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
