---
type: creature
group: ["Aberration", "Goblin"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Goblin Snake"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Aberration"
trait_02: "Goblin"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common, Goblin (snake empathy)"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +6, Intimidation +5, Stealth +7, Survival +4"
abilityMods: ["+3", "+4", "+2", "-2", "+0", "+1"]
abilities_top:
  - name: "Snake Empathy"
    desc: "A goblin snake can communicate with snakes."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +10, **Will** +4"
health:
  - name: HP
    desc: "15"
abilities_mid:
  - name: "Coiled Strike"
    desc: "`pf2:r` As [[Reactive Strike]], but the goblin snake can use this reaction only if it's Coiled."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +9 (`pf2:1`) (finesse, unarmed), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Coil"
    desc: "`pf2:1` The goblin snake uses an action to coil itself, increasing its reach with its fangs from 5 to 10 feet. After the goblin snake Strikes with its fangs, it becomes uncoiled."
  - name: "Goblin Breath"
    desc: "`pf2:2` The goblin snake belches a cloud of nauseating vapor in a @Template[type:cone|distance:15]. Non-goblin creatures within the cloud must succeed at a DC 16 [[Fortitude]] save or become [[Sickened]] 1. On a critical failure, a creature is also [[Slowed]] 1 for as long as it is sickened. Creatures that successfully save are immune for 24 hours. The goblin snake can't use Goblin Breath again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Goblin snakes sometimes train snakes as pets or companions.

A goblin snake is a foul-smelling serpentine creature covered in greasy black scales and sporting a fanged, lipless head resembling that of a goblin.

```statblock
creature: "Goblin Snake"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
