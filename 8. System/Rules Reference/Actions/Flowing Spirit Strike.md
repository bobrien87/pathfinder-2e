---
type: action
source-type: "Remaster"
traits: ["[[Spirit]]", "[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Make two Strikes with the gleaming blade, each against the same target and using your current multiple attack penalty. If the [[Gleaming Blade]] doesn't have the agile trait, the second Strike takes a –2 penalty. If both attacks hit, you combine their damage, which is all dealt as spirit damage.

You add any precision damage only once. Combine the damage from both Strikes and apply resistances and weaknesses only once. This counts as two attacks when calculating your multiple attack penalty.

**Source:** `= this.source` (`= this.source-type`)
