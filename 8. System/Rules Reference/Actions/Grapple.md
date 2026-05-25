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

**Requirements** You have at least one free hand and your target is no more than one size larger than you.

You attempt to grab a creature or object with your free hand. Attempt an Athletics check against the target's Fortitude DC. You can grapple a target you already have [[Grabbed]] or [[Restrained]] without having a hand free.
- **Critical Success** Your target is restrained until the end of your next turn unless you move or your target Escapes.
- **Success** Your target is grabbed until the end of your next turn unless you move or your target Escapes.
- **Failure** You fail to grab your target. If you already had the target grabbed or restrained using a Grapple, those conditions on the target end.
- **Critical Failure** If you already had the target grabbed or restrained, it breaks free. Your target can either grab you, as if it succeeded at using the Grapple action against you, or force you to fall and land [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
