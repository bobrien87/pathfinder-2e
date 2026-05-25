---
type: creature
group: ["Catfolk", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Leaping Thief"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Catfolk"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]]"
languages: "Amurrun, Common"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +7, Deception +10, Society +9, Stealth +11, Thievery +9"
abilityMods: ["+0", "+4", "+2", "+1", "+0", "+3"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The leaping thief deals an extra 1d6 precision damage to [[Off Guard]] creatures."
  - name: "Unexpected Angle"
    desc: "When the leaping thief successfully Tumbles Through a foe's space or [[Leaps]] to a position higher than a foe, the foe is [[Off Guard]] against the next attack the leaping thief makes before the end of their turn."
armorclass:
  - name: AC
    desc: "20; **Fort** +7, **Ref** +11, **Will** +7"
health:
  - name: HP
    desc: "38"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw Blade +11 (`pf2:1`) (agile, deadly d8, disarm, finesse, versatile p), **Damage** 1d4+6 slashing"
  - name: "Melee strike"
    desc: "Claw +11 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4+6 slashing"
spellcasting: []
abilities_bot:
  - name: "Coiled Leap"
    desc: "`pf2:2` The leaping thief [[Leaps]] up to 10 feet vertically or 30 feet horizontally."
  - name: "Stealthy Pad"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The leaping thief Steps, then Hides or Sneaks, ignoring difficult terrain for this movement."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Some catfolk take advantage of their natural agility to steal from those too slow to catch them. They usually target notorious misers and others who obviously have money to spare—sometimes to help the needy, sometimes for simple profit.

Catfolk can be found traveling almost anywhere, and they are quick to settle down for a chat when they encounter fellow travelers. Some trade stories, act as guides, or operate at the fringes of polite society.

```statblock
creature: "Leaping Thief"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
