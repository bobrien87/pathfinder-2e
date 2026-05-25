---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pachycephalosaurus"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Dinosaur"
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
    desc: "Athletics +11, Intimidation +7"
abilityMods: ["+4", "+3", "+4", "-4", "+3", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +12, **Ref** +11, **Will** +7"
health:
  - name: HP
    desc: "65"
abilities_mid:
  - name: "Sudden Shove"
    desc: "`pf2:r` **Trigger** The pachycephalosaurus damages a Medium or smaller foe with its skull Strike <br>  <br> **Effect** The pachycephalosaurus digs in and flings its head up, shoving its foe away. It attempts an [[Athletics]] check against the target's Fortitude DC. <br> - **Critical Success** The pachycephalosaurus pushes the opponent up to 10 feet away from itself and knocks the target [[Prone]]. <br> - **Success** The pachycephalosaurus pushes the opponent back 5 feet. <br> - **Failure** The pachycephalosaurus fails to push the opponent. <br> - **Critical Failure** As failure, but the failed attempt leaves the pachycephalosaurus [[Off Guard]] for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Skull +11 (`pf2:1`) (forceful, reach 10 ft.), **Damage** 1d10+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Clobbering Charge"
    desc: "`pf2:2` The pachycephalosaurus Strides up to its Speed. If it ends its movement within melee reach of a target, it can make a skull Strike against that target. If the pachycephalosaurus critically hits with this Strike, the creature hit is [[Stunned]] 1."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Pachycephalosauruses are normally peaceful, herbivorous dinosaurs, but they grow much more violent during mating season, when they fight one another to win over mates and warn away interlopers. They also defend themselves vehemently if potential predators stray too close to their herd. The pachycephalosaurus's skull has a distinctive dome-shaped crown surrounded by numerous blunt, bony horns. This feature, combined with the dinosaur's powerful, compact neck, allows it to make battering-ramlike charges capable of inflicting great damage.

Some humanoid groups have successfully trained pachycephalosauruses as mounts, but the creatures aren't particularly well suited to the task.

Pachycephalosauruses grow to a length of 15 feet and weigh 1,400 pounds.

Remnants from the world's primeval era, these enormous reptilian animals still exist in large numbers in remote wildernesses or underground in magical Darklands caverns. Lizardfolk, orcs, giants, and other humanoids who live near dinosaurs use the animals as mounts, guards, or hunting beasts. Occasionally, rich nobles will collect dinosaurs to display them in menageries, which almost inevitably leads to cast-offs being nursed back to health by druids and other champions of nature. When dinosaurs establish themselves in regions outside their normal habitats, it's often the result of a large collection being released.

```statblock
creature: "Pachycephalosaurus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
