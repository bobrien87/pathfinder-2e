---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Druid]]", "[[Manipulate]]", "[[Spellshape]]"]
prerequisites: "Untamed Form"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With additional care and effort, you can take on an alternate shape for a longer period of time. If your next action is to cast untamed form, the spell's rank is 2 lower than normal (minimum 1st rank), but you can remain transformed for up to 1 hour or the listed duration (whichever is longer). You can still Dismiss untamed form as normal.

**Source:** `= this.source` (`= this.source-type`)
