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

You come from a long line of hobgoblins who commanded goblins. You are smaller than other hobgoblins, but goblins still listen to any commands you bellow. You gain the [[Group Coercion]] skill feat. If you roll a success on an Intimidation check to [[Coerce]] a goblin, you get a critical success instead; if you roll a critical failure, you get a failure instead.

**Source:** `= this.source` (`= this.source-type`)
