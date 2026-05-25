---
type: creature
group: ["Cold", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Blizzardborn"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Cold"
trait_02: "Elemental"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Thalassic"
skills:
  - name: Skills
    desc: "Athletics +15, Stealth +14"
abilityMods: ["+5", "+2", "+4", "+0", "+4", "+0"]
abilities_top:
  - name: "Snow Vision"
    desc: "The blizzardborn ignores the [[Concealed]] condition from falling snow."
  - name: "Ice Burrow"
    desc: "The blizzardborn can [[Burrow]] through ice or snow with a Speed of 20 feet. It moves at its full burrow Speed, leaving no tunnels or signs of its passing."
armorclass:
  - name: AC
    desc: "24; **Fort** +16, **Ref** +12, **Will** +14"
health:
  - name: HP
    desc: "105; **Immunities** bleed, cold, paralyzed, poison, sleep; **Weaknesses** fire 5"
abilities_mid:
  - name: "Shattering Ice"
    desc: "`pf2:r` **Trigger** An enemy hits the blizzardborn with an attack that deals physical damage <br>  <br> **Effect** A portion of the blizzardborn's body shatters into an explosion of razor-sharp ice crystals and blinding snow that deals @Damage[2d6[piercing]|options:area-damage] damage to opponents in a @Template[type:emanation|distance:5] (DC 24 [[Reflex]] save). Anyone who fails is also [[Blinded]] for 1 round (3 rounds on a critical failure)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ice Claw +17 (`pf2:1`) (versatile b), **Damage** 2d6+8 slashing plus 1d6 cold"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Freezing and thawing in a near-constant loop, blizzardborn resemble humanoid forms composed of a mixture of partially melted snow and sleet. These elementals move with crunching strides, their bodies constantly sloshing and sloughing off shards of ice. Because of their ability to refreeze, blizzardborn can travel into warmer environments safely, though they tend to look more like slush in these areas.

Water elementals that become infused with cold or mist have increased mobility in regions outside of bodies of water.

```statblock
creature: "Blizzardborn"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
