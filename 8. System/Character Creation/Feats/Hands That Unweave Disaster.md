---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Mythic]]"]
prerequisites: "Thief's Calling"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your hands move with uncanny sureness, dismantling danger. When you attempt an Acrobatics check to [[Grab an Edge]], you can spend a Mythic Point to attempt the check at mythic proficiency. You can expend a Mythic Point when attempting to [[Disable a Device]] to attempt the check at mythic proficiency. As normal when attempting a check with mythic proficiency, this allows you to attempt to Disable a Device even if the check normally requires expert or greater proficiency.

**Source:** `= this.source` (`= this.source-type`)
