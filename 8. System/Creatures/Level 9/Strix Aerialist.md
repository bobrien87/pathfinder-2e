---
type: creature
group: ["Humanoid", "Strix"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Strix Aerialist"
level: "9"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Strix"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Low-Light Vision]]"
languages: "Common, Strix"
skills:
  - name: Skills
    desc: "Acrobatics +22, Athletics +20, Deception +18, Performance +20, Society +16, Stealth +20, Thievery +18"
abilityMods: ["+3", "+5", "+2", "+1", "+2", "+3"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The strix aerialist's Strikes deal an additional 2d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "28; **Fort** +18, **Ref** +21, **Will** +15"
health:
  - name: HP
    desc: "120"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +21 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 2d4+7 piercing"
  - name: "Melee strike"
    desc: "Dagger +21 (`pf2:1`) (agile, magical, thrown 10, versatile s), **Damage** 2d4+7 piercing"
spellcasting: []
abilities_bot:
  - name: "Aerial Feint"
    desc: "`pf2:1` The aerialist chooses a creature within 20 feet and attempts an Acrobatics check against the target's Perception DC. On a success, the target is [[Off Guard]] against the aerialist's Strikes for 1 round."
  - name: "Dive Bomb"
    desc: "`pf2:2` The strix aerialist Flies up to double its fly Speed in a straight line, descending at least 10 feet, and then makes a melee Strike."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Strix aerialists are talented acrobats.

Strix, called itarii in their own language, are avian humanoids with sprawling, dark-feathered wings and large talons. They possess angular features and piercing eyes that are fixed facing forward.

```statblock
creature: "Strix Aerialist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
