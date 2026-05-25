---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:1`"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are aboard the vehicle and adjacent to its controls.

You grab the reins, the wheel, or some other mechanism to control the vehicle. Attempt a piloting check; on a success, you become the vehicle's pilot, or regain control of the vehicle if it was uncontrolled. Some vehicles have complicated controls that cause this action to become a multi-action activity.

**Source:** `= this.source` (`= this.source-type`)
