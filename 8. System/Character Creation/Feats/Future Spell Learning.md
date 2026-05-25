---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Time Mage|Time Mage]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Time Mage Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

More future memories of time magic percolate back to the present, teaching you spells you've yet to learn. Add [[Behold the Weave]], [[Cast into Time]], [[Haste]], [[Loose Time's Arrow]], [[Quicken Time]], [[Slow]], and [[Stagnate Time]] to your spell list. If you have a repository of spells, like a witch's familiar or a spellbook, add these spells to it. If you have a spell repertoire, when you gain this feat you can retrain one spell in it, replacing it with one of the added spells.

**Source:** `= this.source` (`= this.source-type`)
