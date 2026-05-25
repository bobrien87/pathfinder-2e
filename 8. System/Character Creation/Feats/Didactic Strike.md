---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Investigator]]"]
prerequisites: "Shared Stratagem"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you find a glaring weakness, you can set your allies up to annihilate your foe.

When you use [[Shared Stratagem]], you can designate up to 10 allies instead of just one. The foe is [[Off Guard]] against the first attack from each designated ally before your next turn, and each ally's first attack deals an extra 2d6 precision damage to the target if it hits.

> [!danger] Effect: Didactic Strike

**Source:** `= this.source` (`= this.source-type`)
