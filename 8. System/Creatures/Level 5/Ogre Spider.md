---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ogre Spider"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +13"
abilityMods: ["+6", "+4", "+4", "-5", "+2", "-4"]
abilities_top:
  - name: "Web Sense"
    desc: "The dream spider has imprecise [[Tremorsense]] to detect the vibrations of creatures touching its web."
  - name: "Eerie Flexibility"
    desc: "An ogre spider can fit through tight spaces as if it were a Large creature. While Squeezing, it can move at its full Speed."
  - name: "Ogre Spider Venom"
    desc: "**Saving Throw** DC 22 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage (1 round) <br>  <br> **Stage 2** 1d6 poison damage, [[Clumsy]] 1, and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 3** 2d6 poison damage, clumsy 1, and enfeebled 1 (1 round) <br>  <br> **Stage 4** 2d6 poison damage, [[Clumsy]] 2, and [[Enfeebled]] 2 (1 round)"
  - name: "Web Trap"
    desc: "A creature hit by the ogre spider's web attack is [[Immobilized]] and stuck to the nearest surface until it Escapes (DC 22)."
armorclass:
  - name: AC
    desc: "22; **Fort** +15, **Ref** +13, **Will** +9"
health:
  - name: HP
    desc: "70"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bite +15 (`pf2:1`), **Damage** 2d8+8 piercing plus [[Ogre Spider Venom]]"
  - name: "Ranged strike"
    desc: "Web +13 (`pf2:1`) (range 30 ft.), **Damage**  plus [[Web Trap]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These terrifying creatures grow as large as elephants. The placement of their eyes above their wide mandibles evokes the grimacing visage of an ogre's leer. Ogres find ogre spider faces simultaneously amusing and adorable, but in most cases, ogres' attempts to keep these spiders as pets result in dead ogres and well-fed spiders.

Spiders range dramatically in size, yet many are to some extent venomous.

```statblock
creature: "Ogre Spider"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
