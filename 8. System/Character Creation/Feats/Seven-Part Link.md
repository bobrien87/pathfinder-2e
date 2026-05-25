---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Thaumaturge]]"]
prerequisites: "Paired Link"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Many traditions hold the number seven as significant. By exchanging pieces of a seven-part set of esoterica, you create a magical web by which your allies can affect each other at a distance. When you use [[Paired Link]] during your daily preparations, you can exchange linking esoterica with up to six willing allies, keeping one piece for yourself. In addition to the normal effects of Paired Link, if a linked ally casts a spell with a range of touch, they can target linked allies within 30 feet with that spell.

**Source:** `= this.source` (`= this.source-type`)
