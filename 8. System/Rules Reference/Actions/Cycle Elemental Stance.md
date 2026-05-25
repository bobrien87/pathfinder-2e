---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're in one of the elemental stances

**Effect** Stride or Step, and then enter a different elemental stance from the one you're currently in.

**Source:** `= this.source` (`= this.source-type`)
