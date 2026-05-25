---
type: action
source-type: "Remaster"
traits: ["[[Transcendence]]"]
cast: "`pf2:3`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You shoot an arrow that multiplies into a dense cloud of weapons. Make one ranged Strike with a –2 penalty against each enemy you are aware of within a cone as long as your weapon's first range increment. Roll the damage only once for all targets, and all the Strike's damage is spirit damage instead of its normal type. Each attack counts toward your multiple attack penalty, the penalty doesn't increase until you have made all your attacks.

**Source:** `= this.source` (`= this.source-type`)
