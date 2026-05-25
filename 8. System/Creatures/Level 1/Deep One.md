---
type: creature
group: ["Amphibious", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Deep One"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]], [[Wavesense]] (imprecise) 30 feet"
languages: "Aklo, Common"
skills:
  - name: Skills
    desc: "Athletics +6, Intimidation +5, Religion +6, Stealth +4, Survival +4"
abilityMods: ["+3", "+1", "+4", "+2", "+1", "+1"]
abilities_top:
  - name: "Pressurized"
    desc: "A deep one is immune to damage and other negative effects from changes in water pressure."
armorclass:
  - name: AC
    desc: "16; **Fort** +9, **Ref** +4, **Will** +8"
health:
  - name: HP
    desc: "24; **Resistances** cold 2, piercing 3"
abilities_mid:
  - name: "Endless"
    desc: "A deep one doesn't age and is immune to spells and other effects that inflict magical aging. Unless killed, a deep one lives forever."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Claw +7 (`pf2:1`) (agile), **Damage** 1d4+3 piercing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 14, attack +6<br>**1st** [[Daze]], [[Hydraulic Push]]"
abilities_bot:
  - name: "Fervent Frenzy"
    desc: "`pf2:3` The deep one makes two claw Strikes and one jaws Strike in any order. If the target creature is currently frightened by a deep one's Share Devotion ability, it's [[Off Guard]] against these attacks. The deep one becomes [[Clumsy]] 1 until the start of their next turn."
  - name: "Share Devotion"
    desc: "`pf2:2` The deep one fills their enemies' minds with terrible hallucinations of the Outer Gods. All enemy creatures within a @Template[type:emanation|distance:30] must attempt a DC 17 [[Will]] save; regardless of the result, a creature is temporarily immune to Share Devotion for 24 hours. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** As failure, plus [[Dazzled]] for as long as it's frightened."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

An average mature deep one weighs 300 pounds and measures 7 feet in length, though they appear shorter on land due to their wide stance and natural hunch.

Lumbering, amphibious, and deathless humanoids known as deep ones inhabit coastal areas and deep ocean trenches all across Golarion. Though most simply wish to be left alone, others work tirelessly to grow their ranks.

```statblock
creature: "Deep One"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
