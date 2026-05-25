---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Jotunborn|Jotunborn]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were tasked with keeping oral and stitched histories for your family, your clan, or even an entire settlement. You are trained in Society. You also gain the [[Additional Lore]] general feat for a lore skill of your choice.

**Source:** `= this.source` (`= this.source-type`)
