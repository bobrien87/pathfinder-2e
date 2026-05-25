---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Champion]]"]
prerequisites: "champion's aura, unholy"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your presence as an avatar of evil makes your foes more susceptible to terror and makes it almost impossible for them to shake off fear when you are near. Enemies in your champion's aura take a –1 circumstance penalty to saving throws against fear. In addition, an enemy that ends its turn in your champion's aura can't reduce the value of its frightened condition below 1.

> [!danger] Effect: Aura of Despair

**Source:** `= this.source` (`= this.source-type`)
