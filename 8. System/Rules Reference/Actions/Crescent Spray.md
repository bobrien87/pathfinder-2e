---
type: action
source-type: "Remaster"
traits: ["[[Flourish]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are wielding a crescent cross

**Effects** You Strike up to three times with the ranged version of your crescent cross. If it is currently in its melee configuration, you can swap it to its ranged configuration as a free action before attempting these Strikes. You must have a bolt already chambered for each Strike and can Interact to swap to a different capacity chamber as a free action between each Strike. Each attack counts toward your multiple attack penalty, but you do not increase your penalty until you have made all your attacks.

**Source:** `= this.source` (`= this.source-type`)
