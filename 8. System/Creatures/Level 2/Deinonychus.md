---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Deinonychus"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: "Dinosaur"
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
    desc: "Acrobatics +7, Athletics +9, Stealth +7"
abilityMods: ["+3", "+3", "+4", "-4", "+1", "+2"]
abilities_top:
  - name: "Predator's Advantage"
    desc: "Bleeding creatures are [[Off Guard]] to the deinonychus."
armorclass:
  - name: AC
    desc: "17; **Fort** +10, **Ref** +9, **Will** +5"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (unarmed), **Damage** 2d6+3 piercing"
  - name: "Melee strike"
    desc: "Talon +9 (`pf2:1`) (agile, unarmed), **Damage** 1d6+3 slashing plus 1d4 bleed"
spellcasting: []
abilities_bot:
  - name: "Darting Strike"
    desc: "`pf2:1` The deinonychus Strides up to 10 feet and then makes a Strike, or makes a Strike and then Strides up to 10 feet."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Deinonychuses are wily hunters that attack in groups of up to a dozen individuals, ripping apart prey with sharp talons and powerful jaws. They are lean, muscular, and have two powerful legs and a long tail that helps them maintain balance. Although deinonychuses don't use their dexterous clawed forelimbs to attack, the dinosaurs can use them to pull aside small barriers. Although some of these dinosaurs have scaly skin, most have thatches of vibrantly colored feathers as well. A deinonychus is about 6 feet tall and weighs about 150 pounds.

Remnants from the world's primeval era, these enormous reptilian animals still exist in large numbers in remote wildernesses or underground in magical Darklands caverns. Lizardfolk, orcs, giants, and other humanoids who live near dinosaurs use the animals as mounts, guards, or hunting beasts. Occasionally, rich nobles will collect dinosaurs to display them in menageries, which almost inevitably leads to cast-offs being nursed back to health by druids and other champions of nature. When dinosaurs establish themselves in regions outside their normal habitats, it's often the result of a large collection being released.

```statblock
creature: "Deinonychus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
