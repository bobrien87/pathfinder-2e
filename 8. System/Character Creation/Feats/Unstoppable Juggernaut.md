---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Barbarian]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have become a brutal, unstoppable force of nature, able to shrug off mortal wounds with ease. You gain resistance equal to 3 + your Constitution modifier to all damage, and your resistance from raging increases to 8 + your Constitution modifier.

In addition, if you are reduced to 0 Hit Points while raging, you can end your rage as a reaction to stay at 1 Hit Point. If you do, you become [[Wounded]] 2 (or increase your wounded condition by 2 if you are already wounded).

**Source:** `= this.source` (`= this.source-type`)
