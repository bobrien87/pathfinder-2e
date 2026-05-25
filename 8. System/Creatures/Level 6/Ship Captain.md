---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ship Captain"
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
    desc: "+12"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +12, Diplomacy +11, Intimidation +13, Survival +10, Sailing Lore +17"
abilityMods: ["+4", "+2", "+0", "+1", "+2", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +12, **Will** +14"
health:
  - name: HP
    desc: "90"
abilities_mid:
  - name: "Bravery"
    desc: "When the Ship Captain rolls a success on a Will save against a fear effect, they get a critical success instead. In addition, any time they gain the [[Frightened]] condition, reduce its value by 1."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +17 (`pf2:1`) (deadly d8, disarm, magical), **Damage** 1d6+10 piercing"
  - name: "Melee strike"
    desc: "Main-Gauche +16 (`pf2:1`) (agile, disarm, parry, versatile s), **Damage** 1d4+10 piercing"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +14 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Dual Disarm"
    desc: "`pf2:2` The captain makes two Strikes, one with their rapier and one with their main-gauche (in either order). If both Strikes hit, the ship captain can attempt to `act disarm` the target. <br>  <br> Their multiple attack penalty increases only after all the attacks are made."
  - name: "No Quarter!"
    desc: "`pf2:1` The captain orders their shipmates to fight without mercy. All allied creatures of equal or lower level within 20 feet of the ship captain gain a +1 status bonus to attack rolls and damage rolls until the end of the ship captain's next turn. <br>  <br> > [!danger] Effect: No Quarter!"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The captain is the ultimate authority on a vessel, responsible for the livelihood and well-being of everyone on the ship.

Adventurers may need passage on a swift vessel, or they might face danger from raiders at sea or in coastal settlements.

```statblock
creature: "Ship Captain"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
