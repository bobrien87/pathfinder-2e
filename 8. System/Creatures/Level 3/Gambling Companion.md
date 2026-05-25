---
type: creature
group: ["Humanoid", "Tengu"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gambling Companion"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Tengu"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Low-Light Vision]]"
languages: "Common, Tengu (plus three others)"
skills:
  - name: Skills
    desc: "Deception +11, Diplomacy +11, Society +9, Thievery +9, Games Lore +16"
abilityMods: ["+0", "+3", "+0", "+2", "+1", "+4"]
abilities_top:
  - name: "+2 to Sense Motive"
    desc: ""
  - name: "Social Specialist"
    desc: "For social encounters involving gaming or gambling, the gambling companion is a 5th-level challenge"
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +12, **Will** +9"
health:
  - name: HP
    desc: "46"
abilities_mid:
  - name: "Gamer's Guidance"
    desc: "When the gambling companion successfully Aids a skill check related to games or gambling, the ally rolls twice and takes the higher result instead of gaining the usual bonus."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +10 (`pf2:1`) (finesse, unarmed), **Damage** 1d6+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Distracting Trick"
    desc: "`pf2:2` **Requirements** The gambling companion is wielding cards or dice <br>  <br> **Effect** The gambling companion performs a quick trick with the cards or dice to [[Feint]], then makes a beak Strike against the same target. If the Feint succeeds, the Strike deals an additional 1d6 precision damage."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A reputation for protecting against bad luck, combined with skill and knowledge, establish these tengu as ideal gambling companions. Their role includes providing local knowledge of establishments as well as the various games available. Refined skills of observation and an ability to read other players increases the value of their services. The example provided is for a companion who frequents the finer establishments. For some areas, a patron would look for a companion with greater fighting skills to also fill the role of bodyguard

Originally hailing from the continent of Tian Xia, tengu have spread across the globe. Though some staunchly uphold traditions, gazing at the sky from the tallest mountaintops, other tengu remain on the ground, adapting and blending into the societies in which they settle.

```statblock
creature: "Gambling Companion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
