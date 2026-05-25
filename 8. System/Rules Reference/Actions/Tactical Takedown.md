---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You direct a coordinated maneuver that sends an enemy tumbling down. Signal up to two squadmates within the aura of your commander's banner. Each of those allies can Stride up to half their Speed as a reaction. If they both end this movement adjacent to an enemy, that enemy must succeed at a [[Reflex]] save against your class DC or fall [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
