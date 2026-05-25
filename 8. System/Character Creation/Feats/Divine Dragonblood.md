---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dragonblood]]", "[[Lineage]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can trace your lineage to a dragon with almost deific powers, such as a diabolic dragon or empyreal dragon. You are blessed with a small bit of divine protection. You gain the trained proficiency rank in Religion. If you would automatically become trained in Religion (from your background or class, for example), you instead become trained in a skill of your choice. In addition, you are endowed quick reactions. You gain a +1 circumstance bonus to initiative rolls. If you choose a draconic exemplar, you must choose a divine dragon.

**Source:** `= this.source` (`= this.source-type`)
