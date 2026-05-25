---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Investigator]]", "[[Prediction]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You spend 10 minutes in contemplation to uncannily predict how events will play out. Choose a particular goal or activity you plan to engage in within 1 week, or an event you expect might happen within 1 week. You analyze whether it's likely to come to pass, learning whether it's highly likely, somewhat likely, somewhat unlikely, or highly unlikely. You also gain a piece of advice suggesting a course of action you or your allies could take that might make the chosen event more or less likely, whichever you prefer.

The GM determines the likeliness of the event and the piece of advice you learn.

**Source:** `= this.source` (`= this.source-type`)
