---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kobold|Kobold]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You grew up in a warren crisscrossed by underwater passages, whether natural or excavated, and were influenced by a powerful aquatic entity or being of primal water. You gain a swim Speed of 15 feet.

**Source:** `= this.source` (`= this.source-type`)
