---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Gunslinger]]"]
prerequisites: "Ricochet Master"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The more obstacles between you and your target, the deadlier your shots become, as you ricochet off multiple surfaces to hit them. When using [[Ricochet Shot]], your shot can bounce off of any surface within your weapon's first three range increments and the target can't benefit from cover unless they have total cover on all sides.

In addition, a creature must attempt a [[Will]] save against your class DC the first time in an encounter you attack it with a Ricochet Shot. If it fails, it's [[Stunned]] 2 and is unable to determine where your shot originated.

**Source:** `= this.source` (`= this.source-type`)
