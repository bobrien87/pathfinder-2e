---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Druid]]"]
prerequisites: "trained in Intimidation"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Imitating animal threat displays, you make yourself appear larger and more imposing. Attempt an Intimidation check to [[Demoralize]] each enemy within 30 feet. This attempt has the visual trait, loses the auditory trait, and you don't take a penalty if the creature doesn't understand your language. Roll your check only once and compare it to the Will DC of each target. You gain a +2 circumstance bonus to the check against animal, fungus, and plant creatures and take a –2 circumstance penalty against other creatures. Each target is then temporarily immune for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
