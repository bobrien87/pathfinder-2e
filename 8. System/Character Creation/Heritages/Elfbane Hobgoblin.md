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

Hobgoblins were engineered long ago from the unreliable and fecund goblins to be used as an army against the elves. Although the elves ultimately freed the hobgoblins from their bondage, some hobgoblins retain ancestral resistance to magic, which they refer to as "elf magic." You gain the [[Resist Elf Magic]] reaction.

**Source:** `= this.source` (`= this.source-type`)
