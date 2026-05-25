---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Kholo]]"]
prerequisites: "sweetbreath kholo heritage"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You smell of honey and savory things. Your circumstance bonus to checks to [[Make an Impression]] if the target can smell your breath increases to +2. In addition, you can cast [[Enthrall]] as a 3rd-rank occult innate spell once per day, except the spell has a range of 30 feet and the olfactory trait instead of the auditory trait. Targets don't gain any circumstance bonus for disagreeing with you.

**Source:** `= this.source` (`= this.source-type`)
