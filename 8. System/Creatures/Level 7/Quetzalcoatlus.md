---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Quetzalcoatlus"
level: "7"
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
    desc: "+15; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +17"
abilityMods: ["+6", "+4", "+3", "-4", "+2", "-1"]
abilities_top:
  - name: "Carry"
    desc: "A quetzalcoatlus can Fly at half Speed while it has a single creature [[Grabbed]] or [[Restrained]]. Both its talons are occupied while it does this."
armorclass:
  - name: AC
    desc: "25; **Fort** +16, **Ref** +17, **Will** +12"
health:
  - name: HP
    desc: "110"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +17 (`pf2:1`) (deadly d10, reach 10 ft., unarmed), **Damage** 2d10+10 piercing plus 1d8 bleed"
  - name: "Melee strike"
    desc: "Talon +17 (`pf2:1`) (unarmed), **Damage** 2d8+10 piercing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Swoop"
    desc: "`pf2:2` The quetzacoaltus Flies up to its Speed and makes one beak or talon Strike at any point during that movement."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Quetzalcoatlus are the largest flying members of the pterosaur family and are often mistaken for dragons due to their immense size and 40-foot wingspans. Using the joints of their massive wings as forelimbs, they are also quite capable of moving on land, snatching smaller prey from the ground or out of streams.

Quetzalcoatlus are carnivorous, feeding on a variety of reptiles, mammals, large fish, amphibians, and other vertebrates. They are not inherently aggressive creatures and are happy to scavenge for food, but when presented with live prey they readily attack almost any creature smaller than themselves.

Pterosaurs are primitive flying creatures. While many are smaller than a human or even small enough to perch on a shoulder, the two presented below are quite a bit larger. Each of these creatures could pose a serious threat to a person.

These flying reptiles can be found in a wide selection of regions, but they tend to soar above warm or temperate climates. They sometimes spread outside their natural range as pets and hunting companions for lizardfolk or giants. Cloud giants living in isolated valleys also train the largest pterosaurs to carry their messages to the outside world.

```statblock
creature: "Quetzalcoatlus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
