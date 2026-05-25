---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You fall.

**Requirements** You have a fly Speed.

You attempt an Acrobatics check or Reflex save to slow your fall. The DC is typically 15, but it might be higher due to air turbulence or other circumstances.
- **Success** You take no damage from the fall.

**Source:** `= this.source` (`= this.source-type`)
