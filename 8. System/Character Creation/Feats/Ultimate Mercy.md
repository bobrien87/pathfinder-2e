---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Champion]]"]
prerequisites: "Mercy"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your mercy transcends the bounds of life and death. Add ultimate mercy to the types of mercy you can provide. When you use [[Mercy]], you can target a creature that died since your last turn to return it to life. The target returns to life with 1 Hit Point and becomes [[Wounded]] 1. You can't return the target to life if it died from [[Disintegrate]] or a death effect. The creature gains the other benefits of [[Lay on Hands]] after it returns to life.

**Source:** `= this.source` (`= this.source-type`)
