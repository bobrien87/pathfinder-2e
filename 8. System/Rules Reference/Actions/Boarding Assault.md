---
type: action
source-type: "Remaster"
traits: ["[[Flourish]]"]
cast: "`pf2:2`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Either Stride twice or attempt an [[Acrobatics]] check (DC determined by the GM, but usually DC 20) to swing up to twice your Speed on a rope or similar object, then Strike.

If you boarded or disembarked from a boat or similar vehicle during this movement, the Strike deals one additional weapon damage die.

**Source:** `= this.source` (`= this.source-type`)
