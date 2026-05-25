---
type: creature
group: ["Mindless", "Skeleton"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skeletal Horse"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
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
    desc: "Acrobatics +7, Athletics +9"
abilityMods: ["+5", "+3", "+2", "-5", "+2", "+0"]
abilities_top:
  - name: "Undead Steed"
    desc: "Undead and creatures allied with them can [[Command]] a skeletal steed without needing to attempt a skill check."
armorclass:
  - name: AC
    desc: "16; **Fort** +6, **Ref** +9, **Will** +8"
health:
  - name: HP
    desc: "33; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** cold 5, electricity 5, fire 5, piercing 5, slashing 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hoof +9 (`pf2:1`), **Damage** 1d8+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Gallop"
    desc: "`pf2:2` The horse Strides twice, with its Speed increased by 10 feet."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Skeletal horses are sometimes used as mounts by other undead or monsters.

Animated skeletons are among the most common types of undead.

```statblock
creature: "Skeletal Horse"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
