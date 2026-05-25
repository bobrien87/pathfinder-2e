---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Tanuki]]"]
prerequisites: "Everyday Form"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Nobody respects tanuki, but most everyone respects an esteemed priest, so what better form to take if you want to get by a little easier? When you Change Shape, you can assume the shape of a priest or other religious official from a religion of your choosing. While in your false priest form, you can attempt Deception checks to Recall Knowledge about Religion, and you can cast [[Divine Lance]] and [[Haunting Hymn]] as primal innate cantrips. If you critically fail at a Deception check while in your false priest form, your transformation is broken, returning you to your tanuki form, and you're so embarrassed that you can't resume your False Priest Form until your next daily preparations, after you've taken a night to sleep on it.

**Source:** `= this.source` (`= this.source-type`)
