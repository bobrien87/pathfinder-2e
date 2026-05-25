---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Compsognathus"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Stealth +6"
abilityMods: ["+0", "+3", "+2", "-4", "+2", "-2"]
abilities_top:
  - name: "Compsognathus Venom"
    desc: "**Saving Throw** DC 16 [[Fortitude]] save <br>  <br> **Maximum Duration** 4 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 1d8 poison damage and Enfeebled 1 (1 round)"
armorclass:
  - name: AC
    desc: "15; **Fort** +4, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`) (agile, finesse, reach 0 ft., unarmed), **Damage** 1d6 piercing plus [[Compsognathus Venom]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The compsognathus is a small bipedal dinosaur that moves in swift, darting motions. Its bite injects a venom that causes numbness and weakness, a trait the animal uses to bring down larger prey, although it prefers to scavenge or snatch insects and other smaller creatures for its meals.

The compsognathus is curious to a fault, often getting itself into trouble. It measures 3 feet long from head to tail and weighs 15 pounds—small enough to serve as a house pet or familiar for a spellcaster. In cases where magical links aren't involved, however, those keeping the creature would be well-advised to treat it with the same caution one might extend to a pet viper or other poisonous reptile, as they're partly tame at best.

Remnants from the world's primeval era, these enormous reptilian animals still exist in large numbers in remote wildernesses or underground in magical Darklands caverns. Lizardfolk, orcs, giants, and other humanoids who live near dinosaurs use the animals as mounts, guards, or hunting beasts. Occasionally, rich nobles will collect dinosaurs to display them in menageries, which almost inevitably leads to cast-offs being nursed back to health by druids and other champions of nature. When dinosaurs establish themselves in regions outside their normal habitats, it's often the result of a large collection being released.

```statblock
creature: "Compsognathus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
