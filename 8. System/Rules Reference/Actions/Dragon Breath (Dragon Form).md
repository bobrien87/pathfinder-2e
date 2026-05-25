---
type: action
source-type: "Remaster"
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You exhale deadly magical energy in an area, dealing @Damage[10d6[untyped]|options:area-damage] damage to each creature in the area with a basic save against your spell DC. The shape, damage type, and save type match that of your chosen dragon's breath. If the chosen dragon's breath can deal more than one type of damage, choose one when you cast *dragon form*. The shape is a @Template[type:cone|distance:30] or a @Template[type:line|distance:100]. Once activated, Dragon Breath can't be used again for 1d4 rounds. Dragon Breath has the tradition trait matching the type of dragon and the damage trait matching the type of damage it deals, if applicable.

**Source:** `= this.source` (`= this.source-type`)
