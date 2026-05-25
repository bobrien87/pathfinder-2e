---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bottlenose Dolphin"
level: "0"
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
    desc: "+7; [[Echolocation]] (precise) 120 feet, [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +6"
abilityMods: ["+2", "+3", "+2", "-4", "+3", "+0"]
abilities_top:
  - name: "Aquatic Echolocation 120 feet"
    desc: "A bottlenose dolphin can use its hearing as a precise sense at the listed range, but only underwater."
  - name: "Deep Breath"
    desc: "A bottlenose dolphin can hold its breath for 2 hours."
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +7, **Will** +5"
health:
  - name: HP
    desc: "16"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Snout +6 (`pf2:1`), **Damage** 1d6+2 bludgeoning"
  - name: "Melee strike"
    desc: "Jaws +6 (`pf2:1`) (unarmed), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Ramming Speed"
    desc: "`pf2:2` The bottlenose dolphin [[Swims]] twice and then makes a snout Strike. As long as it moved at least 20 feet, it gains a +1 circumstance bonus to its attack roll. <br>  <br> A Large or smaller creature hit by this attack must succeed at a DC 16 [[Fortitude]] save or be [[Slowed]] 1 for 1 round."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The bottlenose dolphin is the most common and widespread species of dolphin. They are social predators who hunt shallow seas and rivers in large family groups called pods. Sailors are fond of bottlenose dolphins and frequently tell of how they've saved drowning mariners or protected crew from sharks with blows from their powerful snouts.

Dolphins encompass a wide range of aquatic mammals, all of which are social, intelligent, and widespread throughout the world's oceans.

```statblock
creature: "Bottlenose Dolphin"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
