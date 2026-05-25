---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Ranger]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You designate a single creature as your prey and focus your attacks against that creature. You must be able to see or hear the prey, or you must be tracking the prey during exploration.

You gain a +2 circumstance bonus to Perception checks when you [[Seek]] your prey and a +2 circumstance bonus to Survival checks when you [[Track]] your prey. You also ignore the penalty for making ranged attacks within your second range increment against the prey you're hunting.

You can have only one creature designated as your prey at a time. If you use Hunt Prey against a creature when you already have a creature designated, the prior creature loses the designation and the new prey gains the designation. Your designation lasts until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
