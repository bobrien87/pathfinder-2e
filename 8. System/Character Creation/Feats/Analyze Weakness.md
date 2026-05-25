---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Rogue]]"]
prerequisites: "sneak attack 2d6"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have identified a creature with [[Recall Knowledge]].

Your knowledge of a creature's physiology helps you attack with pinpoint accuracy. You carefully study a creature that you've identified to scope out particularly weak points in its positioning or physical form. The next time you deal sneak attack damage to the chosen creature with a Strike before the end of your turn, add an additional 2d6 precision damage.

At 11th level, the additional damage becomes 3d6, and at 17th level it becomes 4d6.

**Source:** `= this.source` (`= this.source-type`)
