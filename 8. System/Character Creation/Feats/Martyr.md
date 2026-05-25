---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Cleric]]", "[[Spellshape]]"]
prerequisites: "divine font"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You go to extreme lengths to support your allies, even when it means bringing harm to yourself. If your next action is to cast [[Harm]] or [[Heal]] to restore Hit Points to a single ally, you can channel your own vitality along with the spell. You lose 1d8 Hit Points per rank of the spell, which can't be reduced or mitigated in any way, and your ally regains an equal number of Hit Points.

**Source:** `= this.source` (`= this.source-type`)
