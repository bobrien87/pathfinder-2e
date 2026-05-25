---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Rat"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Animal"
trait_02: ""
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
    desc: "Acrobatics +5, Athletics +2, Stealth +5"
abilityMods: ["+1", "+3", "+2", "-4", "+1", "-3"]
abilities_top:
  - name: "Putrid Plague"
    desc: "The [[Sickened]] and [[Unconscious]] conditions from putrid plague don't improve on their own until the disease is cured. <br>  <br> **Saving Throw** DC 14 [[Fortitude]] save <br>  <br> **Stage 1** carrier with no ill effect (1d4 hours) <br>  <br> **Stage 2** [[Sickened]] 1 (1 day) <br>  <br> **Stage 3** Sickened 1 and [[Slowed]] 1 (1 day) <br>  <br> **Stage 4** [[Unconscious]] (1 day) <br>  <br> **Stage 5** dead"
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +7, **Will** +3"
health:
  - name: HP
    desc: "8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d6+1 piercing plus [[Filth Fever]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Giant rats are enormous versions of the common vermin. They are typically found in abundant numbers, but since they cannot fit in the nooks where mundane rats typically hide, they are much easier to locate and exterminate. They mostly live in sewers where they can scavenge from the streets above, but some families of giant rats live in more remote locations, such as dank caves, forests or hills. Rats are incredibly adept survivors and can be found nearly anywhere in the world, though they tend to favor temperate or warm climates as opposed to cold regions.

Although its bite alone is not lethal except to the very young or very old, the giant rat carries the putrid plague common to rodents around the world—a pestilence more than capable of ravaging rural communities.

Rats are a ubiquitous menace, scurrying through the sewers and on the streets of nearly every settlement in the world. Though a regular rat darting underfoot might startle or even frighten the average passerby, giant rats and rat swarms are far more dangerous.

```statblock
creature: "Giant Rat"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
