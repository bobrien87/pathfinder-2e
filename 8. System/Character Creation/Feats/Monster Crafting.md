---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[Skill]]"]
prerequisites: "master in Survival"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can use the parts of monsters to aid in crafting. You can use the body of a monster to help [[Craft]] items, using Survival instead of Crafting for the Craft activity when you do so. If parts of the monster's body are valuable, you can expend them toward the item's raw material cost as well. (The GM makes the determination if the monster's entry doesn't list any valuable materials from its body.)

If you spend additional days working on the item, reduce the Price using the monster's level instead of your own. Certain items may require specific creatures in their Craft requirement.

**Source:** `= this.source` (`= this.source-type`)
