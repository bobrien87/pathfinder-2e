---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Street Musician"
level: "2"
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
    desc: "+9"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +6, Crafting +5, Deception +8, Diplomacy +8, Performance +8, Society +6"
abilityMods: ["+2", "+1", "+2", "+0", "+1", "+4"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The street musician deals an additional 1d4 precision damage to [[Off Guard]] creatures. This increases to 1d6 against creatures off-guard due to the street musician's [[Feint]] or distracting drone."
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +8, **Will** +9"
health:
  - name: HP
    desc: "32"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Dagger +8 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 18, attack +10<br>**1st** (3 slots) [[Charm]], [[Daze]], [[Figment]], [[Force Barrage]], [[Light]], [[Summon Instrument]], [[Ventriloquism]]"
abilities_bot:
  - name: "Distracting Drone"
    desc: "`pf2:1` **Requirements** The street musician is playing their instrument <br>  <br> **Effect** The street musician attempts a Type:performance check compared to the Will DC of an observer within 30 feet. On a success, the target is [[Fascinated]] by the street musician and [[Off Guard]] for 1 round."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Many musicians make their living off stage by playing at markets, fairs, or crossroads. While their fame may not be as widespread as theatrical performers, they are nonetheless staples of many communities.

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Street Musician"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
