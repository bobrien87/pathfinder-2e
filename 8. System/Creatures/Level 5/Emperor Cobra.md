---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Emperor Cobra"
level: "5"
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
    desc: "+13; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +13, Survival +11"
abilityMods: ["+6", "+4", "+4", "-4", "+2", "-2"]
abilities_top:
  - name: "Emperor Cobra Venom"
    desc: "**Saving Throw** DC 22 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d8 poison damage (1 round) <br>  <br> **Stage 2** 1d8 poison damage and [[Drained]] 1 (1 round) <br>  <br> **Stage 3** 2d6 poison damage and [[Drained]] 2 (1 round)"
armorclass:
  - name: AC
    desc: "21; **Fort** +15, **Ref** +11, **Will** +9"
health:
  - name: HP
    desc: "80"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +15 (`pf2:1`) (reach 10 ft.), **Damage** 2d8+8 piercing plus [[Emperor Cobra Venom]]"
spellcasting: []
abilities_bot:
  - name: "Flare Hood"
    desc: "`pf2:1` The emperor cobra flares its hood. Each non–emperor cobra creature within a @Template[type:emanation|distance:20] must attempt a DC 22 [[Will]] save. The creature is then temporarily immune for 1 minute. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 3."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These powerful serpents infest bogs and lowlands. Despite being over 16 feet long and weighing more than 200 pounds, they can climb trees in seconds. Emperor cobras ward off predators by flaring their hoods and hissing at attackers. Like many venomous snakes, they hunt by striking prey with their poison bite, retreating until their victims die, and then returning to swallow them whole.

Snakes of some variety thrive in every non-arctic ecosystem, each with their own particular hunting patterns and defense mechanisms.

```statblock
creature: "Emperor Cobra"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
