---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Warfare Lore"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are constantly drawing up plans and battle scenarios, assembling strategies and gathered intelligence for later use. When you scout an enemy's position or receive a detailed report from an ally who scouted the enemy's position, if you have a clear indication of the number, position, and identities of your potential foes, you can spend 1 minute to come up with a battle plan that takes such potential factors into account and reduces the role luck plays in the equation.

Roll a Warfare Lore check. As long as the information was accurate and remains accurate when you roll initiative against those enemies, you can use the Warfare Lore result you previously rolled for your initiative roll; if you do, this is a fortune effect.

> [!danger] Effect: Battle Planner

**Source:** `= this.source` (`= this.source-type`)
