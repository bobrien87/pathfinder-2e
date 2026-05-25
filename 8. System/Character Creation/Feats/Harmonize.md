---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Bard]]", "[[Concentrate]]", "[[Manipulate]]", "[[Spellshape]]"]
prerequisites: "maestro muse"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can perform multiple compositions simultaneously, typically by performing in multiple ways at the same time, using special vocal techniques to double your voice, or creating occult magic that replicates your song or speech. If your next action is to cast a composition, it becomes a harmonized composition. Unlike a normal composition, a harmonized composition doesn't end if you cast another composition, and you can cast another composition on the same turn as a harmonized one. Casting another harmonized composition ends any harmonized composition you already have in effect.

**Source:** `= this.source` (`= this.source-type`)
