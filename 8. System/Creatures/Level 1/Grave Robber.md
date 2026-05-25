---
type: creature
group: ["Holy", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Grave Robber"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Holy"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5"
languages: "Common"
skills:
  - name: Skills
    desc: "Crafting +6, Deception +2, Intimidation +2, Society +6, Stealth +5, Underworld Lore +6"
abilityMods: ["+1", "+2", "+2", "+3", "+2", "-1"]
abilities_top:
  - name: "Alchemical Embalming"
    desc: "The grave robber carries alchemical vials of specially prepared embalming fluid meant to hinder pursuit by anyone who interrupts their grave-robbing. A creature hit by a grave robber's embalming flask takes a –10-foot penalty to all its Speeds for 1 round. On a critical hit from an embalming flask, the target is also [[Clumsy]] 1 for 1 minute. <br>  <br> > [!danger] Effect: Alchemical Embalming"
armorclass:
  - name: AC
    desc: "15; **Fort** +7, **Ref** +7, **Will** +5"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shovel +6 (`pf2:1`), **Damage** 1d6+1 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
  - name: "Ranged strike"
    desc: "Embalming Flask +7 (`pf2:1`) (alchemical, splash, range 20 ft.), **Damage** 1 acid plus 1d4 acid plus [[Alchemical Embalming]]"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Many cultures have a tradition of burying their dead with a selection of the deceased's most precious possessions. Such valuables can be easy pickings for those with no respect for—or fear of—the dead.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Grave Robber"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
