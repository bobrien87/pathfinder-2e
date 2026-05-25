---
type: creature
group: ["Goblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Goblin Commando"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +6, Intimidation +5, Nature +5, Stealth +6"
abilityMods: ["+3", "+3", "+2", "-1", "+0", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +8, **Will** +5"
health:
  - name: HP
    desc: "18"
abilities_mid:
  - name: "Goblin Scuttle"
    desc: "`pf2:r` **Trigger** A goblin ally ends a move action adjacent to the goblin. <br>  <br> **Effect** The goblin commando [[Step|Steps]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horsechopper +8 (`pf2:1`) (reach 10 ft., trip, versatile p), **Damage** 1d8+3 slashing"
  - name: "Ranged strike"
    desc: "Shortbow +8 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The theoretical leaders of goblin raids are called goblin commandos. In practice, goblin commandos rarely continue to lead their comrades once a battle has begun. Most shirk their responsibilities in favor of wading into the fray and claiming more glory from their tribe-mates.

These small humanoids typically have green or gray skin and large heads with wide ears. While some goblins are civilized and have worked hard to be considered upstanding members of humanoid communities, many are impetuous and vicious creatures who delight in wreaking havoc. These goblins think nothing of slaughtering livestock, stealing, or burning down a building purely for momentary delight. They revel in playing malicious tricks on taller humanoids, whom they call "longshanks."

Goblins are superstitious, with an intense awe of magic and a fascination with fire; goblins who master magic or fire earn great respect from their kin. Most other humanoids find it difficult to understand goblins' outlook: they hate canines but eagerly share their lairs with so-called "goblin dogs," they fearlessly attack larger creatures but are terrified of horses, and they despise vegetables yet consider pickles a delicacy. To a goblin, of course, these are all perfectly sensible life choices.

```statblock
creature: "Goblin Commando"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
