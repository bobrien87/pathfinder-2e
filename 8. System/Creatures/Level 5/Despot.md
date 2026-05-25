---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Despot"
level: "5"
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
    desc: "+11"
languages: "Common, Diabolic"
skills:
  - name: Skills
    desc: "Athletics +11, Deception +13, Diplomacy +11, Intimidation +13, Performance +13, Religion +11, Society +13, Warfare Lore +13"
abilityMods: ["+2", "+2", "+0", "+4", "+2", "+4"]
abilities_top:
  - name: "Persistent Lies"
    desc: "Any creature deceived by the despot's Deception skill believes the deception more readily on the next day. Any later Perception checks attempted against the despot's Deception DC take a –2 circumstance penalty, as do other creatures' attempts to convince the creature otherwise, such as through Diplomacy or further Deception."
  - name: "Sorcerous Potency"
    desc: "When the despot Casts a Spell from a spell slot that deals damage, they gain a status bonus to the spell's initial damage equal to the spell's rank."
  - name: "Tongue of Flame"
    desc: "When the despot casts [[Charm]], [[Diabolic Edict]], [[Enthrall]], or [[Floating Flame]], either a target takes 1 fire damage per spell rank, or the despot gains a +2 status bonus to Deception checks for 1 round."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +9, **Will** +13"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spiked Gauntlet +15 (`pf2:1`) (agile, free hand), **Damage** 1d4+6 piercing"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 23, attack +14<br>**3rd** (3 slots) [[Chilling Darkness]], [[Enthrall]]<br>**2nd** (4 slots) [[Blood Vendetta]], [[Calm]], [[Floating Flame]], [[See the Unseen]]<br>**1st** (4 slots) [[Bane]], [[Command]], [[Daze]], [[Fear]], [[Harm]], [[Ignition]], [[Message]], [[Sanctuary]], [[Shield]], [[Void Warp]]"
  - name: "Sorcerer Bloodline Spells"
    desc: "DC 22, attack +14<br>**1st** [[Diabolic Edict]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Despots live to amass and exploit power over others.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Despot"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
