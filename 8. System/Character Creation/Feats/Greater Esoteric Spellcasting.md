---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Palatine Detective|Palatine Detective]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Esoteric Spellcasting"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your understanding of magic has evolved, and so has your spellcasting. You become an expert in the spell attack modifier and spell DC statistics. Also, choose a tradition from which you can cast innate spells due to the Esoteric Spellcasting feat. You also gain a 4th-rank spell of that tradition as an innate spell you can cast once a day. At 12th level, you gain a 5th-rank spell, and at 14th level, you gain a 6th-rank spell, both of the same tradition.

**Special** You can take this feat a second time, choosing a different eligible tradition.

**Source:** `= this.source` (`= this.source-type`)
