---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Poppet]]"]
prerequisites: "tsukumogami poppet heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You leverage your body's amorphous nature to spook others. Attempt to `act demoralize options=sudden-terror` a creature within 30 feet. Demoralize loses the auditory trait and gains the visual trait, and you don't take a penalty if the creature doesn't understand your language. If you were [[Hidden]] to the creature, you gain a +2 circumstance bonus to your check, and if you succeed, the creature is [[Frightened]] 2 instead of [[Frightened]] 1. All creatures that witnessed you use Sudden Terror are then temporarily immune to your Sudden Terror for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
