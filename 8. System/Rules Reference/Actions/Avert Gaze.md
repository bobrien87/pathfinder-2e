---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You avert your gaze from danger, such as a medusa's gaze. You gain a +2 circumstance bonus to saves against visual abilities that require you to look at a creature or object, such as a medusa's petrifying gaze. Your gaze remains averted until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
