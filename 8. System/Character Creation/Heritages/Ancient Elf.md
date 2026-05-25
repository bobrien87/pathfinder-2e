---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Elf|Elf]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

In your long life, you've dabbled in many paths and many styles. A typical ancient elf is at least 100 years old, though you might be younger at the GM's discretion. Choose a class other than your own. You gain the multiclass dedication feat for that class, even though you don't meet its level prerequisite. You must still meet its other prerequisites to gain the feat.

**Source:** `= this.source` (`= this.source-type`)
