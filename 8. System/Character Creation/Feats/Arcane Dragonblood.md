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

You descend from a dragon that wields mastery of their magical abilities, such as a fortune dragon or mirage dragon. As such, you can instinctively grasp the intricacies of magic. You gain the trained proficiency rank in Arcana. If you would automatically become trained in Arcana (from your background or class, for example), you instead become trained in a skill of your choice. You gain the [[Arcane Sense]] skill feat. If you choose a draconic exemplar, you must choose an arcane dragon.

**Source:** `= this.source` (`= this.source-type`)
