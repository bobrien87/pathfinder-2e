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

Your team dashes about in a series of maneuvers that leave the enemy befuddled. Signal up to two squadmates within the aura of your commander's banner; these squadmates can Stride up to their Speed as a reaction. Each enemy they are adjacent to at any point during this movement must attempt a [[Will]] save against your class DC or become [[Stupefied 1]] for 1 round ([[Stupefied 2]] on a critical failure); this is a mental effect.

**Source:** `= this.source` (`= this.source-type`)
