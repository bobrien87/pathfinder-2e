---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Rogue]]"]
prerequisites: "legendary in Deception"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You use clever tactics to mislead your foes as you sneak away. You [[Sneak]] while leaving a decoy behind. The decoy acts as the spell [[Mislead]], though you aren't [[Invisible]], just [[Undetected]]. You can continue to concentrate to move your decoy, as with the spell, whether or not you remain [[Hidden]] throughout the duration. Once you use Perfect Distraction, you need to spend 10 minutes to set up another decoy before you can use it again.

**Source:** `= this.source` (`= this.source-type`)
