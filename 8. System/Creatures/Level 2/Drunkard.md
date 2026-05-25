---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Drunkard"
level: "2"
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
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +7, Intimidation +8, Alcohol Lore +3"
abilityMods: ["+3", "+2", "+4", "-1", "+0", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +10, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Melee strike"
    desc: "Pewter Mug +8 (`pf2:1`) (thrown 10), **Damage** 1d4+3 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Drunken Flailing"
    desc: "`pf2:1` **Requirements** The drunkard is raging <br>  <br> **Effect** The drunkard attempts two fist Strikes, each against a different creature."
  - name: "Drunken Rage"
    desc: "`pf2:1` **Requirements** The drunkard is drunk, and isn't [[Fatigued]] or raging <br>  <br> **Effect** The drunkard flies into a drunken rage. They gain 6 temporary Hit Points that last until the drunken rage ends. While raging, they deal 4 additional damage with melee attacks and take a –1 penalty to AC. The drunkard can't use concentrate actions except [[Seek]]. The rage lasts for 1 minute, until the drunkard falls [[Unconscious]], or until the drunkard sobers up. The drunkard can't voluntarily stop raging. Once the rage ends, the drunkard can't gain temporary HP from this action for 1 minute."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Every tavern has one-that person who drinks a little too much and starts a fight. While many drunkards are relatively harmless, a few have a hair trigger, and when they're set off come, no one-even the drunkard themself-can tell you what started the row.

Countless adventures begin in a tavern or a pub. Maybe it's because such places attract the risk-prone, or maybe it's because everyone needs a little liquid courage before they decide to take on a group of rampaging ogres.

```statblock
creature: "Drunkard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
