---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Spear Frog"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +0"
abilityMods: ["-2", "+3", "+1", "-4", "+2", "+0"]
abilities_top:
  - name: "Spear Frog Venom"
    desc: "**Saving Throw** DC 15 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage (1 round) <br>  <br> **Stage 2** 1d6 poison damage and [[Enfeebled]] 1 (1 round)"
  - name: "Sticky Feet"
    desc: "Spear frogs are not [[Off Guard]] when Balancing on a narrow surface, and they gain a +4 circumstance bonus to Reflex saves to avoid falling."
armorclass:
  - name: AC
    desc: "14; **Fort** +5, **Ref** +7, **Will** +6"
health:
  - name: HP
    desc: "12"
abilities_mid:
  - name: "Toxic Skin"
    desc: "Anytime a creature touches the spear frog or an adjacent creature Strikes the spear frog with a melee attack, that creature is exposed to spear frog venom."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d6 piercing plus [[Spear Frog Venom]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The spear frog is named for its toxin, which is traditionally used to envenom thrown projectiles like spears and daggers.

Frogs that are poisonous or grow to monstrous size can be a menace to adventurers.

```statblock
creature: "Spear Frog"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
