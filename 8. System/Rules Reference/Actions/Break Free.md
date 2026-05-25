---
type: action
source-type: "Remaster"
traits: ["[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You can attempt to [[Escape]] with a +2 status bonus on your check, then Stride up to twice your Speed in a straight line, and finally make a melee Strike. If you don't need to Escape or you can't move or choose not to, you still take the other actions listed.

**Source:** `= this.source` (`= this.source-type`)
