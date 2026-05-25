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

Your work as an iivlar keeper has granted you a greater understanding of these sacred creatures and the ability to track them, as elusive as they may be. You are trained in Survival, and you gain the [[Survey Wildlife]] skill feat. You gain a +1 circumstance bonus to [[Track]] animals.

**Source:** `= this.source` (`= this.source-type`)
