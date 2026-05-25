---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gravedigger"
level: "1"
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
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +7, Religion +5, Stealth +4, Graveyard Lore +4"
abilityMods: ["+4", "+1", "+3", "+0", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +8, **Ref** +4, **Will** +7"
health:
  - name: HP
    desc: "20; **Resistances** void 2"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shovel +9 (`pf2:1`), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Light in the Dark"
    desc: "`pf2:2` **Requirements** The gravedigger is holding a bull's-eye lantern in one hand and their religious symbol in the other, and the lantern contains oil <br>  <br> **Effect** The gravedigger recites a brief chant to ignite their lantern with vital energy. Each undead creature in a @Template[type:line|distance:15] takes @Damage[3d6[vitality]|options:area-damage] damage with a DC 14 [[Fortitude]] save. This action uses all remaining oil in the bull's-eye lantern."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

An often-overlooked group of laborers, gravediggers have a reputation for being as quiet and grim as their workplace. They're usually strong and tough from their long hours of backbreaking labor, and they tend to have a unique perspective on life and death.

Society is built upon the backs of laborers.

```statblock
creature: "Gravedigger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
