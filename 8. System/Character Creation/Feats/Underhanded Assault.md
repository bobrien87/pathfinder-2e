---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Rogue]]"]
prerequisites: "trained in Stealth"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You capitalize on the distraction provided by an ally. You `act sneak options=underhanded-assault` up to a foe adjacent to one of your allies. You can roll against the foe you're Sneaking up on, even if it's currently observing you, as though you were [[Hidden]]. You take a –2 penalty on your Stealth check. If your Stealth check against the chosen foe succeeds, you can make a melee Strike against that foe at the end of your Sneak.

**Source:** `= this.source` (`= this.source-type`)
