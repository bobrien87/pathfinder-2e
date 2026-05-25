---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Barbarian]]", "[[Druid]]"]
prerequisites: "animal instinct or untamed order"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action dealt piercing or slashing damage using an unarmed Strike granted by a morph or polymorph effect.

You've learned to debilitate your enemies in the same way a hunter tears at their prey. Make an unarmed Strike against the same target. If the Strike hits and deals piercing or slashing damage, the target takes an additional 1d6 persistent bleed damage. If you're at least 12th level, increase this to 2d6 persistent bleed damage.

**Source:** `= this.source` (`= this.source-type`)
