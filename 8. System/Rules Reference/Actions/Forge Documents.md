---
type: action
source-type: "Remaster"
traits: ["[[Downtime]]", "[[Secret]]"]
cast: "Passive"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You prepare forgeries that might serve as convincing props. Attempt a hard or very hard Society check.
- **Success** You create convincing forgeries and gain 1 EP you can use only when presenting some form of paperwork.
- **Failure** You create unconvincing documents. You gain 1 EP that (unknown to you) grants no benefit when used.
- **Critical Failure** As a failure, but a PC who tries to use the Edge Point gets a critical failure, even if they use the Edge Point after rolling a failure.

**Source:** `= this.source` (`= this.source-type`)
