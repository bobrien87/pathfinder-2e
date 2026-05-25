---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rat Swarm"
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
    desc: "+5; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +4, Stealth +6"
abilityMods: ["-2", "+3", "+1", "-4", "+1", "-3"]
abilities_top:
  - name: "Putrid Plague"
    desc: "The [[Sickened]] and [[Unconscious]] conditions from putrid plague don't improve on their own until the disease is cured. <br>  <br> **Saving Throw** DC 14 [[Fortitude]] save <br>  <br> **Stage 1** carrier with no ill effect (1d4 hours) <br>  <br> **Stage 2** [[Sickened]] 1 (1 day) <br>  <br> **Stage 3** Sickened 1 and [[Slowed]] 1 (1 day) <br>  <br> **Stage 4** [[Unconscious]] (1 day) <br>  <br> **Stage 5** dead"
armorclass:
  - name: AC
    desc: "14; **Fort** +2, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "14; **Immunities** precision, swarm mind; **Weaknesses** area damage 3, splash damage 3; **Resistances** physical 6 except bludgeoning"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Bites"
    desc: "`pf2:1` Each enemy in the swarm's space takes @Damage[1d6[piercing]|options:area-damage] damage and must attempt a DC 17 [[Reflex]] save. A creature that fails its save is exposed to putrid plague."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A swarm of rats can cause total chaos within a household or business. Contracting putrid plague is all the easier when dozens of these agitated or hungry vermin gather to bite victims en masse, making rat-hunting a viable career in many parts of the world as desperate townspeople seek relief from the disease's spread.

Rats are a ubiquitous menace, scurrying through the sewers and on the streets of nearly every settlement in the world. Though a regular rat darting underfoot might startle or even frighten the average passerby, giant rats and rat swarms are far more dangerous.

```statblock
creature: "Rat Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
