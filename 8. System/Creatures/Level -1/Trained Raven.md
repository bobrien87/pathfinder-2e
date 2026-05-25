---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Trained Raven"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +5, Deception +5, Thievery +5"
abilityMods: ["-3", "+3", "+0", "-4", "+3", "+0"]
abilities_top:
  - name: "Cunning"
    desc: "A raven can use simple items as tools, such as poking a stick at an opening to tease out a piece of food. They're also quite adept at stealing objects. A raven can't use Thievery to [[Palm an Object]], [[Disable a Device]], or [[Pick a Lock]], but it can use Thievery to [[Steal]] light objects that it can carry in its beak or talons or to accomplish other relatively simple tasks."
  - name: "Sneak Attack"
    desc: "A raven's Strikes deal an additional 1d4 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "15; **Fort** +2, **Ref** +7, **Will** +5"
health:
  - name: HP
    desc: "7"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +7 (`pf2:1`) (finesse), **Damage** 1d4-1 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These omnivorous birds are cunning and opportunistic scavengers. Capable of solving simple puzzles to retrieve desired items, ravens gather at the periphery of civilization, raiding it as needed when they're not hunting in the wilds. Ravens are known for trickery and often trained to further this instinct. Trained ravens will wait for an opening and peck their foes in vulnerable spots.

Few birds are as cunning and social as the raven.

```statblock
creature: "Trained Raven"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
