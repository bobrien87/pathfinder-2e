---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Ranger]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You quickly assess your prey and apply what you know. As part of the action used to Hunt your Prey, you can attempt a check to Recall Knowledge about your prey. When you critically succeed at identifying your hunted prey with [[Recall Knowledge]], you note a weakness in the creature's defenses in addition to any other benefits. You gain a +1 circumstance bonus to your next attack roll against that prey, and any ally you tell gains the same benefit. You can give bonuses from Monster Hunter only once per day against a particular creature.

> [!danger] Effect: Monster Hunter

**Source:** `= this.source` (`= this.source-type`)
