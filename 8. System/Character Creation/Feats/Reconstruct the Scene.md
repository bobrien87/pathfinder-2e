---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Concentrate]]", "[[Investigator]]", "[[Rogue]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You spend 1 minute surveying a small location (such as a single room) to get an impression of events that occurred there in the last day. This involves moving about the area and studying footprints, spilled drinks or blood, and so forth. You get an indistinct mental impression of significant events that happened there. This gives you clues and details of the past, including the overall events and their time frame, but it's not a perfect record. This also isn't enough to identify who was involved in these events if you weren't already aware the person was there. As determined by the GM, you also pick out various seemingly small details that could serve as important clues, like a memorable weapon someone used for a murder or the type of cloak someone wore when passing through.

**Source:** `= this.source` (`= this.source-type`)
