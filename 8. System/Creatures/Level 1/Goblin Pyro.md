---
type: creature
group: ["Goblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Goblin Pyro"
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
    desc: "+4; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Acrobatics +7, Stealth +7, Fire Lore +7"
abilityMods: ["+0", "+4", "+2", "+0", "-1", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +5, **Ref** +9, **Will** +4"
health:
  - name: HP
    desc: "15"
abilities_mid:
  - name: "Goblin Scuttle"
    desc: "`pf2:r` **Trigger** A goblin ally ends a move action adjacent to the goblin. <br>  <br> **Effect** The goblin pyro [[Step|Steps]]."
speed: "0 feet"
attacks: []
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 16, attack +6<br>**1st** (3 slots) [[Breathe Fire]], [[Grease]], [[Ignition]], [[Light]], [[Tangle Vine]], [[Telekinetic Hand]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Some goblins take their people's admiration of fire fully into the realm of deadly obsession. These pyromaniacs can be a great boon to a band of goblin raiders eager to torch their enemies and wreak havoc. More often, however, their presence is a double-edged sword; in the heat of the moment, goblin pyros sometimes lose sight of their tribe's goals and simply set fire to anything that will burn—including their own allies. Goblin squads are also prone to distraction, and more than one goblin raid has failed because its members were too busy watching a massive blaze.

These small humanoids typically have green or gray skin and large heads with wide ears. While some goblins are civilized and have worked hard to be considered upstanding members of humanoid communities, many are impetuous and vicious creatures who delight in wreaking havoc. These goblins think nothing of slaughtering livestock, stealing, or burning down a building purely for momentary delight. They revel in playing malicious tricks on taller humanoids, whom they call "longshanks."

Goblins are superstitious, with an intense awe of magic and a fascination with fire; goblins who master magic or fire earn great respect from their kin. Most other humanoids find it difficult to understand goblins' outlook: they hate canines but eagerly share their lairs with so-called "goblin dogs," they fearlessly attack larger creatures but are terrified of horses, and they despise vegetables yet consider pickles a delicacy. To a goblin, of course, these are all perfectly sensible life choices.

```statblock
creature: "Goblin Pyro"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
