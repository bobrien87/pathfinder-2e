---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Plant]]", "[[Primal]]", "[[Stance]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A haze of pollen floats around you. A creature in your kinetic aura when you enter the stance, or who later enters the aura or ends its turn in the aura, attempts at a [[Fortitude]] save against your class DC. On a failure, it's [[Sickened]] 1 ([[Sickened]] 2 on a critical failure) and [[Dazzled]] until it's no longer sickened. A creature attempts this save no more than once per round and doesn't attempt a new save if already affected.

**Source:** `= this.source` (`= this.source-type`)
