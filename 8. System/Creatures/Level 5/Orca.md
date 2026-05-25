---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Orca"
level: "5"
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
    desc: "+12; [[Echolocation]] (precise) 120 feet, [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +14, Stealth +13"
abilityMods: ["+7", "+2", "+5", "-4", "+3", "+0"]
abilities_top:
  - name: "Aquatic Echolocation 120 feet"
    desc: "An orca can use its hearing as a precise sense at the listed range, but only underwater."
  - name: "Deep Breath"
    desc: "An orca can hold its breath for 2 hours."
armorclass:
  - name: AC
    desc: "21; **Fort** +14, **Ref** +11, **Will** +12"
health:
  - name: HP
    desc: "75"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +13 (`pf2:1`) (unarmed), **Damage** 2d8+9 piercing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "`pf2:1` 30 feet. <br>  <br> An orca can travel no further than 5 feet onto land as part of an Aquatic Ambush. After it does so, it's [[Prone]] until it Crawls to return to the water. <br>  <br> **Requirements** The monster is hiding in water and a creature that hasn't detected it is within the listed number of feet. <br>  <br> **Effect** The monster moves up to its swim Speed + 10 feet toward the triggering creature, traveling on water and on land. Once the creature is in reach, the monster makes a Strike against it. The creature is [[Off-Guard]] against this Strike."
  - name: "Breach"
    desc: "`pf2:2` The orca Swims up to its swim Speed, then [[Leap]] vertically out of the water up to 25 feet in the air, making a Strike against a creature at any point during the jump (this lets it attack a creature within 30 feet of the water's surface). After the Strike, the orca splashes back down into the water."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

While many know orcas as "killer whales," they're actually the largest species of dolphin. These powerful animals hunt together in pods to take down seals, sharks, and even whales. Adult orcas are typically 15–25 feet long and weigh 8,000–12,000 pounds.

Dolphins encompass a wide range of aquatic mammals, all of which are social, intelligent, and widespread throughout the world's oceans.

```statblock
creature: "Orca"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
