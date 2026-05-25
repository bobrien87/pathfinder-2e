---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Cold]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Gleaming flakes of chilling snow fall in a @Template[burst|distance:10] within 60 feet. Each creature in the area takes @Damage[(floor((@actor.level -1)/2)+2)d4[cold]|options:area-damage] damage with a [[Reflex]] save against your class DC. The ground in the area is covered in a snow drift, which is difficult terrain. Each square of the drift lasts until it melts, either naturally or until fire damage is dealt in that square.

**Level (+2)** The damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
