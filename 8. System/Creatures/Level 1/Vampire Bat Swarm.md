---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vampire Bat Swarm"
level: "1"
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
    desc: "+10; [[Echolocation]] (precise) 20 feet, [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +4, Stealth +7"
abilityMods: ["+1", "+4", "+1", "-4", "+3", "-3"]
abilities_top:
  - name: "Echolocation (Precise) 20 feet"
    desc: "A bat swarm can use its hearing as a precise sense at the listed range."
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "11; **Immunities** precision, swarm mind; **Weaknesses** area damage 3, splash damage 3; **Resistances** bludgeoning 6, piercing 6, slashing 3"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Blood Feast"
    desc: "`pf2:1` Each enemy in the bat swarm's space takes 1d4 piercing damage (DC 16 [[Reflex]] save). Creatures that fail this save also take 1 bleed damage."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Although the typical vampire bat has a wingspan of 7 inches and doesn't pose a significant threat to larger prey alone (and indeed, these blood-drinkers can feed without their sleeping victims ever noticing), some unusually aggressive species of these bats hunt in deadly swarms. A churning cloud of vampire bats is much more dangerous than the sum of its individual parts and is capable of inflicting an overwhelming number of bleeding wounds in a frighteningly short span of time.

A wide range of bats dwell throughout the world. Most of these nocturnal animals are harmless insectivores, but deadly breeds of vampire bats and oversized bats the size of horses pose much more significant threats to adventurers.

```statblock
creature: "Vampire Bat Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
