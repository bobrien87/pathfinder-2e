---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Oracle]]"]
prerequisites: "Greater Revelation"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The truest depths of your divine mystery are fathomless and contradictory, granting you changing powers that even you can barely begin to fathom. Each day during your daily preparations, choose one basic or advanced domain spell from any domain from *Player Core*, one of the domains granted by your mystery, another domain to which you have access, or any initial or advanced revelation spell from another mystery. You gain that spell as a revelation spell until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
