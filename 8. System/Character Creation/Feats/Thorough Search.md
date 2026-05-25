---
type: feat
source-type: "Remaster"
level: "3"
traits: ["[[General]]"]
prerequisites: "expert in Perception"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You take your time searching to ensure you find everything. When Searching, you can take twice as long to search. Normally this means you [[Search]] at up to one quarter of your Speed, to a maximum of 150 feet per minute to check everything, or 75 feet per minute to check everything before you walk into an area. If you do and the GM rolls your secret check to [[Seek]] to notice something, you gain a +2 circumstance bonus to that Perception check and if you succeed, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
