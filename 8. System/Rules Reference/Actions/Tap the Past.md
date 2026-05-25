---
type: action
source-type: "Remaster"
traits: ["[[Fortune]]"]
cast: "`pf2:0`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Trigger** You're about to attempt a check to Recall Knowledge

**Effect** You concentrate on the glimpses of a previous life to find a memory of a tome or an applicable lesson from your past. You roll a second time and use the higher result. If you roll a critical failure, you get a failure instead. If you roll a success, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
