---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're adjacent to a willing ally

**Effect** You move the adjacent willing ally 5 feet in any direction and can Step into the space the ally vacated.

**Source:** `= this.source` (`= this.source-type`)
