---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Cursebound]]", "[[Divine]]", "[[Mental]]", "[[Oracle]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You reveal a glimpse of the impossible conflicts between the divine anathema behind your curse, forcing you to reckon with another's conflicts as well. You and one creature within 30 feet each take @Damage[(3*(floor((@actor.level - 2)/2)))d6[mental]] damage with a [[Will]] save, and the target is [[Stunned]] 1 if it critically fails its save. You get a degree of success one better than you rolled for your saving throw. At 10th level, and every 2 levels thereafter, the damage increases by 3d6.

**Source:** `= this.source` (`= this.source-type`)
