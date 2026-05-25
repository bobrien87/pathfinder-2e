---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Palatine Detective|Palatine Detective]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Palatine Detective Dedication"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your study of a variety of esoteric texts and supernatural matters has broadened your mind and improved your spellcasting. Choose a 1st-rank occult or divine spell. You can cast this spell once per day as an innate spell. At 6th level, you gain a 2nd-rank spell of the same tradition you chose, and at 8th level, you gain a 3rd-rank spell, also of that tradition.

**Special** You can take this feat a second time, choosing spells from the other available tradition.

**Source:** `= this.source` (`= this.source-type`)
