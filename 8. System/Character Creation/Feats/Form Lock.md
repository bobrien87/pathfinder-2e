---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wrestler|Wrestler]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Attack]]", "[[Monk]]"]
prerequisites: "Wrestler Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a creature [[Grabbed]] or [[Restrained]].

Your ability to manipulate your enemy's entire body is potent enough that you can tear and break apart alternate forms. Attempt an Athletics check to counteract a polymorph effect currently affecting the creature you have grabbed or restrained. If the target is somehow under the effect of multiple polymorph effects, you can choose which one to attempt to counteract; the GM chooses randomly if the separate effects aren't obvious. The target is then temporarily immune for 1 day.

**Source:** `= this.source` (`= this.source-type`)
