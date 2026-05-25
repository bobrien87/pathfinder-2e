---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Human|Human]]"
source: "Pathfinder Beginner Box: Secrets of the Unlit Star"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your family has trained for battle for generations, granting you advantages against your enemies. You gain a +1 bonus to initiative rolls. In addition, you gain the [[Diehard]] feat.

*Note: This heritage is from the Beginner Box and features non-standard heritage features*

**Source:** `= this.source` (`= this.source-type`)
