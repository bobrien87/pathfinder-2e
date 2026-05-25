---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Rogue]]"]
prerequisites: "legendary in Acrobatics"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Using fantastic acrobatic skill, you can walk for brief stretches across insubstantial surfaces. When you Stride, you can move across water, air, and solid surfaces that can hold only limited weight as if they were normal ground. If you Stride over a trap with a weight-sensitive pressure plate, you don't trigger it. At the end of your turn, you sink, fall, break fragile surfaces, or trigger traps as normal for your current location.

**Source:** `= this.source` (`= this.source-type`)
