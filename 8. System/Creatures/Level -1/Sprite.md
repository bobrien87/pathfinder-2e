---
type: creature
group: ["Fey", "Sprite"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sprite"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fey"
trait_02: "Sprite"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Low-Light Vision]]"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +6, Stealth +6"
abilityMods: ["-3", "+4", "+0", "-2", "+0", "+2"]
abilities_top:
  - name: "Luminous Fire"
    desc: "A sprite naturally sheds light like a torch. The sprite can extinguish, rekindle, or change the color of this light by using an action with the concentrate trait. While this light is extinguished, the sprite's Strikes don't deal fire damage, and they can't use their luminous spark Strike."
armorclass:
  - name: AC
    desc: "15; **Fort** +2, **Ref** +8, **Will** +4"
health:
  - name: HP
    desc: "7; **Weaknesses** cold iron 3"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +8 (`pf2:1`) (deadly d8, disarm, finesse, fire, magical), **Damage** 1d6-3 piercing"
  - name: "Ranged strike"
    desc: "Luminous Spark +8 (`pf2:1`) (fire, light), **Damage** 1d4 fire"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16, attack +8<br>**1st** [[Daze]], [[Detect Magic]], [[Dizzying Colors]], [[Light]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Common sprites, sometimes called firefly sprites, are primeval guardians that latch onto a person, place, or object and defend it for their own inscrutable reasons. Their dispositions vary from kind to spiteful, but all sprites have a capricious streak. Being only about 9 inches tall, they are wary of animals that might hunt them, particularly house cats, and prefer flight to a fight. On the other hand, sprites are incredibly curious about all forms of magic and heedlessly gather around ley line nexuses or other places of power.

Elusive, flighty, and ebullient, sprites are what many villagers first imagine when they hear the terms "fey" or "fairy." While their dispositions vary, all sprites share a connection to magic and a diminutive size. This family of fey shares its name with its slightest and most populous member, the common sprite.

```statblock
creature: "Sprite"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
