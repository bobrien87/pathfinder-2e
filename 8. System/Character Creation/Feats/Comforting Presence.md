---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[General]]", "[[Mental]]", "[[Skill]]"]
prerequisites: "master in Occultism"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An adjacent ally becomes frightened or stupefied.

You use your occult connection to your allies to take on the fear and confusion they feel. Focus on your own calmness and pull in your nearby allies' emotions. Reduce the [[Frightened]] and [[Stupefied]] condition values of adjacent allies by 1, and increase your frightened and stupefied condition values by the same amount.

**Source:** `= this.source` (`= this.source-type`)
