---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Bravado]]", "[[Swashbuckler]]"]
prerequisites: "expert in Intimidation"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your turn begins, and one target within 30 feet failed an attack roll or skill check against you on its last turn.

You capitalize on an opponent's failure with smug attitude and swagger, reminding them of the gap in skill between you and your opponent. You attempt to `act demoralize traits=bravado` the opponent. Regardless of the result, the target becomes temporarily immune for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
