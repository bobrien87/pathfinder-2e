---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Master of Disguise"
level: "7"
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
    desc: "+17"
languages: "Common, Dwarven, Elven, Gnomish, Halfling"
skills:
  - name: Skills
    desc: "Deception +18, Diplomacy +16, Performance +16, Society +17, Stealth +17, Thievery +15, Underworld Lore +15"
abilityMods: ["+0", "+4", "+0", "+2", "+3", "+5"]
abilities_top:
  - name: "+4 to Sense Motive"
    desc: ""
  - name: "Deep Cover"
    desc: "At most times, a master of disguise has infiltrated a specific organization, gaining a +2 circumstance bonus to `act gather-information`, `act impersonate`, `act lie`, or `act request` when dealing with its members."
  - name: "Disguise Specialist"
    desc: "For social encounters involving impersonation, the master of disguise is a 10th-level challenge."
  - name: "Double Take"
    desc: "If the master of disguise and the creature they're [[Impersonating]] are in each others' presence, the genuine creature must [[Lie]] if they're vouching for their own identity, and are treated as though they were Impersonating themself if someone [[Seeks]] in an attempt to pierce their disguise. The genuine creature can use their Deception modifier, Diplomacy modifier, or a +15 modifier, whichever is highest."
  - name: "Sneak Attack"
    desc: "The master of disguise deals an additional 3d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "25; **Fort** +11, **Ref** +17, **Will** +16"
health:
  - name: HP
    desc: "110"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +16 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+6 piercing"
  - name: "Melee strike"
    desc: "Dagger +16 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+6 piercing"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Impeccable Disguise"
    desc: "`pf2:3` The master of disguise creates a disguise and Impersonates. They gain a +5 status bonus to Deception checks to `act impersonate` or to tell a `act lie` that helps them maintain their disguise. When a spell or magical effect tries to read their mind, detect whether they're lying, or reveal their identity, they can attempt a [[Deception]] check against the spell or effect's DC. If they succeed, the effect reveals information appropriate to their cover identity or nothing (the GM determines which)."
  - name: "Shocking Reveal"
    desc: "`pf2:1` The master of disguise removes their disguise with a dramatic gesture. Any creatures that previously failed to see through the disguise is [[Off Guard]] to the master of disguise until the end of the turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A master of disguise uses costuming, makeup, and minor illusions to deceive. Some conceal their identity for years, infiltrating organizations under deep cover.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Master of Disguise"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
