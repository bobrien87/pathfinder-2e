---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

Your soul has been gripped by a powerful force that calls you closer to death. Doomed always includes a value. The [[Dying]] value at which you die is reduced by your doomed value. If your maximum dying value is reduced to 0, you instantly die. When you die, you're no longer doomed.

Your doomed value decreases by 1 each time you get a full night's rest.

**Source:** `= this.source` (`= this.source-type`)
