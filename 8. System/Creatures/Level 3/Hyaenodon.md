---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hyaenodon"
level: "3"
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
    desc: "+9; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +12, Stealth +8"
abilityMods: ["+5", "+3", "+3", "-4", "+2", "-2"]
abilities_top:
  - name: "Bonecrunching Bite"
    desc: "A creature that is critically hit by a hyaenodon must succeed at a DC 20 [[Fortitude]] save or become [[Wounded]] 1 as the creature's bones or cartilage are crushed by the beast's jaws."
  - name: "Pack Attack"
    desc: "The hyaenodon deals an extra 1d6 damage to any creature within reach of at least two of the hyaenodon's allies."
armorclass:
  - name: AC
    desc: "18; **Fort** +10, **Ref** +8, **Will** +7"
health:
  - name: HP
    desc: "45"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +12 (`pf2:1`) (unarmed), **Damage** 1d10+5 piercing plus [[Bonecrunching Bite]] plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Drag"
    desc: "`pf2:1` The hyaenodon makes a jaws Strike against a [[Prone]] enemy. If it hits, in addition to dealing damage, the hyaenodon Strides up to 10 feet, dragging the enemy along."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Hyaenodons are ferocious primeval creatures that resemble hyenas. Looming, shaggy-furred animals nearly the size of a horse, hyaenodons are truly formidable predators to be reckoned with, due both to their size and to their flesh-shearing jaws. Hyaenodons prey on small horses, camels, and even young rhinoceroses. Kholo clans find these creatures particularly useful as mounts and guardians.

Hyenas are pack-hunting scavengers known for their unnerving, laughterlike cries. The most well-known hyenas are the socially gregarious spotted hyenas, who travel in packs and work together to hunt or drive off larger creatures. Hyenas are typically nocturnal creatures who scavenge meat, insects, and fruit, though they aren't above supplementing their carrion diets with fresh prey.

```statblock
creature: "Hyaenodon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
