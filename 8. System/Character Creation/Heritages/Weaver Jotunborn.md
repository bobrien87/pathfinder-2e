---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Jotunborn|Jotunborn]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You've mastered the art of iivlar silk weaving, a technique that requires a fine attention to detail. You are trained in Crafting. You gain a +1 circumstance bonus to Perception checks to [[Seek]] when searching for hidden details like secret doors or traps.

**Source:** `= this.source` (`= this.source-type`)
