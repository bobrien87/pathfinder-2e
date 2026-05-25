---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Surki]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Within all surkis is the capacity to be whatever they need to be, and you can tap into that capacity even now. When you sleep, you can choose to enter a pupa state. You sleep so deeply in your pupa that you can't be woken up by loud noises around you, and you lose the benefits of one of your surki heritages overnight. When you emerge and make your daily preparations, you can select a different surki heritage to replace it. If you had one or more evolutions for that heritage, you can choose a different evolution for your new heritage.

**Source:** `= this.source` (`= this.source-type`)
