---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can apply two different infused injury poisons to the same weapon, though not to a piece of ammunition. Each poison's level must be 2 or more levels lower than your level. You have to apply the two poisons individually. Once you've applied both, the poisons merge into a double poison that uses the lower of the two poisons' DCs and number of stages. If the poisons require different types of saving throws (such as Fortitude and Will), choose which of them the double poison uses. This double poison is virulent only if both poisons were virulent. Combine the effects of each stage of the poison on any creature affected by it. For each stage of the poison, use the effects of both poisons and the longer interval for that stage among the two poisons.

**Source:** `= this.source` (`= this.source-type`)
