---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

You're tied up and can barely move, or a creature has you pinned. You have the [[Off Guard]] and [[Immobilized]] conditions, and you can't use any attack or manipulate actions except to attempt to [[Escape]] or [[Force Open]] your bonds. Restrained overrides [[Grabbed]].

**Source:** `= this.source` (`= this.source-type`)
