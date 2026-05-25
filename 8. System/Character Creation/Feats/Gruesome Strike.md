---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Champion]]"]
prerequisites: "champion's reaction that grants extra damage with your Strikes (including the desecration, iniquity, and obedience causes)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your Strikes currently deal extra damage from your champion's reaction.

Make a Strike against the creature that triggered your champion's reaction. If you hit, double the extra damage the target takes from your reaction, and the target must succeed at a [[Fortitude]] save against your class DC or be [[Drained]] 1. Regardless of the result, the creature is temporarily immune to your Gruesome Strike for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
