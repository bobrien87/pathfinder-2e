---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Automaton]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've attuned your core to allow you to phase in and out of the Astral Plane, allowing you to teleport periodically. You can cast [[Translocate]] once per hour as a 4th-rank innate arcane spell.

**Enhancement** Your attunement allows you to teleport in a series of quick jumps rather than in one big leap. You can expend your hourly use of translocate as a free action when you begin your turn. If you do, your Strides are augmented until the end of your turn, allowing you to instantly teleport to any point you could reach with your Speed instead of traversing normally to the location. While augmented, your Strides gain the teleportation trait. Your augmented Strides don't trigger reactions that can be triggered by move actions or upon leaving or entering a square, unless those reactions trigger on teleportation.

**Source:** `= this.source` (`= this.source-type`)
