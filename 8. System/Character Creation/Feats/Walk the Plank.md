---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pirate|Pirate]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Pirate Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You frighten a foe into moving where you want them, traditionally demanding they walk the plank.

Attempt to [[Demoralize]] an opponent. On a success, in addition to the normal effects, you can also force the target to Stride up to its Speed immediately. You choose the path the target takes, but you can't force it to move into an obviously harmful space (such as into hazardous terrain or a space where it would fall) unless your check was a critical success. As normal for forced movement, this movement doesn't trigger reactions.

The target then becomes temporarily immune to Walk the Plank for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
