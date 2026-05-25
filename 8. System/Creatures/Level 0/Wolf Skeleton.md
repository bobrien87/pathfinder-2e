---
type: creature
group: ["Mindless", "Skeleton"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wolf Skeleton"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +5, Stealth +6"
abilityMods: ["+2", "+4", "+1", "-5", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +3, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "12; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** cold 5, electricity 5, fire 5, piercing 5, slashing 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +8 (`pf2:1`) (unarmed), **Damage** 1d4+2 piercing plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Surge of Speed"
    desc: "`pf2:2` The wolf skeleton Strides three times, but it's [[Off Guard]] until the start of its next turn."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Without the burden of flesh, skeletal wolves charge across the battlefield with terrifying speed.

Among the ranks of the dead, none are so numerous, nor so varied, as the skeleton. While most are almost entirely made from bone, some maintain a few scraps of flesh to aid them in movement, such as wing membranes.

```statblock
creature: "Wolf Skeleton"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
