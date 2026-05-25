---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Inventor]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You would attempt the flat check for an unstable action, but you haven't rolled the flat check yet.

You've built triple redundancies into your innovation and added all sorts of buffers to protect it from the harm of your unstable experiments. You automatically succeed at the triggering flat check.

You can't rely on your Unstable Redundancies again until you spend 10 minutes setting them back up. If you spend 10 minutes retuning your innovation so you can use unstable actions again, you can set up your Unstable Redundancies during the same time.

**Source:** `= this.source` (`= this.source-type`)
