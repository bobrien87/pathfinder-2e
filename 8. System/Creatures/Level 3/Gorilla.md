---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gorilla"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +11, Stealth +7"
abilityMods: ["+4", "+2", "+3", "-4", "+1", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +12, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "45"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d6+4 bludgeoning"
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (unarmed), **Damage** 1d8+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Frightening Display"
    desc: "`pf2:2` The gorilla beats its chest in a terrifying display. Creatures within @Template[emanation|distance:30]{30 feet} must attempt a DC 20 [[Will]] save. <br>  <br> While a creature is frightened by this ability, it is [[Off Guard]] to the gorilla. <br> - **Critical Success** No effect and temporarily immune for 1 minute. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature is [[Frightened]] 1. <br> - **Critical Failure** The creature is [[Frightened]] 2."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Gorillas can be territorial creatures, particularly if provoked by hunters or the presence of more dangerous monsters. A gorilla uses its fangs and powerful arms to bite and pummel trespassers with wild abandon.

While many apes exhibit peaceful or reclusive behavior, gorillas can be territorial, and the megaprimatus is especially aggressive and dangerous.

```statblock
creature: "Gorilla"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
