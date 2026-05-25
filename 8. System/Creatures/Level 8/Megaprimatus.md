---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Megaprimatus"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +19"
abilityMods: ["+7", "+2", "+5", "-4", "+1", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "26; **Fort** +19, **Ref** +16, **Will** +13"
health:
  - name: HP
    desc: "150"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +21 (`pf2:1`) (agile, reach 20 ft., unarmed), **Damage** 2d8+10 bludgeoning"
  - name: "Melee strike"
    desc: "Jaws +21 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d10+10 piercing"
spellcasting: []
abilities_bot:
  - name: "Mangling Rend"
    desc: "`pf2:2` A megaprimatus makes two fist Strikes against the same target. If both hit, the attack deals an additional 2d6 bludgeoning damage, the target is [[Off Guard]], and the target takes a –20-foot status penalty to all Speeds until the end of its next turn. <br>  <br> > [!danger] Effect: Mangling Rend"
  - name: "Terrifying Display"
    desc: "`pf2:2` The megaprimatus beats its chest in a terrifying display. Creatures within @Template[emanation|distance:50]{50 feet} must attempt a DC 27 [[Will]] save. <br>  <br> While a creature is [[Frightened]] by this ability, it is [[Off Guard]] to the megaprimatus and to gorillas. <br> - **Critical Success** No effect and temporarily immune for 1 minute. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature is [[Frightened]] 1. <br> - **Critical Failure** The creature is [[Frightened]] 2 and [[Fleeing]] until the end of its next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The megaprimatus is among the mightiest of apes, quick to confront any perceived intrusions into its domain. With a height of 40 feet, it towers over even most giants, and is used to being the top-tier predator in the region.

While many apes exhibit peaceful or reclusive behavior, gorillas can be territorial, and the megaprimatus is especially aggressive and dangerous.

```statblock
creature: "Megaprimatus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
