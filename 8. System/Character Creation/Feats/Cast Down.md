---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "harmful font or healing font"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The sheer force of your faith can bring a foe crashing down. If the next action you use is to cast [[Harm]] or [[Heal]] to damage one creature, the target is knocked [[Prone]] if it takes any damage from the spell. If the target critically fails its save against the spell, it also takes a –10-foot status penalty to its Speed for 1 minute.

> [!danger] Effect: Cast Down

**Source:** `= this.source` (`= this.source-type`)
