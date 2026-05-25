---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Crocodile"
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
    desc: "+7; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +8, Stealth +7"
abilityMods: ["+4", "+1", "+3", "-5", "+1", "-4"]
abilities_top:
  - name: "Deep Breath"
    desc: "The crocodile can hold its breath for about 2 hours."
armorclass:
  - name: AC
    desc: "17; **Fort** +9, **Ref** +7, **Will** +5"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (unarmed), **Damage** 1d10+4 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tail +10 (`pf2:1`) (agile), **Damage** 1d6+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "`pf2:1` 35 feet <br>  <br> **Requirements** The monster is hiding in water and a creature that hasn't detected it is within the listed number of feet. <br>  <br> **Effect** The monster moves up to its swim Speed + 10 feet toward the triggering creature, traveling on water and on land. Once the creature is in reach, the monster makes a Strike against it. The creature is [[Off-Guard]] against this Strike."
  - name: "Death Roll"
    desc: "`pf2:1` **Requirements** The crocodile must have a creature [[Grabbed]] <br>  <br> **Effect** The crocodile tucks its legs and rolls rapidly, twisting its victim. It makes a jaws Strike with a +2 circumstance bonus to the attack roll against the grabbed creature. If it hits, it also knocks the creature [[Prone]]. If it fails, it releases the creature."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Crocodiles can be found basking on riverbanks, lurking in swamps, or floating in lakes. They are usually indistinguishable from logs when viewed from afar—at least until they attack. Alligators have similar statistics, but because they often live in more temperate climates, they endure cold temperatures better. Unlike alligators, crocodiles can tolerate salt water. Both are formidable predators that are likely to devour careless adventurers who fail to watch where they step.

Powerful and primeval in appearance, crocodiles are dangerous natural predators that dwell in marshes, riverbeds, swamps, and other wetlands.

```statblock
creature: "Crocodile"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
