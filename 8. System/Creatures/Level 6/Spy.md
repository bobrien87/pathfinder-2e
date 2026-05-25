---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Spy"
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
    desc: "+14"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +14, Deception +16, Diplomacy +14, Intimidation +14, Society +14, Stealth +16, Thievery +14, Local Court Lore +16"
abilityMods: ["+0", "+4", "+0", "+2", "+2", "+4"]
abilities_top:
  - name: "Noble's Ally"
    desc: "The spy has positioned themself to seem a trusted ally, gaining a +2 circumstance bonus to `act gather-information options=nobles-ally` or to `act make-an-impression options=nobles-ally` among the nobles of that court."
  - name: "Sneak Attack"
    desc: "The spy deals an extra 2d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +16, **Will** +14"
health:
  - name: HP
    desc: "90"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +17 (`pf2:1`) (deadly d8, disarm, finesse, magical), **Damage** 1d6+7 piercing"
  - name: "Melee strike"
    desc: "Dagger +16 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+7 piercing"
  - name: "Melee strike"
    desc: "Dagger +16 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+7 piercing"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Hidden Blade"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The spy draws a weapon and then Strikes with it. The target of the strike is [[Off Guard]] against the attack."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Any number of nobles could be spies—a beloved confidante of the queen or even the court jester. Spies use their skills to subtly manipulate courtiers, turn enemies against one another, and collect valuable information.

The denizens of a noble court are the most powerful people in a civilization, primed with wealth, station, and authority above the common people.

```statblock
creature: "Spy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
