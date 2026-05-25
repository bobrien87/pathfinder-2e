---
type: feat
source-type: "Remaster"
level: "15"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "legendary in Crafting"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can find ways to craft just about anything, despite restrictions. As long as you have the appropriate Crafting skill feat (such as Magical Crafting for magic items) and meet the item's level and proficiency requirements, you ignore just about any other requirement, such as being of a specific ancestry or providing spells. If a requirement adds to the item's cost, you must still pay it (including castings of spells that themselves have a cost). You can't ignore requirements of special items that have exclusive means of access and Crafting, such as artifacts. The GM decides whether you can ignore a requirement.

**Source:** `= this.source` (`= this.source-type`)
