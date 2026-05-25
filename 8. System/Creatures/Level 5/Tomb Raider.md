---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tomb Raider"
level: "5"
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
    desc: "+13"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +13, Deception +7, Society +9, Stealth +11, Thievery +13, Architecture Lore +11, Engineering Lore +11"
abilityMods: ["+3", "+4", "+1", "+2", "+2", "+0"]
abilities_top:
  - name: "Hazard Spotter"
    desc: "Even if the tomb raider isn't [[Searching]], they get a check to find traps that normally require them to be Searching."
armorclass:
  - name: AC
    desc: "21; **Fort** +10, **Ref** +15, **Will** +11"
health:
  - name: HP
    desc: "75"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Kukri +15 (`pf2:1`) (agile, trip), **Damage** 1d6+9 slashing"
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+9 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +15 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Trick Attack"
    desc: "`pf2:1` The tomb raider chooses one of their weapons. The next attack with that weapon this turn deals an additional 2d6 precision damage. In addition, the tomb raider can Interact to draw or reload the weapon."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Great treasure awaits those willing to explore the hazardous depths of ancient tombs and forgotten dungeons. Some tomb raiders seek the riches of bygone eras; others recover pieces of history thought lost to the sands of time.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Tomb Raider"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
