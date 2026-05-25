---
type: creature
group: ["Changeling", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Changeling Exile"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Changeling"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Common, Wildsong"
skills:
  - name: Skills
    desc: "Deception +9, Medicine +9, Nature +11, Stealth +8, Survival +9"
abilityMods: ["+4", "+1", "+0", "+0", "+4", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "19; **Fort** +7, **Ref** +8, **Will** +11"
health:
  - name: HP
    desc: "45"
abilities_mid:
  - name: "+2 Circumstance to All Saves vs. Dream and Sleep"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claws +11 (`pf2:1`) (agile), **Damage** 1d4+4 slashing"
  - name: "Melee strike"
    desc: "Staff +11 (`pf2:1`) (two hand d8), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Sickle +11 (`pf2:1`) (agile, trip), **Damage** 1d4+4 slashing"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 21, attack +11<br>**2nd** (2 slots) [[Darkness]], [[Humanoid Form]]<br>**1st** (3 slots) [[Breathe Fire]], [[Spider Sting]], [[Ventriloquism]]<br>**Cantrips** [[Ignition]], [[Light]], [[Read Aura]], [[Tangle Vine]]"
  - name: "Druid Order Spells"
    desc: "DC 21, attack +13<br>**1st** [[Untamed Form]], [[Untamed Shift]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

This changeling exile is the child of a cuckoo hag.

As children of hags, perhaps destined to become hags themselves, changelings face a life of conflict. Born of supernatural creatures who usually kill and consume the child's father, changelings are deposited into their father's society to be raised. These offspring appear to be members of their paternal ancestry and have been found among dwarves, gnomes, orcs, goblins, and others, but human-ancestry changelings are by far the most common. Within the normal range for their ancestry, changelings tend toward slighter builds, darker hair, and pale complexions, though their most common feature is a nearly universal heterochromia, leading to widespread superstition about individuals with different colored eyes.

When changelings come of age, they sometimes manifest abilities granted by their hag heritage. Some gain the ability to see in the dark, some grow fingernails long and hard enough to serve as claws, and others gain even stranger abilities specific to their hag mother. For instance, dream mays, the children of cuckoo hags, can gain an enhanced ability to resist the magic of dreams and sleep. Other types of changelings include slag mays, the children of iron hags; callow mays, the children of sweet hags; brine mays, the children of sea hags; and others for each type of hag.

As beings infused with supernatural power, changelings find themselves drawn to either the occult magic common among hags or primal magic. At roughly the same time in their lives, many changelings—women in particular—begin to hear the Call, a psychic urging from their hag mother luring them away from the communities that raised them. If followed, the Call eventually leads the changeling to the hag's coven, where they are twisted into hags themselves. Some changelings are able to resist this Call and continue on with their mortal lives. The fact that the Call disproportionately targets female changelings has led to a widespread misunderstanding that all changelings are female, while changelings of other genders are simply assumed to be members of their paternal ancestry.

```statblock
creature: "Changeling Exile"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
