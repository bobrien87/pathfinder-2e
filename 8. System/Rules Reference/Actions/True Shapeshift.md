---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're under the effects of [[Untamed Form]]

**Effect** You change into any other shape on your *untamed form* list. If the duration of that shape is different from the one you were previously in, use the shorter duration to determine your duration remaining.

**Source:** `= this.source` (`= this.source-type`)
