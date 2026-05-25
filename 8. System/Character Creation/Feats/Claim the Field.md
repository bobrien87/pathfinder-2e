---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Commander]]"]
prerequisites: "Plant Banner"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your banner is attached to a thrown weapon.

You hurl your banner forward with precision, claiming the battlefield for yourself and your allies. You Plant the Banner, but you can place it at any corner within the required weapon's first range increment, rather than the corner of your square. The calculated confidence of this brash maneuver unnerves your enemies; any enemy who attempts to damage or remove your banner while it is planted in this way must succeed at a [[Will]] save against your class DC or the attempt fails. On a critical failure, the enemy is [[Fleeing]] for 1 round. This is an incapacitation and mental effect.

**Source:** `= this.source` (`= this.source-type`)
