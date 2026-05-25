---
type: action
source-type: "Remaster"
traits: ["[[Brandish]]", "[[Commander]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your squad dashes past enemies, slicing their boot laces and breaking their belt buckles. Signal up to two squadmates within the aura of your commander's banner; these squadmates can Stride up to their Speed as a reaction. Each enemy they are adjacent to at any point during this movement must attempt a [[Reflex]] save against your class DC or become [[Clumsy]] 1 for 1 round ([[Clumsy]] 2 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
