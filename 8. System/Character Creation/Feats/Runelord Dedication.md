---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Runelord|Runelord]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Class]]", "[[Dedication]]"]
prerequisites: "runelord"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your connection to your sin suffuses all magic you use. When you contemplate or indulge in your sin to Refocus, you can also exchange one spell you have prepared for one of your curriculum or sin spells of the same rank.

Runelord (Class Archetype)

**Source:** `= this.source` (`= this.source-type`)
