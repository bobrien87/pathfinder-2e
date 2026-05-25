---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Nephilim]]"]
prerequisites: "Aeonbound"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your affinity with process and order makes you a natural artisan. You are trained in Crafting. If you were already trained in Crafting, you instead gain the [[Specialty Crafting]] skill feat in a specialty of your choice; if you have both, you instead become trained in a skill of your choice. In addition, when you critically fail to Repair an item, you get a failure instead.

*Note: If you were already trained in Crafting, you need to manually add the Specialty Crafting feat or select an alternative skill.*

**Source:** `= this.source` (`= this.source-type`)
