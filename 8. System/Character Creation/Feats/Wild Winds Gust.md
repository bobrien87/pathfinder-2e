---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]", "[[Monk]]"]
prerequisites: "Wild Winds Initiate"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in [[Wild Winds Stance]]

You build air pressure with repeated motions, before releasing an enormous crescent of rushing wind strikes. Make a wind crash Strike against each creature in your choice of a @Template[cone|distance:30] or a @Template[line|distance:60]. These attacks all count toward your multiple attack penalty, but the penalty doesn't increase until after you make all the attacks.

**Source:** `= this.source` (`= this.source-type`)
