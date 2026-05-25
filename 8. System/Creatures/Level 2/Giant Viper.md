---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Viper"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +8, Stealth +8, Survival +6"
abilityMods: ["+3", "+4", "+3", "-4", "+1", "-2"]
abilities_top:
  - name: "Giant Viper Venom"
    desc: "**Saving Throw** DC 17 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage (1 round) <br>  <br> **Stage 2** 1d6 poison damage and [[Drained]] 1"
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +11, **Will** +6"
health:
  - name: HP
    desc: "26"
abilities_mid:
  - name: "Coiled Strike (Special)"
    desc: "`pf2:r` As Reactive Strike, but the snake can use this reaction only if it's Coiled. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +11 (`pf2:1`) (finesse), **Damage** 1d8+3 piercing plus [[Giant Viper Venom]]"
spellcasting: []
abilities_bot:
  - name: "Coil"
    desc: "`pf2:1` The giant viper uses an action to coil itself. While Coiled, the reach of its fangs is 10 feet and it has the Reactive Strike reaction. After the giant viper Strikes with its fangs, it becomes uncoiled."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The giant viper's fangs are a frightening sight, with injection tubes as long as daggers. The sheer amount of venom injected by a giant viper can cause severe blood clotting and leave a victim utterly drained of vitality.

Snakes come in an array of forms, from jungle-dwelling constrictors that wrap around their prey to venomous vipers with deadly bites. Regardless, all snakes consume their prey whole by unhinging their jaws and using powerful muscles to move the food down their throats and into their stomachs.

```statblock
creature: "Giant Viper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
