---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Dwarf]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a deep reverence for and connection to stone. You can cast [[One with Stone]] as a 3rd-rank divine innate spell once per day.

If you have the [[Stonemason's Eye]] feat, you can attempt to find unusual stonework and stonework traps that require legendary proficiency in Perception. If you have both Stonemason's Eye and legendary proficiency in Perception, when the GM rolls a secret check for you to notice unusual stonework, you keep your bonus from Stonemason's Eye.

**Source:** `= this.source` (`= this.source-type`)
