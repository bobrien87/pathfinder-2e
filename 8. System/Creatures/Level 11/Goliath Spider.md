---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Goliath Spider"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +18, Athletics +23, Stealth +22"
abilityMods: ["+8", "+5", "+7", "-5", "+3", "-4"]
abilities_top:
  - name: "Web Sense"
    desc: "The goliath spider has imprecise tremorsense to detect the vibrations of creatures touching its web. <br>  <br> Tremorsense allows a monster to feel the vibrations through a solid surface caused by movement. It is an imprecise sense with a limited range (listed in the ability). Tremorsense functions only if the monster is on the same surface as the subject, and only if the subject is moving along (or burrowing through) the surface."
  - name: "Goliath Spider Venom"
    desc: "**Saving Throw** DC 30 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 3d6 poison damage and [[Slowed]] 1 (1 round) <br>  <br> **Stage 2** 3d8 poison damage and [[Slowed]] 2 (1 round) <br>  <br> **Stage 3** 3d10 poison damage and [[Paralyzed]] for 2d4 hours"
  - name: "Web Tether"
    desc: "A creature hit by the spider's web Strike is [[Restrained]] and tethered to the spider, preventing it from moving farther away from the spider. <br>  <br> The spider can have one creature tethered at a time. The DC to [[Escape]] or [[Force Open]] the web is 30. The tether can be severed with a Strike (AC 20, Hardness 5, HP 20), but this doesn't free the restrained creature."
armorclass:
  - name: AC
    desc: "30; **Fort** +25, **Ref** +21, **Will** +17"
health:
  - name: HP
    desc: "220"
abilities_mid:
  - name: "Spring Upon Prey"
    desc: "`pf2:r` **Requirements** Initiative has not yet been rolled. <br>  <br> **Trigger** A creature touches the goliath spider's web while the spider is on it. <br>  <br> **Effect** The goliath spider automatically notices the creature and Strides, Climbs, or Descends on a Web before it rolls initiative."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +24 (`pf2:1`) (reach 10 ft.), **Damage** 2d12+12 piercing plus [[Goliath Spider Venom]]"
  - name: "Ranged strike"
    desc: "Web +22 (`pf2:1`) (range 60 ft.), **Damage**  plus [[Web Tether]]"
spellcasting: []
abilities_bot:
  - name: "Descend on a Web"
    desc: "`pf2:1` The goliath spider moves straight down up to 120 feet, suspended by a web line. It can hang from the web or drop off. The distance it Descends on a Web doesn't count for falling damage. <br>  <br> A creature that successfully Strikes the web (AC 20, Hardness 5, 20 HP) severs it, causing the spider to fall."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Goliath spiders dwell in the deepest jungles, where they build webs as big as temples and feast on prey as large as hippopotami.

Few everyday vermin inspire as much dread as the infamous spider.

```statblock
creature: "Goliath Spider"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
