---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

This condition reflects a creature's disposition toward a particular character, and only supernatural effects (like a spell) can impose on a PC. A creature hostile to a character actively seeks to harm that character. It doesn't necessarily attack, but it won't accept [[Requests]] from the character.

**Source:** `= this.source` (`= this.source-type`)
