---
type: action
source-type: "Remaster"
traits: ["[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You throw your weapon ikons to either side of a creature, and they seek each other out, converging on the target. Make two thrown Strikes against a target within the first range increment of both your weapon ikons. This counts as two attacks toward your multiple attack penalty, but the penalty doesn't increase until after you've made both attacks. The target is flanked for both attacks (typically making it [[Off Guard]] against both attacks). If both Strikes hit, the target also takes an additional die of weapon damage. The weapons then return to your hand.

**Source:** `= this.source` (`= this.source-type`)
