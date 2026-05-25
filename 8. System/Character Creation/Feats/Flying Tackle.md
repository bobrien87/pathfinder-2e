---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Flourish]]", "[[Guardian]]"]
prerequisites: "trained in Athletics"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You barrel forward, gathering enough momentum to take down a threatening foe. Stride and then [[Leap]], or attempt to [[High Jump]] or [[Long Jump]]. If you end your movement adjacent to a foe, you can attempt to [[Trip]] that foe. If you succeed at the Athletics check to Trip, you get a critical success instead. You can use Flying Tackle while Burrowing, Climbing, Flying, or Swimming instead of Striding if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
