---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Apothecary"
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
    desc: "+5"
languages: "Common"
skills:
  - name: Skills
    desc: "Crafting +5, Medicine +10, Nature +8"
abilityMods: ["+0", "+1", "+1", "+3", "+3", "+1"]
abilities_top:
  - name: "Medical Specialist"
    desc: "For encounters involving making medicine or alchemical contests, the apothecary is a 3rd-level challenge."
  - name: "Medical Wisdom"
    desc: "The apothecary can identify the effect of any alchemical composition or medical ingredient using only their senses. This typically takes 1 minute."
armorclass:
  - name: AC
    desc: "14; **Fort** +8, **Ref** +3, **Will** +5"
health:
  - name: HP
    desc: "8; **Resistances** poison 2"
abilities_mid:
  - name: "+1 Circumstance Bonus on Saves vs. Poisons"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Stone Pestle +4 (`pf2:1`), **Damage** 1d6 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
  - name: "Ranged strike"
    desc: "Acid Flask +5 (`pf2:1`) (splash, range 20 ft.), **Damage** 1 acid plus 1d6 acid plus 1 acid"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The apothecary skillfully combines materials into unguents and medicines using crushed herbs, curative minerals, and potent extracts.

The world is a dangerous place. Thankfully, there are those who devote their lives to easing the pain and suffering of others.

```statblock
creature: "Apothecary"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
