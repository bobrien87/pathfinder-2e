---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bloodrager|Bloodrager]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Bloodrager Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The power within your blood grows. You gain the [[Basic Spellcasting Feat]] benefits. Each time you gain a spell slot of a new rank from the bloodrager archetype, add a common spell of the appropriate tradition and rank to your repertoire. In addition, when you Cast a Spell from your repertoire and you are at least [[Drained]] 1, increase the extra damage dealt by that spell from Rage by 1.

**Source:** `= this.source` (`= this.source-type`)
