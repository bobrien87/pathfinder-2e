---
type: action
source-type: "Remaster"
traits: ["[[Fortune]]"]
cast: "`pf2:r`"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Trigger** You fail to [[Lie]] to a creature in public

**Effect** As your target sees through your lie, you spin your falsehood in a way that utilizes the crowd's reaction to bolster believability. Re-roll your Deception check to Lie with a +2 status bonus and use this check's result as the actual result to Lie.

**Source:** `= this.source` (`= this.source-type`)
