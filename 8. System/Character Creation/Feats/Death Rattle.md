---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Necrologist|Necrologist]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Magical]]"]
prerequisites: "Necrologist Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your horde is raised.

When the time comes for your horde to be returned to its temporary rest, its departure carries those nearby closer to death. Dismiss your raised horde, which draws life energy toward it as it crumbles to the ground and fades away. Each living creature within your horde's space or in a @Template[type:emanation|distance:5] around it must attempt a [[Fortitude]] save saving throw against your spell DC or become [[Drained]] 1 ([[Drained]] 2 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
