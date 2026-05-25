---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Detection]]", "[[Divine]]", "[[Thaumaturge]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your cunning knowledge grants you the ability to notice the emotional echo of a soul that passed on, leaving a haunt in its wake. Even when you aren't Searching while in exploration mode, the GM rolls a secret check for you to notice haunts that usually require you to be Searching.

You can disable haunts that require master proficiency in a skill as long as you're at least trained in the skill. If you have master proficiency in the skill, you can disable haunts that require a proficiency rank of legendary instead.

**Source:** `= this.source` (`= this.source-type`)
