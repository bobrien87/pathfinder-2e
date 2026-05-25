---
type: action
source-type: "Remaster"
traits: ["[[Investigator]]"]
cast: "`pf2:0`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

You observe and assess your surroundings with great speed. You [[Recall Knowledge]], [[Seek]], or [[Sense Motive]].

**Source:** `= this.source` (`= this.source-type`)
