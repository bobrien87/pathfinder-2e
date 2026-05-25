---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You pick up a small, unattended object and try not to be noticed. Roll a single Thievery check against the Perception DCs of all creatures who are currently observing you. You can typically only Palm Objects of negligible Bulk, though the GM might determine otherwise depending on the situation.
- **Success** The creature doesn't notice you Palming the Object.
- **Failure** The creature notices you Palming the Object.

**Source:** `= this.source` (`= this.source-type`)
