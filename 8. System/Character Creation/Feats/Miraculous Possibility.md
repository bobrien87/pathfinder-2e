---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Cleric]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your deity empowers you to perform minor miracles, allowing you to readily adapt to the fluctuating needs of your duties. Once during your daily preparations, you can use a spell slot to hold sheer divine potential, rather than using it to prepare a spell. You can use this spell slot to cast any spell you know from the divine spell list that's at least 2 ranks lower than the slot you designate. The spell acts in all ways as a spell of 2 ranks lower. You don't have any particular spell prepared in that slot until you cast it.

**Source:** `= this.source` (`= this.source-type`)
