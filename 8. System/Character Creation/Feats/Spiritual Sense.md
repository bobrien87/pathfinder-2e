---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Divine]]", "[[Oracle]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a vague connection to the Ethereal Plane that enables you to notice spirits. While you're exploring but not Searching, the GM rolls a secret check for you to find haunts that usually require Searching, as well as spirits, creatures on the Ethereal Plane, and beings made entirely of spiritual essence such as celestials, fiends, and monitors.

You can also potentially notice ethereal creatures and spirits inside solid objects, provided they are within 30 feet of you. This applies while Searching, while Seeking, and on the automatic secret check you gain while exploring even if you aren't Searching. You can still notice spirits only on a successful check, and you can't see them if they're more than 5 feet inside an object. When you notice a creature with this sense, you also learn its location, making it [[Hidden]] to you if it had been [[Undetected]].

**Source:** `= this.source` (`= this.source-type`)
