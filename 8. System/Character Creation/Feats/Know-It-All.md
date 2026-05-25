---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Bard]]", "[[Thaumaturge]]"]
prerequisites: "enigma muse"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Bard** When you succeed at a check to Recall Knowledge, you gain additional information or context. When you critically succeed at a check to Recall Knowledge, you get additional information or context or can ask an additional follow-up question (the GM chooses which).

**Thaumaturge** Having heard and scrutinized every rumor or story in the book, you know for a fact that if you've heard something at all, you've probably heard about it at great length. When you succeed or critically succeed at a check to [[Recall Knowledge]], you can ask an additional follow-up question. At the GM's discretion, you might gain even more additional context than normal.

**Source:** `= this.source` (`= this.source-type`)
