---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dockhand"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +3, Athletics +7, Intimidation +4, Labor Lore +4"
abilityMods: ["+3", "+1", "+3", "+0", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "14; **Fort** +7, **Ref** +5, **Will** +3"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Melee strike"
    desc: "Bottle +5 (`pf2:1`) (agile, thrown 15), **Damage** 1d4+3 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Heft Crate"
    desc: "`pf2:2` **Requirements** The dockhand is adjacent to a crate <br>  <br> **Effect** The dockhand picks up a crate and heaves it up to 15 feet. Upon landing, the crate breaks open in a @Template[type:burst|distance:5]. Each creature in the area takes @Damage[2d6[bludgeoning]|options:area-damage] damage with a DC 13 [[Reflex]] save, and the area is difficult terrain until cleared."
  - name: "Swig"
    desc: "`pf2:2` The dockhand Interacts to either draw a bottle of [[Alcohol]] or pick up a nearby unattended bottle of alcohol, then drinks the whole thing. For 1 minute, the dockhand gains a +2 item bonus to melee damage rolls and saving throws against fear but is [[Off Guard]]."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Working to load and unload cargo from ships, dockhands are considered unruly, but many stay focused and work hard until the job is done.

Society is built upon the backs of laborers.

```statblock
creature: "Dockhand"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
