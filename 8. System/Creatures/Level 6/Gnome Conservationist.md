---
type: creature
group: ["Gnome", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gnome Conservationist"
level: "6"
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
    desc: "+17; [[Low-Light Vision]]"
languages: "Common, Gnomish"
skills:
  - name: Skills
    desc: "Athletics +13, Crafting +11, Nature +15, Survival +15"
abilityMods: ["+2", "+1", "+1", "+2", "+4", "+2"]
abilities_top:
  - name: "Animal Elocutionist"
    desc: "The conservationist can ask questions of, receive answers from, and use the Diplomacy skill with animals."
armorclass:
  - name: AC
    desc: "23; **Fort** +17, **Ref** +11, **Will** +14"
health:
  - name: HP
    desc: "100"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trowel +14 (`pf2:1`) (agile, finesse, trip), **Damage** 1d4+8 slashing"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +16 (`pf2:1`) (magical, propulsive, reload 1, range 60 ft.), **Damage** 1d6+7 bludgeoning"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 24, attack +17<br>**3rd** (3 slots) [[Grease]], [[Mad Monkeys]], [[Safe Passage]]<br>**2nd** (4 slots) [[Animal Messenger]], [[Darkvision]], [[Entangling Flora]], [[Oaken Resilience]]<br>**1st** (4 slots) [[Charm]], [[Gentle Landing]], [[Runic Body]], [[Spider Sting]]<br>**Cantrips** [[Detect Magic]], [[Gouging Claw]], [[Know the Way]], [[Light]], [[Tangle Vine]]"
abilities_bot:
  - name: "Wild Leadership"
    desc: "`pf2:1` With a primal incantation, the gnome conservationist inspires a willing animal. The animal becomes [[Quickened]] for 1 round. It can use this additional action only to Climb, Burrow, Fly, Stride, or Strike."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The natural world boasts unsurpassed beauty and countless variety, and the gnome conservationist is devoted to experiencing and protecting as many examples of this grandeur as they possibly can. These gnomes are stalwart allies to animals and plants, and they find it exceptionally easy to build an outstanding rapport with almost all creatures they encounter on their travels.

Because their ancestors came from the First World, gnomes are intrinsically linked to the realm of the fey and crave the mystical and unpredictable. They seek to create daring works of art, voyage to new places, and have experiences they've never had before. Otherwise, they could fall victim to the terrible gnomish illness known as the Bleaching, which not only drains them of their color but of their spirits as well.

```statblock
creature: "Gnome Conservationist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
