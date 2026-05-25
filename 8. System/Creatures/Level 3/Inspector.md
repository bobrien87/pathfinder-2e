---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Inspector"
level: "3"
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
    desc: "+12"
languages: "Common (up to 3 additional languages)"
skills:
  - name: Skills
    desc: "Athletics +9, Diplomacy +12, Intimidation +13, Medicine +8, Society +12, Legal Lore +13"
abilityMods: ["+1", "+3", "+0", "+4", "+3", "+1"]
abilities_top:
  - name: "+3 to Sense Motive, Seek, or Search"
    desc: ""
  - name: "Investigation Specialist"
    desc: "For encounters involving investigation, the inspector is a 5th-level challenge."
  - name: "Sense Demise"
    desc: "The inspector can `act sense-motive` on a corpse, learning about the creature in the moments before its death."
armorclass:
  - name: AC
    desc: "19; **Fort** +5, **Ref** +10, **Will** +12"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +12 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1 piercing plus 1d6+4 piercing"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning plus 1 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Unavoidable Question"
    desc: "`pf2:1` **Frequency** once per turn <br>  <br> **Effect** The inspector Demoralizes a creature and asks a question. On a success, the next Strike the inspector attempts against that target deals an additional 1d6 precision damage. If the target spends an action on their next turn to answer the question, either truthfully or by succeeding at a DC 25 [[Deception]] check, they are temporarily immune to the inspector's Unavoidable Question for 1 minute."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Inspectors cultivate a wide selection of skills to investigate arson, murder, and other serious crimes, usually in major urban centers. They can assist adventurers, perhaps noticing an object or creature that seems out of the ordinary without being sure why.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Inspector"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
