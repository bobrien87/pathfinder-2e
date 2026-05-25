---
type: creature
group: ["Goblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Goblin War Chanter"
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
    desc: "Acrobatics +6, Deception +7, Occultism +4, Performance +7, Stealth +6"
abilityMods: ["+2", "+3", "+2", "+1", "+0", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +8, **Will** +5"
health:
  - name: HP
    desc: "16"
abilities_mid:
  - name: "Goblin Scuttle"
    desc: "`pf2:r` **Trigger** A goblin ally ends a move action adjacent to the goblin. <br>  <br> **Effect** The goblin war chanter [[Step|Steps]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dogslicer +8 (`pf2:1`) (agile, backstabber, finesse), **Damage** 1d6+2 slashing"
  - name: "Ranged strike"
    desc: "Shortbow +8 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6 piercing"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 17, attack +7<br>**1st** (2 slots) [[Bless]], [[Courageous Anthem]], [[Figment]], [[Message]], [[Soothe]], [[Telekinetic Hand]], [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Goblin Song"
    desc: "`pf2:1` The war chanter sings annoying goblin songs, distracting foes with silly and repetitive lyrics. The chanter attempts a Performance check against the Will DCs of up to two enemies within @Template[emanation|distance:30]{30 feet}. This has the usual traits and restrictions for a Performance check. <br> - **Critical Success** The target takes a -1 status penalty to Perception checks and Will saves for 1 minute.  <br>  <br> > [!danger] Effect: Goblin Song (Critical Success) <br> - **Success** As critical success, but the target is affected for only one round.  <br>  <br> > [!danger] Effect: Goblin Song (Success) <br> - **Critical Failure** The target is temporarily immune to Goblin Song for 1 hour."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

While all goblins enjoy singing, goblin war chanters pride themselves on mastering the art of vocal performance. Their ballads and jingles are undeniably catchy, and serve their purpose in battle well, inspiring goblins and distracting foes. Whether they are actually enjoyable is entirely subjective.

These small humanoids typically have green or gray skin and large heads with wide ears. While some goblins are civilized and have worked hard to be considered upstanding members of humanoid communities, many are impetuous and vicious creatures who delight in wreaking havoc. These goblins think nothing of slaughtering livestock, stealing, or burning down a building purely for momentary delight. They revel in playing malicious tricks on taller humanoids, whom they call "longshanks."

Goblins are superstitious, with an intense awe of magic and a fascination with fire; goblins who master magic or fire earn great respect from their kin. Most other humanoids find it difficult to understand goblins' outlook: they hate canines but eagerly share their lairs with so-called "goblin dogs," they fearlessly attack larger creatures but are terrified of horses, and they despise vegetables yet consider pickles a delicacy. To a goblin, of course, these are all perfectly sensible life choices.

```statblock
creature: "Goblin War Chanter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
