---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Spider Swarm"
level: "0"
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
    desc: "+4; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +2, Stealth +5"
abilityMods: ["-2", "+3", "+0", "-5", "+0", "-4"]
abilities_top:
  - name: "Web Sense"
    desc: "The spider swarm has imprecise tremorsense to detect the vibrations of creatures touching its web. <br>  <br> Tremorsense allows a monster to feel the vibrations through a solid surface caused by movement. It is an imprecise sense with a limited range (listed in the ability). Tremorsense functions only if the monster is on the same surface as the subject, and only if the subject is moving along (or burrowing through) the surface."
  - name: "Spider Swarm Venom"
    desc: "**Saving Throw** DC 14 [[Fortitude]] save <br>  <br> **Maximum Duration** 4 rounds <br>  <br> **Stage 1** 1 poison and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 1d4 poison and enfeebled 1 (1 round)"
armorclass:
  - name: AC
    desc: "15; **Fort** +4, **Ref** +7, **Will** +2"
health:
  - name: HP
    desc: "12; **Immunities** precision, swarm mind; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 2, piercing 5, slashing 5"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Bites"
    desc: "`pf2:1` Each enemy in the spider swarm's space takes @Damage[1d4[piercing]|options:area-damage] damage with a DC 14 [[Reflex]] save. <br>  <br> A creature that fails its save is exposed to spider swarm venom."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

An abundance of food, the sudden hatching of a clutch of eggs, or magical influence can cause smaller spiders to gather in terrifying, deadly masses.

Few everyday vermin inspire as much dread as the infamous spider.

```statblock
creature: "Spider Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
