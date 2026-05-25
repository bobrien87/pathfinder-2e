---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have trained your mind and body to tolerate polymorph magic for longer periods of time, so long as you prepare for the change appropriately. When preparing a polymorph spell that lasts 1 minute and grants a battle form, you can prepare the spell in a slot 2 ranks higher than normal. This doesn't grant any of the normal benefits of heightening a spell, but the spell lasts up to 10 minutes. For example, if you prepared animal form in a 4th-rank slot with Form Retention, you would cast a 2nd-rank [[Animal Form]] that lasts for up to 10 minutes. If the spell can be Dismissed, that doesn't change.

**Source:** `= this.source` (`= this.source-type`)
