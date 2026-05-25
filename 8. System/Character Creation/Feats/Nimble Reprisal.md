---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Champion]]"]
prerequisites: "justice cause"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can use [[Retributive Strike]] at greater distance. You can use a ranged weapon to make a ranged Strike instead of a melee Strike for Retributive Strike. The enemy needs to be in range, but not in reach, and it must still be in your champion's aura.

You can also make melee Strikes against enemies a bit farther away. If the enemy that triggered your reaction is outside your reach but is within 5 feet of your reach, as part of your reaction you can Step to put the enemy in your reach before making a melee Retributive Strike.

**Source:** `= this.source` (`= this.source-type`)
