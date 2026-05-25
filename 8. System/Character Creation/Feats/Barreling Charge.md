---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Barbarian]]", "[[Fighter]]", "[[Flourish]]"]
prerequisites: "trained in Athletics"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You rush forward, moving enemies aside to reach your foe. You Stride, attempting to move through your enemies' spaces. Roll an [[Athletics]] check and compare the result to the Fortitude DC of each creature whose space you attempt to move through during your Stride, moving through its space on a success but ending your movement before entering its space on a failure. You can then Strike, regardless of how your Stride ended. You can use Barreling Charge to Burrow, Climb, Fly, or Swim instead of Stride if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
