---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Concentrate]]", "[[Primal]]", "[[Talos]]"]
frequency: "once per day"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Duration** 1 minute

You fortify your natural resistances with elemental metal, covering your skin with thick metal. You gain a +2 status bonus to AC and resistance 10 to physical damage (except adamantine), but you take a –10-foot penalty to Speed. If you take fire damage while this ability is active, until the end of your next turn, you deal an additional 2d6 fire damage with all your unarmed melee Strikes.

**Source:** `= this.source` (`= this.source-type`)
