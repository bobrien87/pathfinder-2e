---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Naari Pyrochemist"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Naari"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3"
languages: "Common, Pyric"
skills:
  - name: Skills
    desc: "Acrobatics +6, Crafting +6, Intimidation +4, Nature +3, Survival +3, Thievery +6"
abilityMods: ["+0", "+3", "+2", "+3", "+0", "+1"]
abilities_top:
  - name: "Infused Items"
    desc: "A naari pyrochemist carries the following infused items, which last for 24 hours or until the next time the pyrochemist makes their daily preparations: <br>  <br> Lesser Alchemist's Fire (5) <br>  <br> Lesser Elixir of Life (2) <br>  <br> Lesser Smoke Ball"
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +6, **Will** +3"
health:
  - name: HP
    desc: "18; **Resistances** fire 1"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +8 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4 piercing"
  - name: "Melee strike"
    desc: "Dagger +8 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4 piercing"
  - name: "Ranged strike"
    desc: "Lesser Alchemist's Fire +8 (`pf2:1`) (range 30 ft.), **Damage** 1d8 fire plus 1 fire plus 1 fire"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16, attack +8<br>**1st** [[Ignition]]"
abilities_bot:
  - name: "Quick Bomber"
    desc: "`pf2:1` The naari pyrochemist draws an alchemist's fire with an Interact action and throws it as a ranged Strike."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Naaris' blood blazes with elemental fire. On the Plane of Fire, most naaris are second-class citizens who serve under the iron heel of the ifrits and their Dominion of Flame, but those born outside the ifrit hierarchy or who choose to flee it live lives of passion in search of fame, glory, and power.

Naaris are fond of fire, but this doesn't mean they all embrace fire's destructive nature. Those who seek more productive roles in a society might cherish fire's protective warmth and the role it plays in creation or cooking. Others find inspiration in the way flames flit and dance, and they pride themselves in their skills as acrobats or dancers. The church of Sarenrae particularly welcomes naari fire dancers, both in appreciation of their skill and to help ensure these naaris have a safe place apart from their more violent kin.

But by and large, naaris are drawn to professions and callings that allow them to indulge in the glories of fire. Naari pyrochemists apply this calling to alchemical teachings, seeing purity in every single bomb thrown or conflagration lit.

```statblock
creature: "Naari Pyrochemist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
