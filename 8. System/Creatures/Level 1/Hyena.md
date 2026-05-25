---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hyena"
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
    desc: "+6; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +7, Stealth +6"
abilityMods: ["+3", "+3", "+2", "-4", "+1", "-2"]
abilities_top:
  - name: "Pack Attack"
    desc: "The hyena deals an extra 1d4 damage to any creature that's within reach of at least two of the hyena's allies."
armorclass:
  - name: AC
    desc: "16; **Fort** +7, **Ref** +8, **Will** +4"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +8 (`pf2:1`) (unarmed), **Damage** 1d8+3 piercing plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Drag"
    desc: "`pf2:1` The hyena makes a jaws Strike against a [[Prone]] enemy. If it hits, in addition to dealing damage, the hyena Strides up to 10 feet, dragging the enemy along."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Hyenas are cunning, powerfully built carnivores that bear a heavy resemblance to dogs and other canines, though they are not themselves canines. Though all hyenas are often maligned as cowardly carrion eaters, their tactics depend on their specific breed: spotted hyenas are active pack hunters that kill most of their prey themselves, while striped and brown hyenas are more likely to be loners and scavengers. Their jaws are exceptionally powerful, allowing hyenas to seize a victim and pull it to the rest of the pack.

Hyenas are pack-hunting scavengers known for their unnerving, laughterlike cries. The most well-known hyenas are the socially gregarious spotted hyenas, who travel in packs and work together to hunt or drive off larger creatures. Hyenas are typically nocturnal creatures who scavenge meat, insects, and fruit, though they aren't above supplementing their carrion diets with fresh prey.

```statblock
creature: "Hyena"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
