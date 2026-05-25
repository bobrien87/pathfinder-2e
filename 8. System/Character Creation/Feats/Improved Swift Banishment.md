---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Cleric]]"]
prerequisites: "Swift Banishment"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You easily banish creatures with your weapon. You can use [[Swift Banishment]] as long as you have a spell slot of 5th rank or higher remaining, even if you don't have [[Banishment]] prepared. You must sacrifice a prepared spell of 5th rank or higher, and the *banishment* effect you create is heightened to the rank of that spell. The target takes a –2 circumstance penalty to its save as though you'd paid the extra cost for *banishment*.

**Source:** `= this.source` (`= this.source-type`)
