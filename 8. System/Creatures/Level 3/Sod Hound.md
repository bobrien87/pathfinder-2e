---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sod Hound"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +11, Survival +9"
abilityMods: ["+4", "-1", "+3", "-4", "+2", "-1"]
abilities_top:
  - name: "Crystal Sense (Imprecise) 60 feet"
    desc: "A sod hound can sense crystals or gems within 60 feet as if using the [[Scent]] ability"
  - name: "Earth Glide"
    desc: "The sod hound can Burrow through any earthen matter, including rock. When it does so, the sod hound moves at its full burrow Speed, leaving no tunnels or signs of its passing."
armorclass:
  - name: AC
    desc: "19; **Fort** +12, **Ref** +6, **Will** +7"
health:
  - name: HP
    desc: "44; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (unarmed), **Damage** 1d10+6 piercing plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Sod hounds are mossy extraplanar canines formed of packed dirt and pebbles. On their native plane, they are often tasked with guarding less secure sites and finding mineral deposits. Others live in the comparative lap of luxury as pets to jabalis.

Earth elementals make excellent bodyguards for adventuresome spelunkers and are ideal protectors of important subterranean locations such as vaults and treasuries.

```statblock
creature: "Sod Hound"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
