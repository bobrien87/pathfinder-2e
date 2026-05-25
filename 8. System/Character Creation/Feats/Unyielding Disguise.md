---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Reflection]]"]
prerequisites: "ability to cast humanoid form or illusory disguise"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you cast [[Humanoid Form]] or [[Illusory Disguise]] to alter your appearance, the spell's duration is 2 hours. At the end of the duration, you can extend the spell's duration for another hour, but doing so is taxing, making you [[Drained]] 1. You can keep extending it in this way, increasing your drained condition by 1 each time, to a maximum duration of 6 hours.

**Source:** `= this.source` (`= this.source-type`)
