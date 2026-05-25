---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Champion]]", "[[Magical]]"]
prerequisites: "Faithful Steed"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are riding your mount.

Confident in your faith, you Command an Animal to order your mount to Stride up to twice its Speed (or up to three times its Speed if you used 3 actions for Faithful Stride). During this movement, your mount can Stride across liquid and other surfaces that don't support its weight. If your mount ends its movement on a surface that can't support it, your mount (and you) fall in or it collapses as normal.

**Source:** `= this.source` (`= this.source-type`)
