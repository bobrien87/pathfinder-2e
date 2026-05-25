---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Mythic]]"]
prerequisites: "Acrobat's Calling"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You feel the call of the sky, or perhaps a desperate urge to test the limits of the earth's hold on you. When you or a creature you're mounted on attempts a [[High Jump]] or [[Long Jump]], you can spend a Mythic Point to allow you or the mount to attempt the check at mythic proficiency; determine the DC using the Long Jump DCs, and increase your maximum distance to double your Speed.

**Source:** `= this.source` (`= this.source-type`)
