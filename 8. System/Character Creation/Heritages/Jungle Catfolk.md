---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Catfolk|Catfolk]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You're descended from jungle stalkers and can move swiftly through scrub and underbrush. You ignore difficult terrain from undergrowth, and greater difficult terrain from undergrowth is only difficult terrain for you.

**Source:** `= this.source` (`= this.source-type`)
