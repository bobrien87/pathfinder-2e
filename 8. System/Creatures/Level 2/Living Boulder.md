---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Living Boulder"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]], [[Tremorsense]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +8, Stealth +5"
abilityMods: ["+4", "-1", "+4", "-4", "+2", "-1"]
abilities_top:
  - name: "Earth Glide"
    desc: "A living boulder can [[Burrow]] through earthen matter, including rock. When it does so, it moves at its full burrow Speed, leaving no tunnels or signs of its passing."
armorclass:
  - name: AC
    desc: "17; **Fort** +10, **Ref** +5, **Will** +8"
health:
  - name: HP
    desc: "35; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (unarmed), **Damage** 1d8+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Rolling Charge"
    desc: "`pf2:2` The living boulder Strides twice, and can then make a Strike with its jaws. This jaws Strike gains [[Knockdown]]."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Living boulders roll and glide through the Plane of Earth, gathering gemstones and metal shards until their surfaces resemble a ship's hull covered in barnacles. Barely more intelligent than many animals, living boulders fill much the same role on the Plane of Earth as the great herd animals found on worlds in the Universe.

Certain earth elementals manifest as specific types of material, be they boulders, sand, or crystals.

```statblock
creature: "Living Boulder"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
