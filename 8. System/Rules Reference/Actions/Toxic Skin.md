---
type: action
source-type: "Remaster"
traits: ["[[Poison]]", "[[Tripkee]]"]
cast: "`pf2:r`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Trigger** A creature touches you, such as by [[Grappling]] you, successfully hitting you with an unarmed attack, or using a touch-range spell against you

**Effect** You exude a deadly toxin. The triggering creature takes @Damage[(ceil(@actor.level/2))d4[poison]] damage ([[Fortitude]] save using your class DC or spell DC, whichever is higher). At 3rd level and every 2 levels thereafter, the damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
