---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Tripkee]]"]
prerequisites: "snaptongue tripkee"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your tongue can momentarily latch on as readily as your hands. So long as you can freely open your mouth, you do not need free hands in order to [[Disarm]], [[Grab an Edge]], [[Reposition]], or [[Trip]]. If you have the [[Long Tongue]] feat, you can Disarm, Grab an Edge, Reposition, and Trip with your tongue at a distance that is 5 feet beyond your normal reach.

**Source:** `= this.source` (`= this.source-type`)
