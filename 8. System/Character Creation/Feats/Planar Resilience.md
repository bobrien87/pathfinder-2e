---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Jotunborn]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your body has adapted to the variety of harsh climes that you encounter in your travels. You treat temperature-based environmental effects as if they were one step less extreme (incredible cold or heat becomes extreme, extreme cold or heat becomes severe, and so on).

Additionally, the planar energies that move through you allow you to further adapt your body with some concentration and effort. During your daily preparations, choose either cold or fire. You gain resistance to that damage equal to half your level (minimum 1).

**Source:** `= this.source` (`= this.source-type`)
