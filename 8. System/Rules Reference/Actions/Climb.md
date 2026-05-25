---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You have both hands free

You attempt an Athletics check to move a maximum distance of 5 feet up, down, or across an incline. You're [[Off Guard]] while climbing unless you have a climb Speed. The GM determines the DC based on the nature of the incline and environmental circumstances; you might get an automatic critical success on an incline that's trivial to climb. If your land Speed is 40 feet or higher, increase the maximum distance by 5 feet for every 20 feet of Speed above 20 feet.
- **Critical Success** You move along the incline, increasing the maximum distance by 5 feet.
- **Success** You move along the incline.
- **Critical Failure** You fall. If you began the climb on stable ground, you fall and land [[Prone]].

Sample Climb Tasks- **Untrained** ladder, steep slope, low-branched tree
- **Trained** rigging, rope, typical tree
- **Expert** wall with small handholds and footholds
- **Master** ceiling with handholds and footholds, rock wall
- **Legendary** smooth surface

**Source:** `= this.source` (`= this.source-type`)
