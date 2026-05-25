---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You steady your body and observe the events of the battlefield to maximize the range of your next shot. You reduce the penalty for firing into your weapon's second range increment from –2 to 0 for the next ranged attack you make this turn. You can use this action a second time in the same turn to reduce the penalty from firing into your weapon's third range increment from –4 to 0 for the next ranged attack you make this turn.

**Source:** `= this.source` (`= this.source-type`)
