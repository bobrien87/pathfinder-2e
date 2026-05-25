---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Swashbuckler]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding one or more one-handed weapons

You use one-handed weapons to parry with style. You gain a +1 circumstance bonus to AC until the start of your next turn, or a +2 circumstance bonus if you have a free hand or are wielding a weapon with the parry trait. You lose this circumstance bonus if you no longer meet this feat's requirement. If a creature misses you with a Strike while you have this bonus, you gain panache until the end of your next turn.

> [!danger] Effect: Panache (Temporary)

**Source:** `= this.source` (`= this.source-type`)
