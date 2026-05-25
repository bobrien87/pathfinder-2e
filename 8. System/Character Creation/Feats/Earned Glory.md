---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Aiuvarin]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Elves often struggle with underestimating aiuvarins, and you are experienced at telling stories of your accomplishments to gain their respect. You are trained in Performance. If you would automatically become trained in Performance (from your background or class, for example), you instead become trained in a skill of your choice.

You gain the [[Impressive Performance]] feat. When you attempt a Performance check to [[Make an Impression]] on an elf, if you roll a critical failure, you get a failure instead.

**Source:** `= this.source` (`= this.source-type`)
