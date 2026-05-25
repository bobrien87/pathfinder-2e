---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Rogue]]"]
prerequisites: "scoundrel racket, Debilitating Strike"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You learn new debilitations that grant you tactical advantages against your foes. Add the following debilitations to the list you can choose from when you use Debilitating Strike.

- **Debilitation** The target can't use reactions.

- **Debilitation** The target can't flank or contribute to allies' flanking. 

> [!danger] Effect: Tactical Debilitations (No Flanking)

**Source:** `= this.source` (`= this.source-type`)
