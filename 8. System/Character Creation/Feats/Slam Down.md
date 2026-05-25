---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Fighter]]", "[[Flourish]]"]
prerequisites: "trained in Athletics"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You make an attack to knock a foe off balance, then follow up immediately with a sweep to topple them. Make a melee Strike. If it hits and deals damage, you can attempt an Athletics check to `act trip` the creature you hit. If you're wielding a two-handed melee weapon, you can ignore Trip's requirement that you have a hand free. Both attacks count toward your multiple attack penalty, but the penalty doesn't increase until after you've made both of them.

**Source:** `= this.source` (`= this.source-type`)
