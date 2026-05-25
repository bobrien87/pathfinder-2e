---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Monk]]"]
prerequisites: "Twisting Petal Stance"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're in [[Twisting Petal Stance]].

Your hands move in a hypnotic and distracting flurry that throws your foes off-balance before you cast them away with a violent pirouette. You Step. Then each enemy within your reach must attempt a Will save against the higher of your [[Will]] save{class DC} or your [[Will]] save{Deception DC}; on a failure, they're [[Off Guard]] to melee attacks from you and your allies until the end of your next turn. Then, `act shove` up to three adjacent enemies; each Shove counts toward your multiple attack penalty, but you don't increase your penalty until after you've resolved all the Shove attempts.

**Source:** `= this.source` (`= this.source-type`)
