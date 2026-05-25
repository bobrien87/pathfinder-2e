---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Jotunborn]]"]
prerequisites: "Plane Hop"
frequency: "once per PT1H"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** Your turn begins.

You concentrate on the spaces between planes, allowing you to enhance your movement for a short period. Your Strides become augmented until the end of your turn, allowing you to instantly teleport to any point you could reach with your Speed instead of traversing normally to the location. While augmented, your Strides gain the teleportation trait. Your augmented Strides don't trigger reactions that can be triggered by move actions or upon leaving or entering a square, unless those reactions are specifically triggered by teleportation.

**Source:** `= this.source` (`= this.source-type`)
