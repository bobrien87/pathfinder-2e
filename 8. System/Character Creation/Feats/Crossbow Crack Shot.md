---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're exceptionally skilled with the crossbow. The first time each round that you Interact to reload a crossbow you are wielding, including Interact actions as part of your slinger's reload and similar effects, you increase the range increment for your next Strike with that weapon by 10 feet and deal 1 additional precision damage per weapon damage die with that Strike. If your crossbow has the backstabber trait and you are attacking an [[Off Guard]] target, backstabber deals 2 additional precision damage per weapon damage die instead of its normal effects.

**Source:** `= this.source` (`= this.source-type`)
