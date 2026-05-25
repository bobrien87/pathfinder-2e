---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Monk]]"]
prerequisites: "One-Inch Punch"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your punches have incredible force and control. When you damage a target using One-Inch Punch, you can focus your qi to send the foe flying. If you do, the target must attempt a [[Fortitude]] save against your class DC.
- **Critical Success** The target is unaffected.
- **Success** The target is pushed back 5 feet.
- **Failure** The target is pushed back 10 feet.
- **Critical Failure** The target is pushed back 10 feet for each action you spent on One-Inch Punch.

**Source:** `= this.source` (`= this.source-type`)
