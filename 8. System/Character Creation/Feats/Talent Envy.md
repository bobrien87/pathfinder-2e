---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Performance, Virtuosic Performer"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You give off a bedazzling glow with every performance, sparking feelings of severe envy and inadequacy in those who compare their talent to yours. Once per minute when you succeed at a check using the type of performance that you chose with Virtuosic Performer, you can attempt to [[Demoralize]] an onlooker of your choice within 60 feet as a free action. If you critically succeeded on your Performance check, improve the degree of success for your Demoralize check by one step.

**Source:** `= this.source` (`= this.source-type`)
