---
type: action
source-type: "Remaster"
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Make a ranged Strike with your ikon. If the Strike hits, the target must succeed at a [[Reflex]] save against your class DC or the arrow transforms into a multitude of ethereal snakes that coil around the target, [[Immobilizing]] it until it succeeds at an [[Escape]] attempt against your class DC.

**Source:** `= this.source` (`= this.source-type`)
