---
type: feat
source-type: "Remaster"
level: "15"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "legendary in Diplomacy"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can negotiate incredibly quickly in adverse situations. You attempt to [[Make an Impression]] and then [[Request]] your opponent cease their current activity and engage in negotiations. You take a –5 penalty to your Diplomacy check. Generally, the DC of this check is the creature's Will DC, although your GM may modify it based on the situation. Some creatures may be unable to stop regardless of their personal desires, and even those who agree to parley might ultimately find your arguments lacking and return to violence.

**Source:** `= this.source` (`= this.source-type`)
