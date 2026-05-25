---
type: creature
group: ["Amphibious", "Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hermit Crab Swarm"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Amphibious"
trait_02: "Animal"
trait_03: "Swarm"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]], [[Tremorsense]] (imprecise) 15 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +12"
abilityMods: ["+4", "+2", "+3", "-4", "+1", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +13, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "42; **Immunities** precision, swarm mind; **Weaknesses** area damage 5, splash damage 5; **Resistances** piercing 5, slashing 5"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Snips"
    desc: "`pf2:1` Each enemy in the swarm's space takes 2d8 piercing damage (DC 20 [[Reflex]] save). <br>  <br> Creatures that fail this save also take 1d4 bleed."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

When hermit crabs find a shell that is too large, they lie in wait for others to arrive and move into the shell, abandoning a possible replacement. This can form a large chain of queuing crabs waiting to upgrade their shells. Interruptions can aggravate the crabs, resulting in attacks against the unfortunate source of disruption.

Hermit crabs have hard exoskeletons like other crabs, but with much weaker abdomens. They find and "wear" shells as homes and protection, getting around with their front legs and claws. Surprisingly fierce, hermit crabs fight for new shells as they grow bigger, using an assortment of hollow alternatives as substitutes when shells of the right size can't be found.

```statblock
creature: "Hermit Crab Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
