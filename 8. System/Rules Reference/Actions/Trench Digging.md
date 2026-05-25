---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You're subjected to forced movement

**Effect** You deploy your claw spikes to churn the earth asunder, creating difficult terrain in each square of ground you're moved through.

**Source:** `= this.source` (`= this.source-type`)
