---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Aftermath]]", "[[Primal]]", "[[Water]]"]
prerequisites: "You've been brought to 0 Hit Points by an enemy that has the water trait or an enemy's ability that has the water trait"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your body looks like it's made of flowing water, clear and pristine, providing a natural grace to all your movements. You gain a swim Speed equal to your land Speed. If you already had a swim Speed, it's increased by 10 feet. You gain the [[Water Transfer]] activity, which enables you to teleport through a body of water.

**Source:** `= this.source` (`= this.source-type`)
