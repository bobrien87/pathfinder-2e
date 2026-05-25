---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Kineticist]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can sustain yourself on a single drop of elemental dew or the slightest spark from the Plane of Fire. You gain a +2 status bonus to saving throws against poisons, sleep, and effects that would make you [[Paralyzed]]. You don't need to breathe, eat, or sleep, though you must still take a full night's rest every 24 hours to be able to make your daily preparations. During this time, you remain awake and alert, but you must spend the time meditating or attuning to your kinetic gate rather than engaging in other complex activities. Each kineticist attunes in their own individual way.

**Source:** `= this.source` (`= this.source-type`)
