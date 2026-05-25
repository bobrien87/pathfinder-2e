---
type: action
source-type: "Remaster"
traits: ["[[Attack]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You have at least one hand free. The target can't be more than one size larger than you.

You push a creature away from you. Attempt an Athletics check against your target's Fortitude DC.
- **Critical Success** You push your target up to 10 feet away from you. You can Stride after it, but you must move the same distance and in the same direction.
- **Success** You push your target back 5 feet. You can Stride after it, but you must move the same distance and in the same direction.
- **Critical Failure** You lose your balance, fall, and land [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
