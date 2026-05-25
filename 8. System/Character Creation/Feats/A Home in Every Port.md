---
type: feat
source-type: "Remaster"
level: "11"
traits: ["[[Downtime]]", "[[General]]"]
prerequisites: "Charisma +3"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a reputation in towns and villages you've visited, and residents are always willing to open their doors to you.

When in a town or village, during downtime, you can spend 8 hours to locate a resident willing to provide lodging for you and up to six allies for up to 24 hours at no charge. The standard of living within the acquired lodging is comfortable, and square meals are provided at no cost.

After 24 hours, you must pay standard prices for further lodging and meals or use this feat again to find a new resident willing to host you.

**Source:** `= this.source` (`= this.source-type`)
