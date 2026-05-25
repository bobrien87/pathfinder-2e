---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dhampir]]", "[[Lineage]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You descend from one of the truly ancient vampires, a nosferatu cursed to eternal life but not eternal youth. People call you straveika, or ancient-born. The vestiges of your forebear's powers of domination have left you with an understanding of how a creature's intentions change its behaviors. You gain a +1 circumstance bonus to Perception checks to [[Sense Motive]] and Perception DCs against attempts to [[Lie]] to you.

**Source:** `= this.source` (`= this.source-type`)
