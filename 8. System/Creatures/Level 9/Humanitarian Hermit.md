---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Humanitarian Hermit"
level: "9"
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
    desc: "+17"
languages: "Common, Fey, Wildsong"
skills:
  - name: Skills
    desc: "Athletics +19, Diplomacy +14, Medicine +21, Nature +19, Society +14, Survival +17"
abilityMods: ["+4", "+1", "+3", "+1", "+4", "+1"]
abilities_top:
  - name: "Plant Empathy"
    desc: "The humanitarian hermit can ask questions of, receive answers from, and use the Diplomacy skill with plants and fungus."
  - name: "Primal Staff"
    desc: "A staff wielded by the humanitarian hermit gains the parry, reach, and trip traits, and Strikes with it deal an additional 2d8 vitality damage."
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the humanitarian hermit's spellcasting action, the hermit attempts a DC 15 flat check. On a success, the action isn't disrupted."
armorclass:
  - name: AC
    desc: "26; **Fort** +18, **Ref** +16, **Will** +19"
health:
  - name: HP
    desc: "150"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +20 (`pf2:1`) (magical, two hand d8), **Damage** 2d4+10 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +19 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 27, attack +19<br>**5th** (5 slots) [[Heal]], [[Heal]], [[Heal]], [[Heal]], [[Vital Beacon]]<br>**4th** (3 slots) [[Cleanse Affliction]], [[Cleanse Affliction]], [[Mountain Resilience]]<br>**3rd** (3 slots) [[Earthbind]], [[Haste]], [[Safe Passage]]<br>**2nd** (3 slots) [[Create Food]], [[Environmental Endurance]], [[Peaceful Rest]]<br>**1st** (3 slots) [[Cleanse Cuisine]], [[Create Water]], [[Vanishing Tracks]]<br>**Cantrips** [[Electric Arc]], [[Light]], [[Know the Way]], [[Stabilize]], [[Vitality Lash]]"
abilities_bot:
  - name: "Cleansing Earth"
    desc: "`pf2:3` **Frequency** once per hour <br>  <br> **Effect** The humanitarian blesses the land and their allies. In a @Template[type:emanation|distance:30], plants grow and become difficult terrain. Additionally, all allies in the emanation gain 20 temporary Hit Points and can ignore the difficult terrain. These effects last for 1 minute. <br>  <br> > [!danger] Effect: Cleansing Earth"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Some druids look after those forgotten by society and thrive at the borders of civilization.

The world is a dangerous place. Thankfully, there are those who devote their lives to easing the pain and suffering of others.

```statblock
creature: "Humanitarian Hermit"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
