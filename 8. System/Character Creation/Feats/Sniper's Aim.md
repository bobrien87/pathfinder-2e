---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Gunslinger]]"]
prerequisites: "Way of the Sniper"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You take an extra moment to carefully sync your aim and breathing, then fire a shot with great accuracy. Make a ranged weapon Strike. You gain a +2 circumstance bonus to this Strike's attack roll and ignore the target's concealment. If you're using a kickback firearm, you don't take the normal circumstance penalty on this Strike for not having the required Strength modifier or firing without using a stabilizer.

**Source:** `= this.source` (`= this.source-type`)
