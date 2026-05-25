---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Leshy|Leshy]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your prehensile vines grant you unmatched skill at climbing. You do not need to have any hands free to [[Climb]]. Additionally, if you roll a success on an Athletics check to Climb, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
