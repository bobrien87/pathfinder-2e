---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mixed Martial Artist"
level: "7"
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
    desc: "+15"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +17, Martial Arts Lore +17"
abilityMods: ["+4", "+2", "+3", "+1", "+2", "+1"]
abilities_top:
  - name: "Powerful Fists"
    desc: "The mixed martial artist's fist Strikes don't take penalties when making lethal attacks."
armorclass:
  - name: AC
    desc: "24; **Fort** +18, **Ref** +15, **Will** +12"
health:
  - name: HP
    desc: "130"
abilities_mid:
  - name: "Takedown Fluidity"
    desc: "`pf2:r` **Trigger** The mixed martial artist's last action was a successful [[Grapple]], [[Shove]], or [[Trip]]. <br>  <br> **Effect** The mixed martial artist uses Stance Shift."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, magical, nonlethal, unarmed), **Damage** 1d8+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Stance Shift"
    desc: "`pf2:1` The mixed martial artist enters a stance of their choice, gaining the listed circumstance bonus and Strike but losing the ability to make other Strikes. <br>  <br> - **Elbow Knockout Stance** +2 to Athletics checks to `act shove` or `act trip`; **Melee** `pf2:1` cross elbow +16 (nonlethal, trip, unarmed) **Damage** 2d6+8 bludgeoning <br> - **Secure Grapple Stance** +2 to Athletics checks to `act grapple`; **Melee** `pf2:1` grappling limb +16 (grapple, nonlethal, unarmed) **Damage** 2d4+8 bludgeoning <br> - **Thrashing Barrage Stance** +2 to damage against [[Off Guard]] opponents; **Melee** `pf2:1` thrashing fist +16 (forceful, nonlethal, unarmed) **Damage** 2d8+8 bludgeoning"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

These fighters combine the takedowns of a wrestler with aggressive stances and unorthodox blows, ensuring that contenders won't know what hit them.

Martial artists strive to master the art of hand-to-hand fighting.

```statblock
creature: "Mixed Martial Artist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
