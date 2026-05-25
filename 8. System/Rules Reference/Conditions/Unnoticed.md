---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

If you're unnoticed by a creature, that creature has no idea you're present. When you're unnoticed, you're also [[Undetected]]. This matters for abilities that can be used only against targets totally unaware of your presence.

**Source:** `= this.source` (`= this.source-type`)
