---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Fighter]]", "[[Ranger]]", "[[Rogue]]"]
prerequisites: "Haft Striker Stance"
frequency: "once per PT1M"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Requirements** You are in Haft Striker Stance.

The momentum of each of your attacks feeds into the next blow in the routine, creating a brutal rhythm that enables you to give your target one continuous beatdown. Strike twice, once with your weapon and once with its haft. Each attack counts towards your multiple attack penalty, but do not increase your penalty until you have made both attacks. Then Strike twice again, once with your weapon and once with its haft.

**Source:** `= this.source` (`= this.source-type`)
