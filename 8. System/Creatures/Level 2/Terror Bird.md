---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Terror Bird"
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
    desc: "+6; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +8"
abilityMods: ["+4", "+3", "+3", "-4", "+0", "+0"]
abilities_top:
  - name: "Tearing Clutch"
    desc: "The terror bird's powerful beak can tear through flesh. On a successful beak Strike, the target takes 1 persistent bleed damage. This bleed damage increases to 1d4 on a critical hit."
armorclass:
  - name: AC
    desc: "17; **Fort** +11, **Ref** +9, **Will** +4"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +9 (`pf2:1`) (reach 10 ft.), **Damage** 1d8+4 piercing plus [[Tearing Clutch]]"
  - name: "Melee strike"
    desc: "Talon +9 (`pf2:1`) (agile), **Damage** 1d6+4 piercing plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Sprint"
    desc: "`pf2:2` **Frequency** once per minute <br>  <br> **Effect** The terror bird Strides three times in a straight line"
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Common terror birds are notable hunters. On their own, they use their great speed to catch prey unaware. In a flock, they can swarm and take down larger beasts like aurochs with their overwhelming numbers.

Terror birds aren't one species, but rather a family of deadly, flightless avian predators. All terror birds are capable of bursts of great speed and have powerful beaks that can tear apart the flesh of their prey. Most stalk large, open prairies and steppes, competing directly with other sizable predators such as big cats and wolves.

```statblock
creature: "Terror Bird"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
