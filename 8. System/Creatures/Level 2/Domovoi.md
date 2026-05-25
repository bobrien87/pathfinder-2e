---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Domovoi"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Crafting +9, Stealth +7, Household Lore +10"
abilityMods: ["+1", "+3", "+1", "+3", "+5", "+1"]
abilities_top:
  - name: "Master of the Home"
    desc: "A home with a friendly domovoi is blessed, as the domovoi cooks, cleans, fetches water, and does a hundred other small tasks. A home so blessed never encounters random accidents such as fires, and any checks to [[Craft]], [[Earn Income]], [[Repair]], or [[Subsist]] in the home receive a +2 circumstance bonus. If the domovoi is unfriendly, such checks take a –2 circumstance penalty instead, as the domovoi hides things, makes noise when people try to sleep, tangles weaving, and otherwise makes life a misery. A domovoi must spend a week in a place before these benefits occur."
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Home Guardian"
    desc: "By commanding their home to attack, the domovoi can `act disarm skill=household-lore`, `act grapple skill=household-lore`, `act reposition skill=household-lore`, `act shove skill=household-lore`, or `act trip skill=household-lore` with their enraged home Strike. The domovoi uses their Household Lore instead of Athletics skill for these checks."
armorclass:
  - name: AC
    desc: "17; **Fort** +5, **Ref** +9, **Will** +11"
health:
  - name: HP
    desc: "35; **Weaknesses** cold iron 4"
abilities_mid:
  - name: "Shy"
    desc: "A domovoi is naturally [[Invisible]] while within sight of their bound home. The domovoi can become visible, or even selectively visible—allowing some people to see them."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Broom +7 (`pf2:1`), **Damage** 1d4+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Enraged Home (Bludgeoning) +9 (`pf2:1`) (primal, range 30 ft.), **Damage** 1d8+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Enraged Home (Piercing) +9 (`pf2:1`) (primal, range 30 ft.), **Damage** 1d8+4 piercing"
  - name: "Ranged strike"
    desc: "Enraged Home (Slashing) +9 (`pf2:1`) (primal, range 30 ft.), **Damage** 1d8+4 slashing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 18, attack +10<br>**1st** [[Mending]] (At Will), [[Prestidigitation]], [[Telekinetic Hand]], [[Telekinetic Projectile]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The elderly domovoi are patrons of the home and the dearest of all house spirits to the people they live with. Families with a domovoi leave a bowl of milk in the corner of the home in thanks, and peasants often take great pains to coax a domovoi to follow them to a new house.

An enraged domovoi rallies the home itself in their defense. Anything in the house could betray its residents. Crockery falls onto the heads of attackers, doors slam in their faces, carpets tangle their feet, and woe betide the attacker if someone has hung a sword on the wall.

House spirits are shy, often helpful, sometimes wrathful fey who dwell alongside peasants and farmers. They reside in the house, the yard, the granary, the bathhouse—wherever people build and live. Due to this proximity, house spirits often take on the mannerisms or appearance of nearby mortals. Their reclusive nature and tendency to go unseen earned them the moniker of "spirits," though in truth they're fully embodied fey.

House spirits take an almost parental interest in "their" mortals. Given proper respect, these fey work tirelessly for their charges—they chop wood, care for livestock, mend clothes, sweep the floor, and tend to the stove. If offended, though, the house spirit becomes a menace, frightening animals or children and ruining belongings.

```statblock
creature: "Domovoi"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
