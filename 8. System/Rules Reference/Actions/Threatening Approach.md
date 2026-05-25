---
type: action
source-type: "Remaster"
cast: "`pf2:2`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You Stride to be adjacent to a foe and `act demoralize` that foe. If you succeed, the foe is [[Frightened]] 2 instead of frightened 1.

**Source:** `= this.source` (`= this.source-type`)
