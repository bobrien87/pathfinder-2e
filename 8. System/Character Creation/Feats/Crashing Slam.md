---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Fighter]]"]
prerequisites: "Slam Down"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can dash your foe to the ground with a single blow. If the Strike you make with [[Slam Down]] hits, you can automatically get a critical success on your [[Trip]] instead of rolling a check. (Both the Strike and Trip still count toward your multiple attack penalty).

If you used a two-handed melee weapon for the Strike, you can use the weapon's damage die size instead of the regular die size for the damage from a critical Trip.

**Source:** `= this.source` (`= this.source-type`)
