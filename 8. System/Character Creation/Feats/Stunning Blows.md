---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Monk]]"]
prerequisites: "Flurry of Blows"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The focused power of your flurry threatens to overwhelm your opponent. When you target the same creature with two Strikes from your [[Flurry of Blows]], you can try to stun the creature. If either Strike hits and deals damage, the target must succeed at a Fortitude save against your class DC or be [[Stunned]] 1 (or [[Stunned]] 3 on a critical failure). This is an incapacitation effect.

**Source:** `= this.source` (`= this.source-type`)
