---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Chronicler"
level: "3"
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
    desc: "+12"
languages: "Common"
skills:
  - name: Skills
    desc: "Nature +10, Society +9, Survival +7, One Additional Lore +10, Scribing Lore +13"
abilityMods: ["+2", "+2", "+1", "+3", "+4", "+0"]
abilities_top:
  - name: "Scroll Mastery"
    desc: "The chronicler can activate any scroll of a 2nd-rank spell or lower, regardless of its magical tradition."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +9, **Will** +10"
health:
  - name: HP
    desc: "45"
abilities_mid:
  - name: "Live to Tell the Tale"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** The chronicler would gain the [[Dying]] condition <br>  <br> **Effect** The chronicler instead falls [[Unconscious]] for 1d4 hours or until they regain 1 Hit Point."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +8 (`pf2:1`) (two hand d8), **Damage** 1d4+5 bludgeoning"
  - name: "Melee strike"
    desc: "Dagger +8 (`pf2:1`) (agile, versatile s), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Dagger +8 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Fist +8 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +7 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+3 piercing"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 20, attack +12<br>**2nd** (2 slots) [[Entangling Flora]], [[Floating Flame]]<br>**1st** (3 slots) [[Fleet Step]], [[Tailwind]], [[Vanishing Tracks]]<br>**Cantrips** [[Know the Way]], [[Light]], [[Frostbite]], [[Sigil]], [[Tangle Vine]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Exploration means very little if no account of the details exist. Members of adventuring bands cherish chroniclers who record tales of their deeds.

The world is a wide, open place fraught with peril and adventure. Explorers use their knowledge of nature and survival skills to see every corner of the land.

```statblock
creature: "Chronicler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
