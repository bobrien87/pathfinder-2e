---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You attempt a saving throw against a magical effect, but you haven't rolled yet

Your ancestors' innate resistance to magic surges before slowly ebbing down. You gain a +1 circumstance bonus to saving throws on the triggering save and other saves against magical effects until the end of this turn.

**Source:** `= this.source` (`= this.source-type`)
