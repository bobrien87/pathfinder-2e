---
type: creature
group: ["Mindless", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zombie Shambler"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Zombie"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+0; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +7"
abilityMods: ["+3", "-2", "+2", "-5", "+0", "-2"]
abilities_top:
  - name: "Slow"
    desc: "A zombie is permanently [[Slowed]] 1 and can't use reactions."
armorclass:
  - name: AC
    desc: "12; **Fort** +6, **Ref** +0, **Will** +2"
health:
  - name: HP
    desc: "20; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Weaknesses** vitality 5, slashing 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (unarmed), **Damage** 1d6+3 bludgeoning plus [[Grab]]"
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`) (unarmed), **Damage** 1d8+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A zombie shambler is a slow-moving horror dangerous in larger groups.

A zombie's only desire is to consume the living. Unthinking and ever-shambling harbingers of death, zombies stop only when they're destroyed.

```statblock
creature: "Zombie Shambler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
