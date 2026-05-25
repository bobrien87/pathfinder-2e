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

You spend time observing the place or group you wish to infiltrate. Attempt a normal, hard, or very hard DC Perception, Society or Stealth check.
- **Success** You make observations that provide 1 EP.
- **Failure** You learn nothing particularly noteworthy.
- **Critical Failure** You misjudge some aspect of what you observed, gaining 1 EP that results in a critical failure instead of a success when used, even if a PC uses the Edge Point after rolling a failure.

**Source:** `= this.source` (`= this.source-type`)
