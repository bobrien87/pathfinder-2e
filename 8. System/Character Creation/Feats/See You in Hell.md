---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Reincarnated]]"]
frequency: "once per day"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You're reduced to 0 Hit Points by a creature but not immediately killed.

You aren't sure if you'll be reincarnated again, so you might as well take this foe with you. A blast of spiritual energy lashes out from the depths of your soul, targeting the creature who attacked you. The creature takes spirit damage equal to the amount that reduced you to 0 Hit Points ([[Will]] save with a DC equal to your class DC or spell DC, whichever is higher).

**Source:** `= this.source` (`= this.source-type`)
