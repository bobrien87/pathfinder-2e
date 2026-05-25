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

**Requirements** You have at least one hand free. Your target can't be more than one size larger than you.

You try to knock a creature to the ground. Attempt an Athletics check against the target's Reflex DC.
- **Critical Success** The target falls, lands [[Prone]], and takes 1d6 bludgeoning damage.
- **Success** The target falls and lands prone.
- **Critical Failure** You lose your balance, fall, and land prone.

**Source:** `= this.source` (`= this.source-type`)
