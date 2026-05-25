---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dvorovoi"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Crafting +8, Nature +9, Stealth +9, Household Lore +11"
abilityMods: ["+3", "+2", "+1", "-1", "+0", "+1"]
abilities_top:
  - name: "Master of the Yard"
    desc: "The dvorovoi helps or causes trouble in the yard, milking or scaring cows, protecting or scattering tools, and so forth. A yard so blessed never encounters random accidents such as fires, and any checks to [[Craft]], [[Earn Income]], [[Repair]], or [[Subsist]] in the yard receive a +2 circumstance bonus. If the dvorovoi is unfriendly, such checks take a –2 circumstance penalty instead, as the dvorovoi hides things, makes noise when people try to sleep, tangles weaving, and otherwise makes life a misery. A domovoi must spend a week in a place before these benefits occur."
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
armorclass:
  - name: AC
    desc: "18; **Fort** +10, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "44; **Weaknesses** cold iron 5"
abilities_mid:
  - name: "Shy"
    desc: "A dvorovoi is naturally [[Invisible]] while within sight of their bound home. The dvorovoi can become visible, or even selectively visible-allowing some people to see them."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pitchfork +12 (`pf2:1`), **Damage** 1d8+6 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 0, attack +0<br>**2nd** [[Entangling Flora]], [[Speak with Animals]] (At Will)<br>**1st** [[Charm (Animals Only)]], [[Command (Animals Only)]], [[Mending]], [[Prestidigitation]], [[Telekinetic Hand]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Traditionally, the dvorovoi is seen as the domovoi's younger sibling and has charge of a peasant's yard and all the animals and tools within. Animals favored by the dvorovoi become healthy, strong, and obedient, while less-loved livestock are exhausted and miserable. Peasants with a resident dvorovoi make sure to formally introduce new livestock to the house spirit and placate the spirit by leaving meals in the shed. Dvorovoi loathe white-furred animals and will chase away any all-white cows or horses, though they have no similar grudge against chickens.

House spirits are shy, often helpful, sometimes wrathful fey who dwell alongside peasants and farmers. They reside in the house, the yard, the granary, the bathhouse—wherever people build and live. Due to this proximity, house spirits often take on the mannerisms or appearance of nearby mortals. Their reclusive nature and tendency to go unseen earned them the moniker of "spirits," though in truth they're fully embodied fey.

House spirits take an almost parental interest in "their" mortals. Given proper respect, these fey work tirelessly for their charges—they chop wood, care for livestock, mend clothes, sweep the floor, and tend to the stove. If offended, though, the house spirit becomes a menace, frightening animals or children and ruining belongings.

```statblock
creature: "Dvorovoi"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
