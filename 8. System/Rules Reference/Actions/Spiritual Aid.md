---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You fail a Reflex or Will saving throw

**Effect** You reroll the triggering saving throw. You must use the second result, even if it's worse. If you roll a success, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
