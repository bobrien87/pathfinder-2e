---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Veteran Noble"
level: "6"
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
    desc: "+15"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +13, Deception +12, Diplomacy +12, Intimidation +14, Heraldry Lore +14, Warfare Lore +14"
abilityMods: ["+3", "+2", "+0", "+2", "+3", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24; **Fort** +12, **Ref** +14, **Will** +16"
health:
  - name: HP
    desc: "85"
abilities_mid:
  - name: "Battle Scarred"
    desc: "The first time each day the veteran noble would be reduced to 0 HP, they remain at 1 HP and are [[Enfeebled]] 2 for the rest of the day."
  - name: "Noble Pride"
    desc: "`pf2:r` **Trigger** An opponent attempts to [[Demoralize]] the veteran noble or one of the noble's allies within 30 feet <br>  <br> **Effect** The veteran noble attempts to Demoralize the triggering opponent before the opponent rolls. On a critical success, the triggering action is disrupted as well."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +16 (`pf2:1`) (magical, versatile p), **Damage** 1d8+11 slashing"
  - name: "Melee strike"
    desc: "Dagger +15 (`pf2:1`) (agile, versatile s), **Damage** 1d4+11 piercing"
  - name: "Melee strike"
    desc: "Dagger +15 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+11 piercing"
  - name: "Melee strike"
    desc: "Gauntlet +15 (`pf2:1`) (agile, free hand), **Damage** 1d4+11 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Tactical Command"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The veteran noble directs an ally. The ally can immediately use their reaction to Strike or to Stride without triggering reactions. The ally gains a +2 status bonus to their Strike if the veteran noble has dealt with that creature or an organization that creature belongs to before, as the veteran offers hard-earned tactical advice. <br>  <br> > [!danger] Effect: Tactical Command"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Veteran nobles have survived battles in the past, both social and physical. These movers and shakers are often the patrons or mentors of bold adventurers.

The denizens of a noble court are the most powerful people in a civilization, primed with wealth, station, and authority above the common people.

```statblock
creature: "Veteran Noble"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
