---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Tripkee|Tripkee]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your thick leathery skin resembles that of a toad. You gain 8 Hit Points from your ancestry instead of 6. You gain a +1 circumstance bonus to saves against diseases and poisons.

**Source:** `= this.source` (`= this.source-type`)
