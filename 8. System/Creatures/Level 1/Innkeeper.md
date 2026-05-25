---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Innkeeper"
level: "1"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +6, Diplomacy +6, Society +7, Accounting Lore +5, Alcohol Lore +7, Cooking Lore +5"
abilityMods: ["+2", "+0", "+0", "+2", "+2", "+3"]
abilities_top:
  - name: "Font of Gossip"
    desc: "The innkeeper's business gives them insight into the neighborhood's happenings. A person can [[Gather Information]] from an innkeeper in 30 minutes rather than canvassing an entire neighborhood. Each person can learn gossip from an innkeeper only once per day, and only if the innkeeper is friendly or helpful to that individual. Whatever information the innkeeper knows about a given topic doesn't change if someone else asks the innkeeper about that topic, unless the innkeeper has since learned more."
  - name: "Home Base Brawler"
    desc: "The innkeeper knows how to settle fights that break out. When the innkeeper is fighting in their establishment, their Strikes gain a +1 circumstance bonus to the attack roll, deal an additional 1d4 damage, and gain the nonlethal trait if they don't already have it. The innkeeper can choose not to gain this benefit."
armorclass:
  - name: AC
    desc: "14; **Fort** +7, **Ref** +3, **Will** +9"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Broom +7 (`pf2:1`) (two hand d8), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Pewter Mug +5 (`pf2:1`) (thrown 10), **Damage** 1d4+2 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Innkeeper's Advice"
    desc: "`pf2:3` **Frequency** once per day <br>  <br> **Effect** The innkeeper gives some pertinent advice to a single creature other than themself. For 24 hours, when that creature fails a skill check or saving throw, they can recall this advice and reroll the check, using the second result instead. Once that creature uses this ability, its effect ends. A creature that receives the Innkeeper's Advice is temporarily immune to the ability for 1 month."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The sight of an inn is a welcome one to any weary traveler. Innkeepers can often be found cleaning the common room, overseeing the evening meal, or settling in new lodgers. Innkeepers keep an eye on their neighbors' doings and are often excellent sources of information.

Society is built upon the backs of laborers.

```statblock
creature: "Innkeeper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
