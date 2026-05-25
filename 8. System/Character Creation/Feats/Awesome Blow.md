---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Barbarian]]", "[[Concentrate]]", "[[Rage]]"]
prerequisites: "Knockback"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your attacks are so powerful, they can flatten your opponents. When you use [[Knockback]], you can attempt an [[Athletics]] check against your target's Fortitude DC.
- **Critical Success** You gain the critical success effect of a [[Shove]], then the critical success effect of a [[Trip]] against the target.
- **Success** You gain the success effect of a Shove, then the success effect of a Trip against the target.
- **Failure** You gain the normal effect of Knockback.

**Source:** `= this.source` (`= this.source-type`)
