---
type: action
source-type: "Remaster"
traits: ["[[Fortune]]", "[[Linguistic]]"]
cast: "`pf2:r`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** An ally you reviewed stratagems with is about to attempt an attack roll or skill check

**Effect** The ally rolls the triggering check twice and takes the better of the two results. That ally then becomes temporarily immune to your Inspired Stratagem until your next daily preparations.

> [!danger] Effect: Inspired Stratagem

**Source:** `= this.source` (`= this.source-type`)
