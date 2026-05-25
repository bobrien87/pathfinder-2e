---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Champion]]"]
prerequisites: "Mercy"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your faith enhances your ability to remove conditions. Add the following options to the list of conditions you can counteract for any type of mercy you can grant.

- **Mercy of the Body** [[Drained]], [[Slowed]]; if you're 16th level, add [[Stunned]]

- **Mercy of Grace** [[Immobilized]], [[Restrained]], [[Slowed]]; if you're 12th level, add [[Petrified]]; if you're 16th level, add [[Stunned]]

- **Mercy of the Mind** [[Confused]], [[Controlled]], [[Slowed]]; if you're 16th level, add [[Doomed]] and [[Stunned]].

**Source:** `= this.source` (`= this.source-type`)
