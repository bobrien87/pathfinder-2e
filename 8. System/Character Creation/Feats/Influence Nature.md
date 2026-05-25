---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[Downtime]]", "[[General]]", "[[Skill]]"]
prerequisites: "master in Nature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With patience and time, you can make bird calls, leave game trails, and ultimately influence the behavior of a certain type of animals in the region to favor and even aid you in the days to come.

The GM determines the DC of any check required and the amount of time your work requires (usually at least a day or two of downtime). While you can't directly control how you've influenced nature, you can hope for certain effects, such as easier hunts or birds falling silent whenever danger is approaching.

If you're legendary in Nature, you can elicit these same adjustments to animal behavior in the area by spending only 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
