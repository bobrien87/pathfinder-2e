---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Fighter]]"]
prerequisites: "Aggressive Block or Brutish Shove"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whether you're shoving opponents with a shield or a large weapon, you've learned to push them even further. Increase the distance you [[Shove]] your opponent with [[Aggressive Block]] or [[Brutish Shove]] to 10 feet on a success or 20 feet on a critical success. When you use Aggressive Block, you can choose whether the target is [[Off Guard]] or Shoved. When you make a Brutish Shove, you also Shove the target 5 feet on a failure.

**Source:** `= this.source` (`= this.source-type`)
