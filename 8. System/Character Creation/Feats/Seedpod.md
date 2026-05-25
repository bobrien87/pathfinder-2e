---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Leshy]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your body produces a nearly endless supply of hard seedpods. You gain a seedpod ranged unarmed attack with a range increment of 30 feet that deals 1d4 bludgeoning damage. On a critical hit, a seedpod bursts, issuing forth a tangle of vegetation that imposes a –10-foot circumstance penalty on the target's Speed until the start of your next turn. Seedpods do not add critical specialization effects.

> [!danger] Effect: Seedpod

**Source:** `= this.source` (`= this.source-type`)
