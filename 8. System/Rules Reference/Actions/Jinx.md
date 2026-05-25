---
type: action
source-type: "Remaster"
traits: ["[[Curse]]", "[[Occult]]"]
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** You can curse another creature with clumsiness. This curse has a range of 30 feet, and you must be able to see your target. The target gets a [[Will]] save saving throw against your class DC or spell DC, whichever is higher.
- **Success** The target is unaffected and temporarily immune for 24 hours.
- **Failure** The target is [[Clumsy]] 1 for 1 minute.
- **Critical Failure** The target is [[Clumsy]] 2 for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
