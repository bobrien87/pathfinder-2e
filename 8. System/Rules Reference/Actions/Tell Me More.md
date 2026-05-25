---
type: action
source-type: "Remaster"
cast: "`pf2:2`"
source: "Paizo Blog: Foolish Housekeeping and Other Articles"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Target** one creature that shares a language you speak

**Requirements** You're not in combat

**Effect** Just batting your eyes and giving someone a familiar nudge can get them talking, ready to spill the beans about everything and everyone around them. You roll twice on all rolls to influence the target and use the better result.

**Source:** `= this.source` (`= this.source-type`)
