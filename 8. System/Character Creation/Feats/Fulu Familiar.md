---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Familiar Sage|Familiar Sage]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Talisman]]"]
prerequisites: "Familiar Sage Dedication, expert in Occultism or Religion"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can imprint your familiar's spiritual essence into a fulu, a small paper charm that can be affixed to objects, creatures, or structures. You gain the [[Create Familiar Fulu]] action, which you can use once per day; at 12th level, this increases to twice per day, and at 18th level, it increases to three times per day.

**Source:** `= this.source` (`= this.source-type`)
