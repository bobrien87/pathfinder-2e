---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rat Snake Swarm"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +10, Stealth +8"
abilityMods: ["+0", "+4", "+2", "-4", "+2", "-3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +8, **Ref** +10, **Will** +6"
health:
  - name: HP
    desc: "25; **Immunities** precision, swarm mind; **Weaknesses** area damage 3, splash damage 3; **Resistances** bludgeoning 3, piercing 5, slashing 5"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
  - name: "Mass Wriggle"
    desc: "`pf2:r` **Trigger** The rat snake swarm takes damage from a melee Strike <br>  <br> **Effect** Snakes slither up and around the creature's weapon and limbs. The target must succeed at a DC 15 [[Will]] save or become [[Frightened]] 1."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Strikes"
    desc: "`pf2:1` Each enemy in the swarm's space takes 1d8 piercing damage (DC 17 [[Reflex]] save)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A solitary snake might be no cause for alarm, but a hissing mass of frenzied snakes can make even seasoned adventurers shudder. Rat snakes can reach lengths of up to 10 feet, and they gather en masse to hibernate as well as to breed. Though nonvenomous, these territorial snakes will strike anything that threatens them.

Snakes of some variety thrive in every non-arctic ecosystem, each with their own particular hunting patterns and defense mechanisms.

```statblock
creature: "Rat Snake Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
