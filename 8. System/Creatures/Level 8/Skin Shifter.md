---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skin Shifter"
level: "8"
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
    desc: "+16"
languages: "Common, Wildsong"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +14, Diplomacy +13, Intimidation +11, Nature +18, Stealth +12, Survival +18"
abilityMods: ["+4", "+2", "+3", "+0", "+4", "+1"]
abilities_top:
  - name: "Animal Empathy"
    desc: "The skin shifter can ask questions of, receive answers from, and use the Diplomacy skill with animals."
armorclass:
  - name: AC
    desc: "25 26 in animal form; **Fort** +15, **Ref** +14, **Will** +16"
health:
  - name: HP
    desc: "140"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spiked Gauntlet +18 (`pf2:1`) (agile, free hand), **Damage** 1d4+10 piercing"
  - name: "Ranged strike"
    desc: "Longbow +17 (`pf2:1`) (deadly d10, magical, reload 0, volley 30, range 100 ft.), **Damage** 2d8+6 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 26, attack +18<br>**1st** [[Gouging Claw]], [[Know the Way]]"
abilities_bot:
  - name: "Gift of the Wild Spirits"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The skin shifter casts their choice of a 4th-rank [[Aerial Form]], [[Animal Form]], [[Dinosaur Form]], or [[Pest Form]] spell. They must transform into an animal of a kind they've seen within the last 24 hours. They can't gain temporary HP again from a spell cast with Gift of the Wild Spirits for 10 minutes. Their Strikes for forms other than *pest form* have reach 10 feet, a +20 attack modifier, and a +13 damage bonus (or a +9 damage bonus for *aerial form*). Most other changes to their statistics are listed above. <br>  <br> While polymorphed, the skin shifter can still use Gift of the Wild Spirits, though they're still prevented from casting other spells as normal."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Skin shifters are defenders of nature, blessed by the spirits of the wild with the ability to shape shift into powerful animal forms. Prowling as beasts or charging across the field, they protect the balance of nature and punish those who would upset it.

A primalist is a wielder of primal energies and magic, sometimes taught by forces of primal power, including powerful elementals or fey of the First World. Primalists protect the natural world, offering strong medicine to those in need while facing suspicion from those who don't understand their ways.

A great many primalists belong to druidic circles, and even those who aren't members tend to be familiar with the most prominent ones in their homeland.

```statblock
creature: "Skin Shifter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
