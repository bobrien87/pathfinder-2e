---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You attempt a saving throw against a harmful magical effect but haven't rolled yet.

Your innate magic protects you. You gain a +1 circumstance bonus to the triggering saving throw. Additionally, if the triggering effect is arcane, if you roll a success, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
