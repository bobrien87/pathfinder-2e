---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Grizzly Bear"
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
    desc: "+10; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +11, Survival +8"
abilityMods: ["+4", "+1", "+5", "-4", "+1", "-2"]
abilities_top:
  - name: "Mauler"
    desc: "The grizzly bear gains a +2 circumstance bonus to damage rolls against creatures it has [[Grabbed]]."
armorclass:
  - name: AC
    desc: "17; **Fort** +12, **Ref** +6, **Will** +8"
health:
  - name: HP
    desc: "59"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (unarmed), **Damage** 2d8+4 piercing"
  - name: "Melee strike"
    desc: "Claw +11 (`pf2:1`) (agile, unarmed), **Damage** 1d10+4 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Rush"
    desc: "`pf2:2` The grizzly bear Strides and makes a Strike at the end of that movement. During the Stride, the grizzly bear gains a +10-foot circumstance bonus to its Speed."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

This large and powerful omnivore inhabits forested hills. While it typically sustains itself on nuts, berries, fish, and small mammals, it's fiercely territorial and will chase off or kill any creature it views as competition. Grizzly bears are especially temperamental when their young are nearby. In combat, a grizzly bear often attempts to grab and maul its foe with surprising ferocity. It continues its assault until its foe seems like it is no longer a threat, though if the bear is hungry, it will not hesitate to feed.

Bears are ferocious predators typically found in cold or temperate woodlands and hills. Many species of bear exist in addition to the two presented below, such as the smaller black bear or the arctic-dwelling polar bear.

```statblock
creature: "Grizzly Bear"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
