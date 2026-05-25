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

Whether due to a blessing from Hei Feng or hatching from your egg during a squall, you are resistant to storms. You gain electricity resistance equal to half your level (minimum 1). You automatically succeed at the flat check to target a [[Concealed]] creature if that creature is concealed only by rain or fog.

**Source:** `= this.source` (`= this.source-type`)
