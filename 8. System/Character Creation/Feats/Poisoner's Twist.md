---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Poisoner|Poisoner]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Poisoner Dedication, trained in Medicine"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was a successful melee Strike that dealt damage against a target afflicted by a poison, and you know which poison.

Poisons attack specific parts of the body—one venom might target the lungs, another the circulatory system, while another deteriorates the nerves. You know how to take advantage of such weaknesses. You deal 1d6 untyped damage of the required Strike's damage type and 1d6 poison damage to the target. If you're at least 18th level, you deal 2d6 untyped damage of each type.

**Source:** `= this.source` (`= this.source-type`)
