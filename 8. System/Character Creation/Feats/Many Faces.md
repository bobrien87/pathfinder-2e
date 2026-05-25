---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Tanuki]]"]
prerequisites: "Everyday Form"
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** three times per day

Putting on a new face offers a great way to get a fresh perspective on life. When you Change Shape into your everyday form, you gain the effects of a 3rd-rank [[Illusory Disguise]] for 1 hour or until you shift back, whichever comes first, except it's a polymorph effect rather than an illusion. However, your transformations can be broken with a good shock; if you gain the [[Frightened]] or [[Stunned]] condition while transformed, your transformation ends, returning you to your tanuki form, and your confidence is so shaken you can't attempt to resume that specific disguise again until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
