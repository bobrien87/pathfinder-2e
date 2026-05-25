---
type: action
source-type: "Remaster"
traits: ["[[Infusion]]"]
cast: "`pf2:1`"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

If your next action is an impulse, it gains the nonlethal trait. If it has an area, you can exclude creatures you've designated with Safe Elements from its effects.

**Source:** `= this.source` (`= this.source-type`)
