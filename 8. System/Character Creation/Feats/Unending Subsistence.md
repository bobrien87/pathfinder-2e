---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your mythic power allows you to take a small amount of food and replicate it near endlessly. When you attempt a Society or Survival check to [[Subsist]], you can spend a Mythic Point to attempt the check at mythic proficiency. Succeeding at the check always provides enough food and shelter for you and up to a dozen other creatures. On a critical success, all creatures you obtain food and shelter for gain a +2 circumstance bonus to Fortitude saving throws for the next 24 hours.

> [!danger] Effect: Unending Subsistence

**Source:** `= this.source` (`= this.source-type`)
