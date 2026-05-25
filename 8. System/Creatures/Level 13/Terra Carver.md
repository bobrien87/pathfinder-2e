---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Terra Carver"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+23; [[Darkvision]], [[Tremorsense]] (imprecise) 100 feet"
languages: "Petran (Can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +27, Intimidation +22, Mining Lore +25"
abilityMods: ["+8", "-1", "+6", "+4", "+0", "+2"]
abilities_top:
  - name: "Earthbound"
    desc: "When not touching solid ground, the terra carver is [[Slowed]] 1 and can't use reactions."
  - name: "Hew Stone"
    desc: "Melee attacks the terra carver makes with their stone tool ignore physical resistance and Hardness."
  - name: "Stone Tunnels"
    desc: "A terra carver can burrow through solid stone. When they do, they leave a tunnel."
armorclass:
  - name: AC
    desc: "33; **Fort** +26, **Ref** +19, **Will** +23"
health:
  - name: HP
    desc: "265; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Crashing Fall"
    desc: "Due to their size, a terra carver falls a lot harder than most creatures. When a terra carver is knocked [[Prone]] or takes falling damage, they take an additional 15 bludgeoning damage in addition to any other effect."
  - name: "Territorial Retaliation"
    desc: "`pf2:r` **Trigger** A creature within 15 feet uses a move action or leaves a square during a move action (move actions using only a fly Speed don't trigger this reaction) <br>  <br> **Effect** The terra carver attempts an Athletics check to [[Trip]] the triggering creature. Regardless of the result, the space of the triggering creature and all spaces on the ground adjacent to that creature become difficult terrain for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Stone Tool +26 (`pf2:1`) (reach 15 ft., versatile b, versatile s), **Damage** 3d10+16 piercing plus [[Hew Stone]]"
  - name: "Ranged strike"
    desc: "Rock +24 (`pf2:1`) (propulsive, range 60 ft.), **Damage** 3d8+12 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Carve Projectile"
    desc: "`pf2:2` The terra carver carves a deadly projectile from nearby materials and makes a rock ranged Strike that gains the deadly d10 trait. On a successful hit, the target also falls [[Prone]]."
  - name: "Wedge"
    desc: "`pf2:2` The terra carver attempts a stone tool Strike while wedging the blow further with another tool. If it hits, the target takes an additional 3d10 damage of the same type as the Strike and is [[Enfeebled]] 2 for 1 hour or until the creature is fully healed. This counts as two attacks for the terra carver's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Even other earth elementals and creatures of stone fear the formidable terra carver. Their four arms end with sharpened stone tools that can cleave through the toughest rocks—and anything that wanders into their territory. Despite having powerful forms, their bulky upper bodies appear comically large compared to their stout legs. They lumber slowly through their territory and spend most of their time cutting stone deep in the bedrock to create elaborate networks of tunnels.

They prefer isolation, and when two terra carvers meet, it typically ends with one hewing the other. Instead of taking their enemy's territory, a terra carver collapses the tunnels, continuing elsewhere with their own designs.

Voiceless MinersTerra carvers are talented miners, and their tunnels are some of the longest lasting on any plane. However, the reason for these tunnels is unknown. Scholars have theorized that their tunnels function as a form of written language for the otherwise voiceless elementals. Unfortunately, attempts to map abandoned tunnels often end where another terra carver collapsed an encroaching tunnel, and mapping active tunnels often results in the cartographer never making it back.

```statblock
creature: "Terra Carver"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
