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

Your hands and feet exude a film that helps them adhere to surfaces. You gain a +2 circumstance bonus to your Fortitude and Reflex DC against attempts to [[Disarm]], [[Shove]], [[Reposition]], or [[Trip]] you. When ascending trees, vines, and other foliage, if you roll a success on the Athletics check to Climb, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
