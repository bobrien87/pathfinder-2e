---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Changeling]]", "[[Lineage]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are the child of a cuckoo hag, making one of your eyes violet or even black. Your mother's powers over sleep and dreams have given you a degree of resistance to those effects, granting you a +2 circumstance bonus to all saving throws against sleep effects and effects that cause or alter dreams.

In addition, sleep is more restorative for you. You regain HP equal to your Constitution modifier × double your level (instead of just × your level), and you reduce any drained and doomed conditions you have by 2 instead of by 1.

**Source:** `= this.source` (`= this.source-type`)
