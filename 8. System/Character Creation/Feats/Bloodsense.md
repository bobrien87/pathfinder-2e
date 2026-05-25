---
type: feat
source-type: "Remaster"
level: "7"
prerequisites: "master in Perception"
source: "Pathfinder #213: Thirst for Blood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're extraordinarily sensitive to the presence of blood. You gain bloodsense as an imprecise sense with a range of 15 feet. This allows you to sense the presence of creatures, living or dead, that have blood (this includes most creatures that aren't immune to bleed). You're similarly able to detect the presence of fresh blood in volumes of one pint or more, so long as it's no more than 24 hours old.

**Source:** `= this.source` (`= this.source-type`)
