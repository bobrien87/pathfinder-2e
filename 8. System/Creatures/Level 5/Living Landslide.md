---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Living Landslide"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]], [[Tremorsense]] (imprecise) 60 feet"
languages: "Petran"
skills:
  - name: Skills
    desc: "Athletics +14, Stealth +8"
abilityMods: ["+5", "-1", "+4", "-2", "+1", "-1"]
abilities_top:
  - name: "Earthbound"
    desc: "When not touching solid ground, the living landslide is [[Slowed]] 1 and can't use reactions."
  - name: "Earth Glide"
    desc: "The living landslide can Burrow through any earthen matter, including rock. When it does so, the living landslide moves at its full burrow Speed, leaving no tunnels or signs of its passing."
armorclass:
  - name: AC
    desc: "21; **Fort** +15, **Ref** +8, **Will** +10"
health:
  - name: HP
    desc: "90; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Crumble"
    desc: "`pf2:r` **Trigger** The living landslide takes damage from a hostile source while atop rock or earth <br>  <br> **Effect** The living landslide crumbles into the ground, Burrowing down 10 feet. This Burrowing does not trigger reactions. <br>  <br> The living landslide can't Crumble again for 1d4 rounds."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d8+8 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Sliding Earth"
    desc: "`pf2:2` The living landslide Strides up to twice its normal Speed in a straight line, then attempts to [[Trip]] a creature in its reach. If a creature falls [[Prone]] from this Trip, it takes 1d4 bludgeoning damage for every 10 feet the living landslide moved."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Living landslides resemble humanoids made of earth and gravel. They find moving across the many surfaces of the mortal Universe strangely liberating.

Earth elementals make excellent bodyguards for adventuresome spelunkers and are ideal protectors of important subterranean locations such as vaults and treasuries.

```statblock
creature: "Living Landslide"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
