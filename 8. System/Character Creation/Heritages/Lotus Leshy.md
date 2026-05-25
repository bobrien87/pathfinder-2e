---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Leshy|Leshy]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You effortlessly float on the surface of water. You can walk on the surface of still water and other non-damaging liquids, moving at half your normal Speed. You can also attempt to [[Balance]] to move across the surface of flowing water, using the DC of a Swim check to move through the water. When you do this, you can't move faster than half your Speed, and if you fail or critically fail, you fall into the water rather than the normal effects.

**Source:** `= this.source` (`= this.source-type`)
