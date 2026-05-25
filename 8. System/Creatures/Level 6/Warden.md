---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Warden"
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
    desc: "+17"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +15, Nature +11, Stealth +13, Survival +13"
abilityMods: ["+4", "+2", "+3", "+1", "+2", "+1"]
abilities_top:
  - name: "Warden's Protection"
    desc: "A warden deals an extra 1d8 damage to any creature trespassing on the territory the warden protects."
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +15, **Will** +11"
health:
  - name: HP
    desc: "100"
abilities_mid:
  - name: "Warding Strike"
    desc: "`pf2:r` **Trigger** One of the warden's enemies within 100 feet attacks one of the warden's allies or a person the warden is sworn to protect <br>  <br> **Effect** The warden Strikes the triggering enemy. If the Strike hits, the enemy's attack is deflected, reducing its damage by 8, or by 16 if the warden's Strike was a critical hit."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bastard Sword +16 (`pf2:1`) (two hand d12), **Damage** 1d8+10 slashing"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Longbow +17 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 1d8+8 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Wardens are the chief guardians of borders and frontiers. Whether standing watch over a single village or an entire region, wardens keep a vigilant eye out for threats to their charges. Wardens are stalwart folk, often called to duty by Erastil to protect those around them. Be it times of war or along the frontier, wardens are often the balanced edge of a blade between a community and the wilds at its fringes.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Warden"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
