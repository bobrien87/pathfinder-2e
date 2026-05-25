---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gamekeeper"
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
    desc: "Athletics +13, Diplomacy +11, Intimidation +13, Nature +15, Survival +15, Hunting Lore +11"
abilityMods: ["+3", "+4", "+2", "+0", "+2", "+1"]
abilities_top:
  - name: "Keeper's Revenge"
    desc: "When the gamekeeper dies, all creatures in a @Template[type:emanation|distance:60] that have damaged the gamekeeper in the last minute must succeed a DC 24 [[Will]] save saving throw or be cursed. All animals the cursed creature encounters have an initial attitude toward them that is one step worse. This curse can be removed only by an effect that specifically targets curses."
  - name: "Move It!"
    desc: "The gamekeeper can [[Hustle]] for 30 minutes longer and is not affected by difficult terrain while in their territory."
  - name: "Leader of the Pack"
    desc: "The gamekeeper depends on a small pack of dogs or other pack animals suitable for the environment to patrol their area. Creatures that are adjacent to a hostile animal are considered [[Off Guard]] to the gamekeeper."
armorclass:
  - name: AC
    desc: "23; **Fort** +17, **Ref** +13, **Will** +12"
health:
  - name: HP
    desc: "95"
abilities_mid:
  - name: "Sic 'Em!"
    desc: "`pf2:r` **Trigger** An animal within 60 feet of the gamekeeper is killed <br>  <br> **Effect** The gamekeeper stokes the ire of the wild. Until the end of the gamekeeper's next turn, they and all animals in a @Template[type:emanation|distance:60] gain a +1 status bonus to attack rolls and a +2 status bonus to damage rolls. <br>  <br> > [!danger] Effect: Sic 'Em!"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+9 bludgeoning"
  - name: "Melee strike"
    desc: "Club +15 (`pf2:1`), **Damage** 1d6+9 bludgeoning"
  - name: "Ranged strike"
    desc: "Arbalest +17 (`pf2:1`) (backstabber, magical, reload 1, range 110 ft.), **Damage** 1d10+6 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Gamekeepers know every beast that walks, slithers, flies, or swims in their territory and where to find them; try to keep up with the pack if you think you can. The land has chosen these people as guardians, giving them mysterious powers while in their territory. They are prepared to keep balance.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Gamekeeper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
