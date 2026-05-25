---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Cursebound]]", "[[Oracle]]", "[[Prediction]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You open your senses to numerous visions of the immediate future. The visions grant you subtle details of your immediate surroundings within 30 feet. Within this range, you don't need to succeed at a flat check to target a [[Concealed]] creature, you're not [[Off Guard]] to creatures that are [[Hidden]] from you (unless you're off-guard to them for reasons other than the hidden condition), and you need only a successful DC 5 flat check to target a hidden creature. Beyond 30 feet, the visions become overwhelmed with too many possible futures, making all of your senses imprecise beyond this range. The visions persist for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
