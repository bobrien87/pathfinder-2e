---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Fighter]]", "[[Guardian]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Fighter** With a sixth sense for the flow of combat, you can quickly react to any situation as required. At the start of each enemy's turn, you gain a reaction you can use only during that turn for any reaction from a fighter feat or class feature.

**Guardian** With a sixth sense for the flow of combat, you can quickly react to any situation as required. At the start of each enemy's turn, you gain a reaction you can use only during that turn for any reaction from a guardian feat or class feature.

**Source:** `= this.source` (`= this.source-type`)
