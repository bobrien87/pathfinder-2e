---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Champion]]"]
prerequisites: "Loyal Warhorse"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Under your care, your mount has realized its innate potential. The mount you gained with Faithful Steed is now a nimble or savage animal companion.

Your animal companion has greater independence. During an encounter, even if you don't use the Command an Animal action, your animal companion can still use 1 action that round on your turn to Stride or Strike. It can do this at any point during your turn, as long as you aren't currently taking an action. If it does, that's all the actions it gets that round—you can't Command it later.

**Source:** `= this.source` (`= this.source-type`)
