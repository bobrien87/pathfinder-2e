---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

You're held in place by another creature, giving you the [[Off Guard]] and [[Immobilized]] conditions. If you attempt a manipulate action while grabbed, you must succeed at a flat check or it is lost; roll the check after spending the action, but before any effects are applied.

**Source:** `= this.source` (`= this.source-type`)
