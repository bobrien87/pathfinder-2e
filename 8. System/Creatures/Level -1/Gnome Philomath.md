---
type: creature
group: ["Gnome", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gnome Philomath"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Low-Light Vision]]"
languages: "Common, Fey, Gnomish"
skills:
  - name: Skills
    desc: "Athletics +3, Crafting +1, Society +4, Thievery +3, History Lore +5, One Additional Lore +5"
abilityMods: ["+0", "+1", "+0", "+3", "+2", "+1"]
abilities_top:
  - name: "Helpful Hoard"
    desc: "Gnome philomaths can quickly find almost any document in their vast collection. They gain a +8 circumstance bonus to skill checks involving local records and histories."
  - name: "Local Records Specialist"
    desc: "For encounters involving local records and histories, the gnome philomath is a 5th-level challenge."
armorclass:
  - name: AC
    desc: "12; **Fort** +2, **Ref** +5, **Will** +8"
health:
  - name: HP
    desc: "7"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +4 (`pf2:1`) (two hand d8), **Damage** 1d4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 13, attack +0<br>**1st** [[Detect Magic]], [[Light]], [[Prestidigitation]]"
abilities_bot:
  - name: "Mind if I Borrow That?"
    desc: "`pf2:1` The gnome philomath designates a single item within their sight as an item of interest to their studies. They then gain a +2 circumstance bonus to `act disarm options=mind-if-i-borrow-that` or `act steal options=mind-if-i-borrow-that` that item. They can only designate one item at a time in this way. If they use Mind if I Borrow That? to designate a new item of interest, they lose the bonus with the previous item."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The innate gnomish inclination to revel in new experiences leads gnome philomaths to delve as deeply as they can into the multitudes of knowledge contained within a library. These shrewd observers have encyclopedic memories and tend to surround themselves with piles of documents and trinkets pertaining to whatever subject currently holds their attention. As their interests branch from one topic to the next, a gnome philomath files away their discoveries to be referenced again another day.

Because their ancestors came from the First World, gnomes are intrinsically linked to the realm of the fey and crave the mystical and unpredictable. They seek to create daring works of art, voyage to new places, and have experiences they've never had before. Otherwise, they could fall victim to the terrible gnomish illness known as the Bleaching, which not only drains them of their color but of their spirits as well.

```statblock
creature: "Gnome Philomath"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
