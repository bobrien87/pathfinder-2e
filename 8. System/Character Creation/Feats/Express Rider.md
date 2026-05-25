---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Exploration]]", "[[General]]", "[[Skill]]"]
prerequisites: "trained in Nature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can encourage your mount to cover ground quickly. When calculating your travel Speed for the day while mounted, you can attempt a Nature check to Command an Animal to increase your mount's travel Speed. The DC is determined by the GM, but is typically based on the mount's level or the difficulty of the environment, whichever is harder. On a success, increase your mount's travel Speed by half. This has no effect on your mount's movement in encounters. This benefit extends to up to six other allies traveling with you, as long as all such allies are also mounted, or are quadrupeds with a Speed of at least 30 feet.

**Source:** `= this.source` (`= this.source-type`)
