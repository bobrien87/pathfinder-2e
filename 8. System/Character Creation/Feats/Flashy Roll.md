---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Swashbuckler]]"]
prerequisites: "Flashy Dodge"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can use [[Flashy Dodge]] before attempting a Reflex save, in addition to its original trigger. If you do, the circumstance bonus applies to your Reflex save against the triggering effect.

When you use Flashy Dodge and the triggering attack fails or critically fails, or when you succeed or critically succeed at the saving throw, you can also Stride up to 10 feet as part of the reaction. If you do, the reaction gains the move trait. You can use Flashy Roll while Flying or Swimming instead of Striding if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
