---
type: action
source-type: "Remaster"
cast: "`pf2:0`"
source: "Pathfinder Myth-Speaker Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Trigger** Your [[Dying]] value would reach an amount sufficient to kill you (typically 4)

**Effect** You instead stabilize and increase your [[Doomed]] value by 1.

**Source:** `= this.source` (`= this.source-type`)
