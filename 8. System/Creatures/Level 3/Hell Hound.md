---
type: creature
group: ["Beast", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hell Hound"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Fire"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Diabolic ((Can't Speak Any Language))"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +9, Stealth +8, Survival +9"
abilityMods: ["+4", "+3", "+2", "-2", "+2", "-2"]
abilities_top:
  - name: "Pack Attack"
    desc: "The hell hound's Strikes deal 1d4 extra damage to creatures within the reach of at least two of the hell hounds' allies."
armorclass:
  - name: AC
    desc: "17; **Fort** +9, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "40; **Immunities** fire; **Weaknesses** cold 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +13 (`pf2:1`) (magical, unarmed, unholy), **Damage** 1d8+4 piercing plus 1d6 fire"
spellcasting: []
abilities_bot:
  - name: "Hellfire Breath"
    desc: "`pf2:1` The hell hound breathes flames that deal @Damage[4d6[fire]|options:area-damage] damage to all creatures in a @Template[cone|distance:15] (DC 19 [[Reflex]] save). <br>  <br> The hell hound can't use Hellfire Breath again for 1d4 rounds. If the hell hound would take fire damage or be targeted by a fire effect, their Hellfire Breath recharges."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A hell hound's appearance dismisses any doubts as to their infernal origins—flesh the color of burning pitch, teeth as sharp as any fiend's pitchfork, and a shroud of ever-burning hellfire are all trademark features.

Hell hounds are fiendish, extraplanar canines hailing from the Pit that can hunt down quarry and breathe supernatural gouts of flame. They are temperamental and quick to exhibit aggressive behavior.

```statblock
creature: "Hell Hound"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
