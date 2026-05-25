---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Downtime]]", "[[Reincarnated]]"]
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Some feel trapped by their choices and have a tough time reinventing themselves. To you, this dilemma is just a natural part of reincarnation. [[Retraining]] other feats or skill increases during downtime only takes 4 days instead of a week, and class features that require a choice can be retrained in a week instead of a month. You also never need to find a teacher to retrain, as the memories of abilities you possessed in past lives are superior to any instructor.

**Source:** `= this.source` (`= this.source-type`)
