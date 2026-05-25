---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Sprite]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you sleep, you turn into an inanimate object a little smaller than a human's thumb—easily overlooked and carried. Being in your Charmed Sleep counts as setting up a disguise for the [[Impersonate]] use of Deception (except that you Impersonate an object instead of a creature), it gives you a +4 status bonus to Deception checks to prevent others from seeing through your disguise, and you add your level even if you're untrained. While in your Charmed Sleep, you can be picked up and carried as easily as any small object. This effect immediately ends as soon as you wake.

**Source:** `= this.source` (`= this.source-type`)
