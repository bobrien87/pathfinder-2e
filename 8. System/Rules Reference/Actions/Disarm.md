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

You try to knock an item out of a creature's grasp. Attempt an Athletics check against the target's Reflex DC.
- **Critical Success** You knock the item out of the target's grasp. It falls to the ground in the target's space.
- **Success** You weaken your target's grasp on the item. Further attempts to Disarm the target of that item gain a +2 circumstance bonus, and the target takes a –2 circumstance penalty to attacks with the item or other checks requiring a firm grasp on the item. The creature can end the effect by Interacting to change its grip on the item; otherwise, it lasts as long as the creature holds the item.

> [!danger] Effect: Disarm (Success)
- **Critical Failure** You lose your balance and become [[Off Guard]] until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
