---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gigantopithecus"
level: "4"
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
    desc: "+10; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +13, Stealth +9"
abilityMods: ["+4", "+2", "+3", "-4", "+1", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +14, **Ref** +11, **Will** +8"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +13 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d6+6 bludgeoning"
  - name: "Melee strike"
    desc: "Jaws +13 (`pf2:1`) (unarmed), **Damage** 1d8+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Frightening Display"
    desc: "`pf2:2` The gorilla beats its chest in a terrifying display. Creatures within @Template[emanation|distance:30]{30 feet} must attempt a DC 22 [[Will]] save. <br>  <br> While a creature is frightened by this ability, it is [[Off Guard]] to the gigantopithecus. <br> - **Critical Success** No effect and temporarily immune for 1 minute. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature is [[Frightened]] 1. <br> - **Critical Failure** The creature is [[Frightened]] 2."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These fierce kin of orangutans are three times heavier than a gorilla.

While many apes exhibit peaceful or reclusive behavior, gorillas can be territorial, and the megaprimatus is especially aggressive and dangerous.

```statblock
creature: "Gigantopithecus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
