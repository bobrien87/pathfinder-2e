---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wolf"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
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
    desc: "Acrobatics +7, Athletics +6, Stealth +7, Survival +7"
abilityMods: ["+2", "+4", "+1", "-4", "+2", "-2"]
abilities_top:
  - name: "Pack Attack"
    desc: "The wolf's Strikes deal 1d4 extra damage to creatures within reach of at least two of the wolf's allies."
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +9, **Will** +5"
health:
  - name: HP
    desc: "24"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (unarmed), **Damage** 1d6+2 piercing plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Wolves live and hunt in packs, which, contrary to popular belief, are not led by the strongest in the group, but typically consist of a mated pair, their pups, and juvenile offspring from previous mating seasons. Offspring generally leave their parents' pack upon reaching maturity, at which point they seek out mates of their own to form their own packs elsewhere.

Humanoids are not traditionally viewed as prey animals by wolves, but extraordinary circumstances can lead these animals to attack people, especially in winter months and other situations where traditional prey (deer and elk mainly) is scarce. Some beings, such as powerful vampires, can call upon wolves to aid them in combat.

Wolves roam forests, hills, and other wild lands, where they hunt in packs to beleaguer and surround their prey before going in for the kill. Like most predatory animals, wolves prefer to attack the weakest or most vulnerable prey they can find.

```statblock
creature: "Wolf"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
