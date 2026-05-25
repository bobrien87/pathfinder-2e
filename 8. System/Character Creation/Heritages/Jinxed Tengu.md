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

Your lineage has been exposed to curse after curse, and now they slide off your feathers like rain. If you succeed at a saving throw against a curse or misfortune effect, you get a critical success instead. When you would gain the [[Doomed]] condition, attempt a DC 17 flat check. On a success, reduce the value of the doomed condition you would gain by 1.

**Source:** `= this.source` (`= this.source-type`)
