---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Jotunborn]]"]
prerequisites: "warrior jotunborn heritage"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You use the momentum of your massive fists to launch yourself through the air. Strike with your fist unarmed attack and then attempt a [[High Jump]] or [[Long Jump]]; you count as having a running start and do not need to Stride before this activity to avoid failure. You can attempt this Strike against an unattended object or unoccupied flat surface, and you gain a +2 circumstance bonus to your Athletics check to High Jump or Long Jump when you do so.

*PFS Note:* For the purposes of this feat, the AC of an unoccupied surface is 10.

**Source:** `= this.source` (`= this.source-type`)
