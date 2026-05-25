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

Your fur grows thick and warm, well suited to the frozen mountains in which you reside. You gain cold resistance equal to half your level (minimum of 1). Environmental cold effects are one step less extreme for you.

**Source:** `= this.source` (`= this.source-type`)
