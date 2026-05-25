---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Occult]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You transform your tattoo to a different form of approximately the same size. You can Dismiss this effect.

**Source:** `= this.source` (`= this.source-type`)
