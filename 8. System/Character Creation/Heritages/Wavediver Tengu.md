---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Tengu|Tengu]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You're one of the rare tengu who can cut through water like a bird through air, and you often lurk in rivers or oceans where few expect you. You gain a swim Speed of 15 feet.

**Source:** `= this.source` (`= this.source-type`)
