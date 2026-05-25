---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Kitsune]]"]
prerequisites: "fox alternate form"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're especially nimble while in your full fox shape. While you've Changed Shape into a fox, you gain the following benefits.

- You can use your own Speed if it's higher than 20 feet.
- You can use your own Athletics modifier for checks to [[High Jump]] or [[Long Jump]].
- You can scale short distances with a bit of a running start. When you attempt to Climb, and your previous action was to Stride at least 20 feet along solid ground, you gain a climb Speed of 20 feet for the duration of that Climb action.

**Source:** `= this.source` (`= this.source-type`)
