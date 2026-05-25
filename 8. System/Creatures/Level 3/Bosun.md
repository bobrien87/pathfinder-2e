---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bosun"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +9, Intimidation +9, Sailing Lore +11"
abilityMods: ["+2", "+4", "+1", "+0", "+1", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +11, **Will** +8"
health:
  - name: HP
    desc: "45"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +13 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
  - name: "Melee strike"
    desc: "Naval Pike +11 (`pf2:1`), **Damage** 1d6+5 piercing"
  - name: "Melee strike"
    desc: "Dagger +13 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Naval Pike +13 (`pf2:1`) (thrown 20), **Damage** 1d6+5 piercing"
spellcasting: []
abilities_bot:
  - name: "Bosun's Command"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The bosun orders an ally to attack or to get in position. Until the end of the ally's next turn, they gain the bosun's choice of a +2 status bonus to attack rolls or a +10-foot status bonus to their Speeds. <br>  <br> > [!danger] Effect: Bosun's Command"
  - name: "Pike and Strike"
    desc: "`pf2:2` The bosun makes a melee Strike with their naval pike. <br>  <br> If this Strike hits, the bosun can either move the target 5 feet within the pike's reach or make a fist Strike against the target without increasing their multiple attack penalty until after the fist Strike."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A ship's boatswain, or bosun, leads the deckhands who maintain the ship.

Adventurers may need passage on a swift vessel, or they might face danger from raiders at sea or in coastal settlements.

```statblock
creature: "Bosun"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
