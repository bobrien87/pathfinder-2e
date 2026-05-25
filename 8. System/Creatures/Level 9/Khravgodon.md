---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Khravgodon"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +16, Stealth +18, Survival +18"
abilityMods: ["+6", "+3", "+5", "-4", "+3", "+0"]
abilities_top:
  - name: "Grasping Tail"
    desc: "A khravgodon can drag a Large or smaller creature it has [[Grabbed]] with its tail along with it when it Strides."
armorclass:
  - name: AC
    desc: "27; **Fort** +20, **Ref** +18, **Will** +16"
health:
  - name: HP
    desc: "160; **Resistances** acid 10, poison 10"
abilities_mid:
  - name: "+2 Circumstance to All Saves vs. Disease"
    desc: ""
  - name: "Feign Death"
    desc: "`pf2:r` **Trigger** The khravgodon is reduced below 70 HP <br>  <br> **Effect** The khravgodon collapses. It is [[Off Guard]] and can use actions that require only its mind, but any other action ends the ruse. <br>  <br> A successful DC 18 [[Perception]] check to [[Seek]] or DC 18 [[Medicine]] check to [[Recall Knowledge]] is required to determine that the animal is not, in fact, dead."
  - name: "Revived Retaliation"
    desc: "`pf2:r` **Trigger** The khravgodon is attacked or disturbed by a creature within reach while Feigning Death <br>  <br> **Effect** The khravgodon Strikes the triggering creature."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +21 (`pf2:1`) (deadly d12, unarmed), **Damage** 2d12+9 piercing"
  - name: "Melee strike"
    desc: "Claw +21 (`pf2:1`) (agile, unarmed), **Damage** 2d10+9 slashing"
  - name: "Melee strike"
    desc: "Tail +21 (`pf2:1`) (reach 20 ft.), **Damage** 2d6+9 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Crush Chitin"
    desc: "`pf2:1` **Requirements** The khravgodon has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The khravgodon bites the creature, dealing @Damage[(2d12+9)[piercing]] damage (DC 28 [[Fortitude]] save) that ignores the first 5 of the target's Hardness or resistance to physical damage. On a failed save, the target also takes a -2 circumstance penalty to AC for 1 round. <br>  <br> > [!danger] Effect: Crush Chitin"
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Few creatures can shrug off an ankhrav's acid and crunch its chitin like a khravgodon.

Few creatures have survived as long and in as many environments as the opossum.

```statblock
creature: "Khravgodon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
