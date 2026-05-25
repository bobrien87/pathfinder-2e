---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Lizardfolk|Lizardfolk]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your family is descended from the most common lizardfolk heritage, and you are accustomed to aquatic environments. You gain a 15-foot swim Speed.

**Source:** `= this.source` (`= this.source-type`)
