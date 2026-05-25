---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Raven Swarm"
level: "3"
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
    desc: "+9; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +10, Thievery +10"
abilityMods: ["+0", "+3", "+0", "-4", "+4", "+0"]
abilities_top:
  - name: "Enraged Cunning"
    desc: "There are few things as dangerously persistent in the natural world as an angry unkindness of ravens. A raven swarm can hound its prey through most barriers. Simple latches, unsecured chimney flues, loosely shuttered windows, and similar obstacles rarely keep an unkindness away. A raven swarm attempts a Thievery check to bypass many of these simple obstructions, typically against DC 20."
armorclass:
  - name: AC
    desc: "19; **Fort** +7, **Ref** +12, **Will** +9"
health:
  - name: HP
    desc: "30; **Immunities** swarm mind, precision; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 2, piercing 5, slashing 5"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Beaks"
    desc: "`pf2:1` The ravens' angry pecking deals 2d8 piercing damage to each enemy in the swarm's space (DC 20 [[Reflex]] save). A creature that critically fails its save is [[Blinded]] for 1d4 rounds as the ravens focus their attacks on the target's vulnerable face."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A flock of ravens is known as an unkindness. Certainly, the name lives up to its meaning when a swarm of ravens decides to work together. In most cases, a raven swarm like the one presented here won't attack larger foes, but when manipulated by supernatural forces or simple desperation born from hunger, an unkindness of ravens can be a surprisingly dangerous threat.

Few birds are as cunning and social as the raven.

```statblock
creature: "Raven Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
