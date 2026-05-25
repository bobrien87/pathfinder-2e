---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Velociraptor"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +5, Stealth +6"
abilityMods: ["+0", "+3", "+2", "-4", "+1", "+1"]
abilities_top:
  - name: "Pack Attack"
    desc: "The velociraptor deals 1d4 extra damage to any creature that's within reach of at least two of the velociraptor's allies."
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +8 (`pf2:1`) (finesse, unarmed), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Talon +8 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4+3 slashing"
spellcasting: []
abilities_bot:
  - name: "Leaping Charge"
    desc: "`pf2:1` The velociraptor Strides up to 10 feet, ignoring difficult terrain as it leaps over obstacles. It then makes a Strike with its talons, gaining a +1 circumstance bonus to its attack roll."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A smaller cousin of the deinonychus, the velociraptor is a swift, cunning pack hunter. It has no fear of larger creatures, and a group of these dinosaurs won't hesitate to attack prey the size of a horse. They have manes of feathery plumage that extend down their backs and along the sides of their arms, legs, and tail, while their underbellies and flanks are scaly. These feathers allow them to blend into their natural terrain with ease, but when startled, a velociraptor can puff and frill this plumage to expose brighter colors normally covered by the longer feathers. A typical velociraptor is 1-1/2 feet tall, 7 feet long, and weighs 35 pounds.

Remnants from the world's primeval era, these enormous reptilian animals still exist in large numbers in remote wildernesses or underground in magical Darklands caverns. Lizardfolk, orcs, giants, and other humanoids who live near dinosaurs use the animals as mounts, guards, or hunting beasts. Occasionally, rich nobles will collect dinosaurs to display them in menageries, which almost inevitably leads to cast-offs being nursed back to health by druids and other champions of nature. When dinosaurs establish themselves in regions outside their normal habitats, it's often the result of a large collection being released.

```statblock
creature: "Velociraptor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
