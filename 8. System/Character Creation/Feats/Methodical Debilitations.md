---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Rogue]]"]
prerequisites: "mastermind racket, Debilitating Strike"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You strategically craft your debilitations to lessen or negate an enemy's tactical advantages. Add the following debilitations to the list you can choose from when you use Debilitating Strike.

- **Debilitation** The target can't flank or contribute to allies' flanking. 

> [!danger] Effect: Methodical Debilitations (Flanking)

- **Debilitation** The target doesn't gain a circumstance bonus to AC from [[Raising a Shield]], lesser cover, or standard cover; it gains a +2 circumstance bonus to AC only from greater cover or [[Taking Cover]]. 

> [!danger] Effect: Methodical Debilitations (Cover)

**Source:** `= this.source` (`= this.source-type`)
