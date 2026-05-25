---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Surgeon"
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
    desc: "+14"
languages: "Common"
skills:
  - name: Skills
    desc: "Crafting +10, Diplomacy +8, Medicine +16"
abilityMods: ["+1", "+3", "+1", "+2", "+4", "+0"]
abilities_top:
  - name: "Doctor's Hand"
    desc: "When the surgeon rolls a critical failure on a check to [[Treat Disease]], [[Treat Poison]], or [[Treat Wounds]], they get a failure instead."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +7, **Will** +10"
health:
  - name: HP
    desc: "30"
abilities_mid:
  - name: "Medical Specialist"
    desc: "In medical matters, a surgeon is a 6th-level challenge."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scalpel +11 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Scalpel +11 (`pf2:1`) (agile, finesse, thrown 10, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
  - name: "Melee strike"
    desc: "Bonesaw +9 (`pf2:1`) (trip), **Damage** 1d8+1 slashing"
spellcasting: []
abilities_bot:
  - name: "Medical Malpractice"
    desc: "`pf2:1` The surgeon attempts a [[Medicine]] check against the Fortitude DC of one living creature they can see within 60 feet. <br>  <br> On a success, the surgeon's melee Strikes deal an extra 1d6 precision damage against that creature (2d6 on a critical success) until 1 minute passes or the surgeon critically hits that creature, whichever comes first. <br>  <br> Using this action again ends any previous one. A surgeon can target an individual creature no more than once per day with this ability."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The surgeon specializes in the physical alteration of the body to prevent the spread of disease, removing necrotic and decaying flesh to help the whole to survive. Few healers know the science of anatomy and physiology better.

The world is a dangerous place. Thankfully, there are those who devote their lives to easing the pain and suffering of others.

```statblock
creature: "Surgeon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
