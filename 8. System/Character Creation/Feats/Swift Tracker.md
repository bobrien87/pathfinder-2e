---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Ranger]]"]
prerequisites: "expert in Survival, Experienced Tracker"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your keen eyes catch signs of passage even when you're moving. You can move at your full Speed while you [[Track]]. If you have master proficiency in Survival, you don't need to attempt a new Survival check every hour while Tracking. If you have legendary proficiency in Survival, you can use another exploration activity while Tracking.

If you roll Survival for initiative while tracking your hunted prey, when you start your first turn of the encounter, you can Stride toward your hunted prey as a free action.

**Source:** `= this.source` (`= this.source-type`)
