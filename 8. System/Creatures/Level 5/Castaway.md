---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Castaway"
level: "5"
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
    desc: "+13"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +13, Crafting +12, Nature +11, Stealth +11, Survival +15"
abilityMods: ["+4", "+2", "+3", "+0", "+4", "-1"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The castaways deals 1d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "21; **Fort** +14, **Ref** +13, **Will** +11"
health:
  - name: HP
    desc: "80"
abilities_mid:
  - name: "Skittish"
    desc: "`pf2:r` **Trigger** The castaway takes damage from a Strike <br>  <br> **Effect** The castaway Steps away from the source of the Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hatchet +15 (`pf2:1`) (agile, sweep), **Damage** 1d6+7 slashing"
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning"
  - name: "Ranged strike"
    desc: "Blowgun +15 (`pf2:1`) (agile, nonlethal, reload 1, range 20 ft.), **Damage** 1 piercing plus 2d6 poison plus 1d6 poison"
spellcasting: []
abilities_bot:
  - name: "Cockamamie Rant"
    desc: "`pf2:2` The castaway launches into a nonsensical verbal stream of consciousness. Creatures in a @Template[type:emanation|distance:30] must succeed at a DC 19 [[Will]] save or be [[Confused]] for 1 round. Once a creature has succeeded at a save against the castaway's Cockamamie Rant, they are immune to its effects for 24 hours."
  - name: "Snare Master"
    desc: "`pf2:3` **Frequency** five times per day <br>  <br> **Effect** By scrounging local materials, the castaway constructs a simple but effective deadfall without expending resources. Treat this as a snare with a DC 19 [[Perception]] check to spot, and a DC 23 [[Thievery]] check to disable. It occupies a single 5-foot square and lasts 24 hours before falling apart. The first creature that enters the space takes 6d6 bludgeoning damage (DC 22 [[Reflex]] save)."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Be it the result of shipwreck, forcible marooning, or personal choice, surviving alone on an island long enough tends to weed out the weak of body and mind. Lack of social interaction tends to breed belligerence towards outsiders, but hostilities are not a certainty.

Adventurers may need passage on a swift vessel, or they might face danger from raiders at sea or in coastal settlements.

```statblock
creature: "Castaway"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
