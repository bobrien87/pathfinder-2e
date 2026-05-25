---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Hobgoblin|Hobgoblin]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your family have been alchemists, engineers, and scientists for generations, laboring on projects that bring smoke and fire to the field of battle. You gain fire resistance equal to half your level (minimum 1). You automatically succeed at the DC 5 flat check to target a [[Concealed]] creature if that creature is concealed only by smoke.

**Source:** `= this.source` (`= this.source-type`)
