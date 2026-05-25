---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Rogue]]"]
prerequisites: "trained in Intimidation"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You menace the target, stoking their fears and drawing their attention. Attempt an [[Intimidation]] check against the Will DC of a target within 30 feet. If you succeed, for 1 minute, that target gains a +2 status bonus to Perception checks against you, but it takes a –2 status penalty to Will saves against fear effects.

> [!danger] Effect: Watch Your Back

**Source:** `= this.source` (`= this.source-type`)
