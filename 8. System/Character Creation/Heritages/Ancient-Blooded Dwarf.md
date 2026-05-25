---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Dwarf|Dwarf]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Dwarven heroes of old could shrug off their enemies' magic, and some of that resistance manifests in you. You gain the [[Call on Ancient Blood]] reaction.

**Source:** `= this.source` (`= this.source-type`)
