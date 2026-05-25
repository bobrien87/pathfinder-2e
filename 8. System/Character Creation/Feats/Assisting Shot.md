---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Fighter]]", "[[Press]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a ranged weapon.

Using your last shot to gauge your accuracy, you can fire off a quick shot to interfere with a foe in combat. Make a Strike with a ranged weapon. If the Strike hits, the next creature other than you to attack the same target before the start of your next turn gains a +1 circumstance bonus to their roll, or a +2 circumstance bonus if your Strike was a critical hit.

> [!danger] Effect: Assisting Shot

**Source:** `= this.source` (`= this.source-type`)
