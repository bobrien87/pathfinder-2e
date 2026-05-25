---
type: feat
source-type: "Remaster"
level: "15"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "legendary in Athletics"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your unparalleled athletic skill allows you to jump impossible distances. Triple the distance you jump on a successful [[Long Jump]] (so you could jump 90 feet with an Athletics result of 30). When you successfully [[High Jump]], use the distance jumped and distance limit for a Long Jump but don't triple the distance.

You can jump a distance greater than your Speed by spending additional actions when you Long Jump or High Jump. For each additional action spent, add your Speed to the distance limit.

**Source:** `= this.source` (`= this.source-type`)
