---
type: action
source-type: "Remaster"
traits: ["[[Barbarian]]"]
cast: "`pf2:0`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You roll initiative.

**Requirements** You are not [[Encumbered]] or wearing heavy armor.

So long as you are able to move freely, your fury is instinctive and instantaneous. You [[Rage]].

**Source:** `= this.source` (`= this.source-type`)
