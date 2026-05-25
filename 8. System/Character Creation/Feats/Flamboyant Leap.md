---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Swashbuckler]]"]
prerequisites: "master in Athletics, Flamboyant Athlete"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are capable of using a finisher.

You stylishly leap and deliver a powerful finisher. Make a [[Leap]], [[High Jump]], or [[Long Jump]] and attempt one single-action finisher at any point during your jump; the finisher can't be one that includes other movement, such as [[Mobile Finisher]]. Immediately after the finisher, you fall to the ground if you're in the air, even if you haven't reached the maximum distance of your jump. If the distance you fall is no more than the height of your jump, you take no damage and land upright.

When attempting a High Jump or Long Jump during a Flamboyant Leap, determine the DC using the Long Jump DCs, and increase the maximum distance to double your Speed, rather than just your Speed.

**Source:** `= this.source` (`= this.source-type`)
