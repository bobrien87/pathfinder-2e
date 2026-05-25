---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Adept"
level: "-1"
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
    desc: "+4"
languages: "Common"
skills:
  - name: Skills
    desc: "Arcana +5, Diplomacy +3, Occultism +5, Society +5, Scribing Lore +5"
abilityMods: ["+0", "+2", "+0", "+3", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "14; **Fort** +2, **Ref** +4, **Will** +6"
health:
  - name: HP
    desc: "8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
  - name: "Melee strike"
    desc: "Journal +6 (`pf2:1`) (nonlethal, thrown 10), **Damage** 1d6 bludgeoning"
spellcasting:
  - name: "Occult Spells Known"
    desc: "DC 15, attack +7<br>**1st** [[Daze]], [[Detect Magic]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Focused Thinker"
    desc: "`pf2:1` The adept concentrates to muster knowledge and wisdom. While focusing, they gain a +2 status bonus to checks to [[Recall Knowledge]], but take a –2 penalty to Perception. They can Dismiss this focused state."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Adepts have unlocked only the most minor of occult mysteries. A few are chosen by accomplished practitioners for further training.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Adept"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
