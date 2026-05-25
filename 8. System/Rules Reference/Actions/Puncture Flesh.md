---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your last action was to deal piercing damage to an enemy within your reach

**Effect** Attempt an Athletics check to `act grapple` the same enemy. The weapon that dealt the triggering damage gains the grapple trait for this check. On a success, the target also takes 1d8 persistent,piercing damage (or 2d8 persistent,piercing damage on a critical success). When the target is no longer [[Grabbed]] or [[Restrained]] by you, the persistent damage ends.

**Source:** `= this.source` (`= this.source-type`)
