---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Lineage]]", "[[Nephilim]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your lineage is influenced or directly tied to the supernatural inhabitants of the Perfect City of Axis, a realm of pure and absolute order. This energy suffuses your body and helps it maintain coherency, resisting effects that would undermine your function or mar your otherwise orderly form. You and your allies can Treat your Wounds without a healer's toolkit. Once per day, when someone rolls a failure or a critical failure on a check to Treat your Wounds, you can focus on your internal cohesion to increase the degree of success by one step.

**Source:** `= this.source` (`= this.source-type`)
