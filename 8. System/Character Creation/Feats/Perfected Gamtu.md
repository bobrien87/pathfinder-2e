---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Goblin]]", "[[Occult]]"]
prerequisites: "Glorious Gamtu"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your hat embodies the illusory grandeur of a master dokkaebi. Your gamtu now grants its wearer a +1 item bonus to Stealth checks when worn, and its Hat Trick activation can grant your choice of 2nd-rank [[Invisibility]] or 6th-rank *invisibility*.

In addition, the gamtu can be removed while Hat Trick is activated. Doing so removes the effects of *invisibility* from the original wearer, but the spell doesn't end. Instead, the effect continues to elapse; if another creature puts the gamtu on, they're immediately affected by *invisibility*, which lasts for the remaining duration of Hat Trick.

**Source:** `= this.source` (`= this.source-type`)
