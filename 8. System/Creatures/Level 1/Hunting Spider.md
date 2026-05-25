---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hunting Spider"
level: "1"
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
    desc: "+7; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +5, Stealth +7"
abilityMods: ["+2", "+4", "+1", "-5", "+2", "-4"]
abilities_top:
  - name: "Web Sense"
    desc: "The hunting spider has imprecise tremorsense to detect the vibrations of creatures touching its web. <br>  <br> Tremorsense allows a monster to feel the vibrations through a solid surface caused by movement. It is an imprecise sense with a limited range (listed in the ability). Tremorsense functions only if the monster is on the same surface as the subject, and only if the subject is moving along (or burrowing through) the surface."
  - name: "Hunting Spider Venom"
    desc: "**Saving Throw** DC 16 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage and [[Off Guard]] (1 round) <br>  <br> **Stage 2** 1d6 poison damage, [[Clumsy]] 1, and off-guard (1 round) <br>  <br> **Stage 3** 1d6 poison damage, [[Clumsy]] 2, and off-guard (1 round)"
  - name: "Web Trap"
    desc: "A creature hit by the hunting spider's web Strike is [[Immobilized]] and stuck to the nearest surface until it Escapes."
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +9, **Will** +5"
health:
  - name: HP
    desc: "16"
abilities_mid:
  - name: "Spring Upon Prey"
    desc: "`pf2:r` **Requirements** Initiative has not yet been rolled. <br>  <br> **Trigger** A creature touches the hunting spider's web while the spider is on it. <br>  <br> **Effect** The hunting spider automatically notices the creature and Strides, Climbs, or Descends on a Web before it rolls initiative."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +9 (`pf2:1`) (finesse), **Damage** 1d6+2 piercing plus [[Hunting Spider Venom]]"
  - name: "Ranged strike"
    desc: "Web +7 (`pf2:1`) (range 30 ft.), **Damage**  plus [[Web Trap]]"
spellcasting: []
abilities_bot:
  - name: "Descend on a Web"
    desc: "`pf2:1` The hunting spider moves straight down up to 40 feet, suspended by a web line. It can hang from the web or drop off. The distance it Descends on a Web doesn't count for falling damage. <br>  <br> A creature that successfully Strikes the web (AC 20, Hardness 3, 5 HP) severs it, causing the spider to fall."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Hunting spiders are the most common type of giant spider, though not the largest.

Few everyday vermin inspire as much dread as the infamous spider.

```statblock
creature: "Hunting Spider"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
