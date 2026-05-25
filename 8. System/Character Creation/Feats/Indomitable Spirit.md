---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Concentrate]]", "[[Reincarnated]]"]
frequency: "once per day"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Your soul has accumulated countless particles of quintessence over myriad deaths and rebirths, and for one moment, this raw material from the Great Beyond envelops you and your comrades. Until the end of your next turn, you and any allies adjacent to you get a +4 circumstance bonus to AC and are [[Quickened]]. The additional action can be used only to Strike or Stride.

> [!danger] Effect: Indomitable Spirit

**Source:** `= this.source` (`= this.source-type`)
