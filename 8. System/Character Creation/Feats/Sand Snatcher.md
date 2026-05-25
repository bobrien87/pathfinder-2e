---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A figure of sand with grasping arms arises in an unoccupied square within 30 feet. You can choose to make it Small or Medium size, and it can flank. When the sand snatcher appears, you can have it attempt to [[Grapple]] one creature adjacent to it that's no more than one size larger than it. This Grapple uses your impulse attack roll instead of an Athletics check and shares your multiple attack penalty. The sand snatcher lasts until the end of your next turn, and you can Sustain the impulse up to 1 minute. Each time you Sustain the impulse, you can have the sand snatcher either Grapple again or Burrow, Climb, or Stride up to 20 feet. Attempts to [[Escape]] its grasp use your class DC.

**Level (10th)** You can also choose Large size.

**Level (14th)** You can also choose Large or Huge size.

**Source:** `= this.source` (`= this.source-type`)
