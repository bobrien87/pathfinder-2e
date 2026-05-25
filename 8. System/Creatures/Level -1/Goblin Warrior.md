---
type: creature
group: ["Goblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Goblin Warrior"
level: "-1"
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
    desc: "+2; [[Darkvision]]"
languages: "Goblin, Common"
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +2, Nature +1, Stealth +5"
abilityMods: ["+0", "+3", "+1", "+0", "-1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +7, **Will** +3"
health:
  - name: HP
    desc: "6"
abilities_mid:
  - name: "Goblin Scuttle"
    desc: "`pf2:r` **Trigger** A goblin ally ends a move action adjacent to the goblin. <br>  <br> **Effect** The goblin warrior [[Step|Steps]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dogslicer +7 (`pf2:1`) (agile, backstabber, finesse), **Damage** 1d6 slashing"
  - name: "Ranged strike"
    desc: "Shortbow +7 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The frontline fighters of goblin tribes prefer to fight in large groups—especially when they can outnumber their foes at least three to one.

These small humanoids typically have green or gray skin and large heads with wide ears. While some goblins are civilized and have worked hard to be considered upstanding members of humanoid communities, many are impetuous and vicious creatures who delight in wreaking havoc. These goblins think nothing of slaughtering livestock, stealing, or burning down a building purely for momentary delight. They revel in playing malicious tricks on taller humanoids, whom they call "longshanks."

Goblins are superstitious, with an intense awe of magic and a fascination with fire; goblins who master magic or fire earn great respect from their kin. Most other humanoids find it difficult to understand goblins' outlook: they hate canines but eagerly share their lairs with so-called "goblin dogs," they fearlessly attack larger creatures but are terrified of horses, and they despise vegetables yet consider pickles a delicacy. To a goblin, of course, these are all perfectly sensible life choices.

```statblock
creature: "Goblin Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
