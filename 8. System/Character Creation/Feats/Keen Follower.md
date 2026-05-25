---
type: feat
source-type: "Remaster"
level: "3"
traits: ["[[General]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your keen observation of your allies has made you better at following their lead. When using the Follow the Expert activity in exploration mode, you gain a +3 circumstance bonus if the ally you are following is an expert and a +4 circumstance bonus if your ally is a master.

You can share your observations with others to help further coordinate the group. If the ally you are following has Quiet Allies or another skill feat that allows the group to roll a single skill check for an exploration activity and use the lowest modifier, they can instead use your modifier, even if it's not the lowest.

**Source:** `= this.source` (`= this.source-type`)
