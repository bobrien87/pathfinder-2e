---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Illusion]]", "[[Tanuki]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know how to run an enterprise that others would never be able to get off the ground—some say it's your savvy acumen or jovial manner, but you know it's because you can cut costs by transforming leaves into money. You can use Deception to [[Earn Income]], and you gain a +1 status bonus to your check if you do so. The illusion doesn't hold long, though! The GM rolls a secret d20; that many hours after concluding your check, the money transforms back, likely inviting consequences depending on how far the bills traveled from you in the time they were transformed.

**Source:** `= this.source` (`= this.source-type`)
