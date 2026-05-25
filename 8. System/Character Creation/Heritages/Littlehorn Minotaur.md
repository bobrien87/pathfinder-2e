---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Minotaur|Minotaur]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Though no less powerful, your frame (and your horns) are smaller than those of most other minotaurs. Instead of Large, your size is Medium. Your horns unarmed attack deals 1d6 piercing damage instead of 1d8, but it has the agile trait.

**Source:** `= this.source` (`= this.source-type`)
