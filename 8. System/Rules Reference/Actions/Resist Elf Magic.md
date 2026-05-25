---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You attempt a saving throw against a magical effect but haven't rolled yet

Your ancestral resistance to magic protects you. You gain a +1 circumstance bonus to the triggering saving throw. If the triggering effect is arcane, you gain a +2 circumstance bonus instead.

**Source:** `= this.source` (`= this.source-type`)
