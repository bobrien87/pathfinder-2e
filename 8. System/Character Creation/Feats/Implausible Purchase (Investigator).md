---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Investigator]]"]
prerequisites: "Predictive Purchase"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

It seems impossible, but you've analyzed every angle and are able to just keep pulling out exactly the item you need, even in far-flung locations.

You can use [[Prescient Planner]] even if you have already used it after purchasing goods, and you can use it as a single action instead of a 2-action activity, during which you [[Interact]] to draw the item.

In addition, five times per day, you can use Prescient Planner to pull out a common consumable item up to 6 levels lower than your level.

**Source:** `= this.source` (`= this.source-type`)
