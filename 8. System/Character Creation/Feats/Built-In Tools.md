---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Inventor]]", "[[Modification]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've built tools into your innovation so you can access and use them easily. When you take this feat, choose up to two sets of tools you own, such as thieves' tools or healer's tools, that weigh a total of 2 Bulk or less. These tools become part of your innovation. The innovation's Bulk doesn't increase from this addition. As long as you are wielding, wearing, or adjacent to your innovation, you have the same quick access to these tools as the tools you are wearing, and they don't count against the usual limit of tools you can wear.

**Source:** `= this.source` (`= this.source-type`)
