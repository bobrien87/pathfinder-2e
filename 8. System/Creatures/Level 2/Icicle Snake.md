---
type: creature
group: ["Cold", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Icicle Snake"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Cold"
trait_02: "Elemental"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +7, Stealth +7"
abilityMods: ["+1", "+3", "+2", "-4", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +9, **Will** +5"
health:
  - name: HP
    desc: "35; **Immunities** bleed, cold, paralyzed, poison, sleep; **Weaknesses** fire 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (finesse), **Damage** 1d6+1 piercing plus 1d6 cold"
spellcasting: []
abilities_bot:
  - name: "Icicle"
    desc: "`pf2:1` Until the next time it acts, the icicle snake appears to be an unassuming icicle. It has an automatic result of 27 on Deception checks and DCs to pass as an icicle."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Translucent and capable of hanging suspended and near motionless, icicle snakes sense the heat of living creatures as a threat and attempt to use their camouflage and chilling bite against foes.

Water elementals that become infused with cold or mist have increased mobility in regions outside of bodies of water.

```statblock
creature: "Icicle Snake"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
