---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ankhrav"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]], [[Tremorsense]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +11, Stealth +8"
abilityMods: ["+4", "+1", "+3", "-4", "+0", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +12, **Ref** +8, **Will** +7"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +13 (`pf2:1`) (acid), **Damage** 1d8+4 piercing plus 1d6 acid"
  - name: "Ranged strike"
    desc: "Acid Spit +10 (`pf2:1`) (acid), **Damage** 3d6 acid"
spellcasting: []
abilities_bot:
  - name: "Armor-Rending Bite"
    desc: "`pf2:2` The ankhrav makes a mandibles Strike; if the Strike hits, the target's armor takes the damage and the acid damage bypasses the armor's Hardness."
  - name: "Spray Acid"
    desc: "`pf2:2` **Frequency** once per hour <br>  <br> **Effect** The ankhrav spews acid in a @Template[cone|distance:30], dealing @Damage[3d6[acid],1d6[persistent,acid]|options:area-damage]{3d6 acid damage and 1d6 persistent acid damage} (DC 20 [[Reflex]] save)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These horse-sized, burrowing monsters generally avoid heavily settled areas like cities, but ankhravs' predilection for livestock and humanoid flesh ensures that the creatures do not remain in the deep wilderness for long. Desperate farmers whose fields become infested by ankhravs often have little recourse but to seek the aid of adventurers.

Ankhravs are immense, burrowing, and insectile predators, considered by inhabitants of the rural areas of the world to be an all-too-common plague.

```statblock
creature: "Ankhrav"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
