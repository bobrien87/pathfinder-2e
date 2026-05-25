---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dream Spider"
level: "0"
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
    desc: "+6; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +2, Stealth +7"
abilityMods: ["+0", "+3", "+1", "-5", "+0", "-4"]
abilities_top:
  - name: "Web Sense"
    desc: "The dream spider has imprecise [[Tremorsense]] to detect the vibrations of creatures touching its web."
  - name: "Dream Spider Venom"
    desc: "**Saving Throw** DC 16 [[Fortitude]] save <br>  <br> **Maximum Duration** 4 rounds <br>  <br> **Stage 1** [[Stupefied 1]] (1 round) <br>  <br> **Stage 2** 1d6 poison damage plus stupefied 1 (1 round)"
  - name: "Web Trap"
    desc: "A creature hit by the dream spider's web attack is [[Immobilized]] and stuck to the nearest surface until it Escapes (DC 16)."
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "15"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bite +7 (`pf2:1`) (finesse), **Damage** 1d6 piercing plus [[Dream Spider Venom]]"
  - name: "Ranged strike"
    desc: "Web +7 (`pf2:1`) (range 10 ft.), **Damage**  plus [[Dream Spider Venom]] plus [[Web Trap]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A dream spider's webs have an iridescent hue and are infused with the same hallucinogenic compound as the creature's toxin. Originally denizens of tropical jungles, dream spiders have adapted well to temperate environments, particularly thriving among the rooftops of cities where shady alchemists use their venom to produce addictive drugs.

Spiders range dramatically in size, yet many are to some extent venomous.

```statblock
creature: "Dream Spider"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
