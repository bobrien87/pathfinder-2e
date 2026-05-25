---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Acrobat"
level: "2"
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
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +8, Deception +5, Performance +9, Stealth +8, Circus Lore +5"
abilityMods: ["+2", "+4", "+2", "+1", "+0", "+1"]
abilities_top:
  - name: "Acrobatic Specialist"
    desc: "For encounters involving contests of acrobatics and similar activities, the acrobat is a 5th-level challenge."
  - name: "Steady Balance"
    desc: "When the acrobat rolls a success on an Acrobatics check, they get a critical success instead. <br>  <br> They aren't [[Off Guard]] when attempting to [[Balance]] and can attempt an Acrobatics check instead of a Reflex save to [[Grab an Edge]]."
  - name: "Sneak Attack"
    desc: "The acrobat deals an extra 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +11, **Will** +4"
health:
  - name: HP
    desc: "30"
abilities_mid:
  - name: "Cat Fall"
    desc: "The acrobat treats all falls as 25 feet shorter."
  - name: "Nimble Dodge"
    desc: "`pf2:r` **Trigger** The acrobat is targeted with a melee or ranged attack by an attacker they can see <br>  <br> **Effect** The acrobat gains a +2 circumstance bonus to AC against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Foot +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Swinging Strike"
    desc: "`pf2:2` The acrobat swings on a rope or trapeze, moving up to double their Speed. At any point during the swing, they can make a melee Strike."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Acrobats perform feats of agility, balance, and strength.

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Acrobat"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
