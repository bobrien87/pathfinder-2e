---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Gnome]]"]
prerequisites: "at least one arcane or occult innate spell gained from a gnome heritage or gnome ancestry feat"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've learned a few magical techniques for getting yourself both into and out of trouble unnoticed. You gain [[Disguise Magic]] and [[Silence]] as 2nd-rank arcane or occult innate spells. The tradition of these spells must match the tradition you use for your gnome ancestry options. You can cast each spell once per day and can target only yourself.

**Source:** `= this.source` (`= this.source-type`)
