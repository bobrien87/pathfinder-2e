---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Auditory]]", "[[Bard]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "Courageous Advance, Courageous Assault"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You use your performance to orchestrate an onslaught against your enemies. If your next action is to cast the [[Courageous Anthem]] composition cantrip, one ally of your choice who gains a status bonus from the spell can immediately use their reaction to Stride and then make a melee Strike.

**Source:** `= this.source` (`= this.source-type`)
