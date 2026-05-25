---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Automaton|Automaton]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your lithe, humanoid shape is designed for speed and accuracy suitable for ranged combat. You gain the [[Automaton Aim]] action.

**Source:** `= this.source` (`= this.source-type`)
