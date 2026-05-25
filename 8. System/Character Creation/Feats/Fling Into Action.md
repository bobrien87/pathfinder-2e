---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You release mythic power to turn disaster into opportunity and hurl yourself into an advantageous position. When you attempt a Reflex save, you can spend a Mythic Point to attempt the save at mythic proficiency. If the check is successful, you immediately fling yourself up to 30 feet in a direction of your choice, or up to 60 feet on a critical success. When flinging yourself in this manner, you can move the entire distance in a straight horizontal or vertical line, or you can move 5 feet horizontally for every 10 feet you move vertically. For example, if you got a critical success using Fling Into Action while Grabbing an Edge as you fall from the middle of a cliff, you could hurl yourself 40 feet up the cliffside and 20 feet forward onto a plateau at the top of the cliff.

**Source:** `= this.source` (`= this.source-type`)
