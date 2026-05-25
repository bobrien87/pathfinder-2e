---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "trained in Medicine"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You understand the principles of forensic medicine, making you better at examining a body to determine the cause of death or injury.

You can perform a forensic examination on a body, as described under [[Recall Knowledge]] in the Medicine skill, in half the normal amount of time it would take (to a minimum of 5 minutes).

If you succeed at your check, you can attempt an immediate check to Recall Knowledge to follow up on something you found, with a +2 circumstance bonus.

This check is usually related to the cause of injury or death, such as a Crafting check to identify a poison or weapon that was used or an additional Medicine check to identify a specific disease. If you prefer, you can instead attempt to Recall Knowledge about the type of creature whose body you were examining, using the appropriate skill and gaining the same circumstance bonus.

The circumstance bonus increases to +3 if you have master proficiency in Medicine and +4 if you have legendary proficiency.

**Source:** `= this.source` (`= this.source-type`)
