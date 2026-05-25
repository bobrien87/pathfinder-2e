---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:1`"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are piloting a vehicle.

You pilot your vehicle to move. Decide how many actions you intend to spend before you begin Driving. The effects depend on the number of actions you spend. You can't Drive through spaces occupied by creatures, even if they are allies.

`pf2:1` Attempt a piloting check. On a success, the vehicle moves up to its Speed and can turn normally. On a failure, the vehicle moves its Speed in a straight line. On a critical failure, the vehicle moves its Speed in a straight line and becomes uncontrolled

`pf2:2` (reckless) The vehicle moves up to twice its Speed in a straight line at the vehicle's current heading.

`pf2:3` (reckless) You take a –5 penalty on your piloting check to maintain control of the vehicle. The vehicle moves up to three times its Speed in a straight line at the vehicle's current heading.

**Source:** `= this.source` (`= this.source-type`)
