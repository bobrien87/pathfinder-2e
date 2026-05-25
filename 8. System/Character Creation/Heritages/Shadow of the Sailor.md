---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Wayang|Wayang]]"
traits: ["[[Wayang]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your shadow flits across the surface of the water, and so do you. You can walk on the surface of still water and other non-damaging liquids, moving at half your normal Speed. You can attempt to walk along the surface of flowing water as well, still moving at half Speed, but to do so, you must succeed at an Acrobatics check to [[Balance]] using the DC of a Swim check to move through the water; on a failure, you fall into the water. This Acrobatics check doesn't use an action.

**Source:** `= this.source` (`= this.source-type`)
