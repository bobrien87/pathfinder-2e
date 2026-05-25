---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Librarian"
level: "-1"
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
languages: "Common, Draconic, Elven (up to 4 additional languages)"
skills:
  - name: Skills
    desc: "Arcana +9, Nature +8, Religion +8, Academia Lore +11, Library Lore +13"
abilityMods: ["+0", "+1", "+0", "+3", "+2", "+1"]
abilities_top:
  - name: "Methodical Research"
    desc: "When [[Searching]] through stacks of books, a librarian can find the answer to almost any question. This allows the librarian to use Library Lore in place of other lore skills, given enough time. The GM determines the DC of the check and the amount of time it takes (typically, a librarian can attempt three or four checks during 1 day of downtime)."
  - name: "Research Specialist"
    desc: "A librarian is a 3rd-level challenge for encounters involving research."
armorclass:
  - name: AC
    desc: "13; **Fort** +2, **Ref** +3, **Will** +7"
health:
  - name: HP
    desc: "6"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Book +4 (`pf2:1`) (nonlethal), **Damage** 1d4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
  - name: "Melee strike"
    desc: "Book +5 (`pf2:1`) (nonlethal, thrown 10), **Damage** 1d4 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Keepers of knowledge, librarians document discoveries, events, and laws. The best librarians record events twice: once for public record and again to record how events truly unfolded.

True power comes from knowledge—the power to shape the growth of kingdoms by mere whispers, stay three steps ahead of adversaries, or even know which flora is best for creating untraceable poisons.

```statblock
creature: "Librarian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
