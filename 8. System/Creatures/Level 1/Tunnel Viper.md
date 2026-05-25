---
type: creature
group: ["Humanoid", "Ratfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tunnel Viper"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Ratfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Common, Sakvroth, Ysoki"
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +6, Nature +5, Stealth +8, Survival +5, Thievery +6"
abilityMods: ["+3", "+3", "+0", "+1", "+2", "+0"]
abilities_top:
  - name: "Swarming"
    desc: "A tunnel viper can end their movement in the same square as an ally that also has this ability. Only two such creatures can share the same space."
  - name: "Tunnel Fighter"
    desc: "The tunnel viper deals an additional 1d6 precision damage to creatures that are [[Squeezing]] or in difficult terrain due to narrow spaces."
  - name: "Tunnel Travel"
    desc: "Narrow spaces aren't difficult terrain for the tunnel viper, and the viper can [[Squeeze]] at 5 feet per round (or 10 feet on a critical success)."
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +9, **Will** +5"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ranseur +8 (`pf2:1`) (disarm, reach 10 ft.), **Damage** 1d10+3 piercing"
  - name: "Melee strike"
    desc: "Jaws +8 (`pf2:1`) (agile, unarmed), **Damage** 1d4+3 piercing"
  - name: "Ranged strike"
    desc: "Arbalest +8 (`pf2:1`) (backstabber, reload 1, range 110 ft.), **Damage** 1d10 piercing"
spellcasting: []
abilities_bot:
  - name: "Running Reload"
    desc: "`pf2:1` The tunnel viper Strides, Steps, or [[Sneaks]], then Interacts to reload."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

There is no better way for a ysoki to distinguish themself than to defend the warren, with many proving themselves by venturing out and challenging monsters they come across. Those who return triumphant from such tests find themselves among the ranks of ysoki warriors, able to wear their accomplishments as a badge of pride. They often venture out again once established and experienced to attain more notoriety as warriors.

Ysoki (or, as outsiders call them, ratfolk) in their warrens have a society that is both stern and democratic, caring and ever vigilant. And at the top is a handful of intimidating and protective figures who make sure the swarm remains safe.

```statblock
creature: "Tunnel Viper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
