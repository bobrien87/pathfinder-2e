---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Grandmaster"
level: "17"
rare_01: "Uncommon"
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
    desc: "+35; [[Lifesense]] (imprecise) 60 feet"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +33, Athletics +33, Diplomacy +25, Intimidation +25, Medicine +25, Stealth +25, Martial Arts Lore +30"
abilityMods: ["+6", "+4", "+3", "+1", "+5", "+1"]
abilities_top:
  - name: "Powerful Fists"
    desc: "The grandmaster's fist Strikes don't take penalties when making lethal attacks, and fist Strikes are treated as adamantine, cold iron and silver."
armorclass:
  - name: AC
    desc: "40; **Fort** +28, **Ref** +32, **Will** +27"
health:
  - name: HP
    desc: "310"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Temple Sword +33 (`pf2:1`) (magical, trip), **Damage** 3d8+14 slashing"
  - name: "Melee strike"
    desc: "Fist +33 (`pf2:1`) (agile, magical, nonlethal, unarmed), **Damage** 3d6+14 bludgeoning"
  - name: "Melee strike"
    desc: "Shuriken +31 (`pf2:1`) (magical, reload 0, thrown 20), **Damage** 3d4+14 piercing"
spellcasting:
  - name: "Monk Focus Spells"
    desc: "DC 38, attack +34<br>**8th** [[Touch of Death]]<br>**5th** [[Wind Jump]]<br>**3rd** [[Qi Blast]]<br>**2nd** [[Harmonize Self]]"
abilities_bot:
  - name: "Disrupt Qi"
    desc: "`pf2:2` The grandmaster attempts an unarmed Strike against a living creature. On a hit, the creature takes 3d6 persistent void damage and is [[Enfeebled]] 2 until the persistent damage ends."
  - name: "Flurry of Blows"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The grandmaster makes two fist Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses. <br>  <br> The grandmaster can substitute any number of the attacks with temple sword Strikes or attempts to `act grapple`, `act reposition`, `act shove`, or `act trip`."
  - name: "Forbidden Palm"
    desc: "`pf2:3` **Requirements** The grandmaster has at least 1 Focus Point <br>  <br> **Effect** The grandmaster casts [[Touch of Death]] (spending 1 Focus Point as normal). Any time the target attempts a Fortitude save against this *touch of death*, the grandmaster takes 40 damage and is permanently [[Enfeebled]] 1. If the target gets a critical success, it's [[Stunned]] 1; if it gets a success or failure the stunned condition it gains is increased by 1, and any damage it takes is increased by 40."
  - name: "One-Millimeter Punch"
    desc: "`pf2:2` `pf2:2` or `pf2:3` <br>  <br> The grandmaster makes a single, carefully controlled unarmed Strike that deals 2 additional dice of damage, or 4 additional dice if the grandmaster spent 3 actions. If this damages the target, the grandmaster can choose to make the target attempt a DC 38 [[Fortitude]] save. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target is pushed back 5 feet. <br> - **Failure** The target is pushed back 10 feet. <br> - **Critical Failure** The target is pushed back 10 feet for each action the grandmaster spent on One-Millimeter Punch."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Beyond the black belt, there is the grandmaster. If a battle breaks out, this incredible warrior possesses unparalleled qi adeptness and punches that can kill.

Martial artists strive to master the art of hand-to-hand fighting.

```statblock
creature: "Grandmaster"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
