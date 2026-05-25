---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Toady"
level: "0"
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
    desc: "+3"
languages: "Common (one additional language spoken by their boss)"
skills:
  - name: Skills
    desc: "Athletics +4, Deception +2, Stealth +6, Thievery +4"
abilityMods: ["+2", "+2", "+3", "-1", "+1", "+0"]
abilities_top:
  - name: "+6 Bonus on Perception to Eavesdrop"
    desc: ""
  - name: "Master Sends Their Regards"
    desc: "A toady can deliver a message from their boss to [[Demoralize]] using their boss's Intimidation modifier instead of their own."
armorclass:
  - name: AC
    desc: "14; **Fort** +9, **Ref** +6, **Will** +3"
health:
  - name: HP
    desc: "20; **Weaknesses** mental 2"
abilities_mid:
  - name: "Human Shield"
    desc: "`pf2:r` **Trigger** The toady's boss takes damage from an attack, and the toady is adjacent to them <br>  <br> **Effect** The toady takes the damage instead, along with any secondary effects of attack. This damage can't be reduced in any way."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sap +6 (`pf2:1`) (agile, nonlethal), **Damage** 1d6+2 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Scurry"
    desc: "`pf2:1` The toady Strides, then can `act hide`. They can attempt to Hide from creatures without cover or being [[Concealed]], but at a –2 circumstance penalty."
  - name: "Throw Cargo"
    desc: "`pf2:2` A toady carries a heavy load of supplies at their boss's behest. They hurl a heavy item they're carrying, which explodes on impact to deal @Damage[1d10[bludgeoning]|options:area-damage] damage to all creatures in a @Template[type:burst|distance:5] with a DC 14 [[Reflex]] save."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

These minions perform the thankless tasks that keep their master's vile machine running. Whether out of loyalty or fear, a toady serves their boss faithfully.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Toady"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
