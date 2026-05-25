---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Executioner"
level: "6"
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
    desc: "+12"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +15, Intimidation +13, Medicine +10"
abilityMods: ["+5", "+2", "+3", "-1", "+2", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +15, **Ref** +12, **Will** +14"
health:
  - name: HP
    desc: "105"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greataxe +16 (`pf2:1`) (magical, sweep), **Damage** 1d12+9 slashing"
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+9 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Behead"
    desc: "`pf2:3` **Requirements** The executioner is adjacent to a dying creature or a creature specifically prepared for a killing blow <br>  <br> **Effect** The executioner Strikes the creature with their greataxe. On a hit, in addition to taking damage, the target must attempt a DC 23 [[Fortitude]] save or be reduced to 0 HP and become [[Dying]] 1. If the creature was already dying (including if it was reduced to 0 HP by the Strike's damage), the creature's dying value increases by 1, in addition to any increase from the Strike. On a critical failure, the creature dies instantly. If the executioner's Strike was a critical hit, the target uses the outcome one degree of success worse than the result of their saving throw."
  - name: "Intimidating Strike"
    desc: "`pf2:2` The executioner makes a melee Strike. If it hits and deals damage, the target is [[Frightened]] 1, or [[Frightened]] 2 on a critical hit."
  - name: "Mark for Death"
    desc: "`pf2:1` The executioner marks a single creature they can see for death. The first time each round the executioner Strikes that creature, the Strike deals an extra 1d12 precision damage. <br>  <br> The creature remains marked for death until the executioner is knocked out, marks a different creature for death, or the encounter ends."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Executioners carry out sentences from cruel tyrants and legitimate rulers alike. Most remain numb to the necessity of their duty, but some evil executioners grow to love the power of having someone else's life in their hands.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Executioner"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
