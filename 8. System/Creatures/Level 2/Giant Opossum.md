---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Opossum"
level: "2"
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
    desc: "Athletics +8, Stealth +8, Survival +6"
abilityMods: ["+4", "+2", "+3", "-4", "+2", "+0"]
abilities_top:
  - name: "Grasping Tail"
    desc: "A giant opossum can drag a Small or Tiny creature it has [[Grabbed]] with its tail along with it when it Strides."
armorclass:
  - name: AC
    desc: "17; **Fort** +11, **Ref** +8, **Will** +5"
health:
  - name: HP
    desc: "35; **Resistances** poison 3"
abilities_mid:
  - name: "+2 Circumstance to All Saves vs. Disease"
    desc: ""
  - name: "Feign Death"
    desc: "`pf2:r` **Trigger** The opossum is reduced below 15 HP <br>  <br> **Effect** The opossum collapses. It is [[Off Guard]] and can use actions that require only its mind, but any other action ends the ruse. <br>  <br> A successful DC 18 [[Perception]] check to [[Seek]] or DC 18 [[Medicine]] check to [[Recall Knowledge]] is required to determine that the animal is not, in fact, dead."
  - name: "Revived Retaliation"
    desc: "`pf2:r` **Trigger** The opossum is attacked or disturbed by a creature within reach while Feigning Death <br>  <br> **Effect** The opossum Strikes the triggering creature."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (deadly d10, unarmed), **Damage** 1d10+4 piercing"
  - name: "Melee strike"
    desc: "Claw +10 (`pf2:1`) (agile, unarmed), **Damage** 1d6+4 slashing"
  - name: "Melee strike"
    desc: "Tail +10 (`pf2:1`) (reach 15 ft.), **Damage** 1d4+4 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Larger species of opossum can eat nearly anything human-sized or smaller.

Few creatures have survived as long and in as many environments as the opossum.

```statblock
creature: "Giant Opossum"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
