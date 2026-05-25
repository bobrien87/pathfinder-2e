---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Bard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature or hazard would deal sonic damage to you.

You can manipulate the acoustics around you to deflect sonic damage back at its source. Attempt a Performance check against the Performance check{Will DC} of the creature or Performance check{Fortitude DC} of a hazard. If the damage came from a spell, use the creature's spell DC if it's lower.
- **Critical Success** You reduce the triggering damage by an amount up to four times your level. The creature takes sonic damage equal to the amount of damage you reduced in this way.
- **Success** As critical success, but you reduce the triggering damage by an amount up to twice your level.

**Source:** `= this.source` (`= this.source-type`)
