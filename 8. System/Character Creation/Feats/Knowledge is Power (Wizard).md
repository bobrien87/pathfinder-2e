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

Your academic knowledge about a creature allows you to subtly alter your magic to defeat them. When you critically succeed at a [[Recall Knowledge]] check about a creature, you can invoke your knowledge to make the creature take a –1 circumstance penalty to either AC and saves against the next attack you make against it, or the next spell you cast that it needs to defend against. The creature takes the same penalty to its attack or DC the next time it attacks against you or causes you to attempt a save against one of its effects.

If you share this information with your allies, they gain the benefits as well. If not used, the bonuses end after 1 minute.

**Source:** `= this.source` (`= this.source-type`)
