---
type: creature
group: ["Beast", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Greater Hell Hound"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Fire"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Darkvision]], [[Scent]] (imprecise) 120 feet"
languages: "Diabolic ((Can't Speak Any Language))"
skills:
  - name: Skills
    desc: "Acrobatics +18, Athletics +19, Stealth +18, Survival +20"
abilityMods: ["+6", "+5", "+5", "-2", "+4", "-2"]
abilities_top:
  - name: "Pack Attack"
    desc: "The greater hell hound's Strikes deal 1d8 extra damage to creatures within the reach of at least two of their allies."
armorclass:
  - name: AC
    desc: "28; **Fort** +21, **Ref** +19, **Will** +16"
health:
  - name: HP
    desc: "150; **Immunities** fire; **Weaknesses** cold 10"
abilities_mid:
  - name: "Hellish Revenge"
    desc: "`pf2:r` **Trigger** The greater hell hound is critically hit by any Strike <br>  <br> **Effect** The greater hell hound's Hellfire Breath recharges. They can immediately use it as part of this reaction."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +21 (`pf2:1`) (magical, unarmed, unholy), **Damage** 2d8+6 piercing plus 2d6 fire"
spellcasting: []
abilities_bot:
  - name: "Hellfire Breath"
    desc: "`pf2:1` The hell hound breathes flames that deal @Damage[10d6[fire]|options:area-damage] damage to all creatures in a @Template[cone|distance:15] (DC 28 [[Reflex]] save.) <br>  <br> The hell hound can't use Hellfire Breath again for 1d4 rounds. If the greater hell hound would take fire damage or be targeted by a fire effect, their Hellfire Breath recharges."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Believed to be bred by the Kings of Hell themselves within vast kennels, greater hell hounds are the favored guards and hunting hounds of powerful fiends and, rarely, mortals who worship them and have earned their favor.

Hell hounds are fiendish, extraplanar canines hailing from the Pit that can hunt down quarry and breathe supernatural gouts of flame. They are temperamental and quick to exhibit aggressive behavior.

```statblock
creature: "Greater Hell Hound"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
