---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Sorcerer]]", "[[Spellshape]]"]
prerequisites: "dispel magic in your spell repertoire"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You weave dispelling energy into a spell. If your next action is to cast a single-target spell against an enemy, and you either hit the enemy with the spell attack roll or the enemy fails its saving throw, you can cast [[Dispel Magic]] on the enemy as a free action, expending a spell slot as normal and targeting one spell effect affecting the enemy.

**Source:** `= this.source` (`= this.source-type`)
