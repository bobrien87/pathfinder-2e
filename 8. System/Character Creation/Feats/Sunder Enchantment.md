---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Barbarian]]"]
prerequisites: "Sunder Spell"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can focus your superstition to break the magic of an item, in addition to destroying freestanding spells and those active on creatures. When you [[Sunder a Spell]], you can instead attempt to counteract either an unattended magic item or one of your target's magic items. If your counteract attempt succeeds, the item becomes a mundane item of its type for 10 minutes. If you target an artifact, an intelligent item, or a similarly particularly powerful item, your counteract attempt automatically fails.

**Source:** `= this.source` (`= this.source-type`)
