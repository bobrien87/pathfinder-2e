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

Your ancestors lived underground. Your ears are larger than those of other hobgoblins and sensitive to echoes. While you're underground, when you target an opponent that is [[Concealed]] from you or [[Hidden]] from you, reduce the DC of the flat check to 3 for a concealed target or 9 for a hidden one. In addition, if you roll a success on an Acrobatics check to [[Squeeze]], you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
