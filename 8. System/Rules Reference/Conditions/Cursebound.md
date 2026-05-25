---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

Your oracular curse is constricting around you as you receive divine punishment after drawing too deeply on your mystery's powers. Cursebound is a condition that affects only creatures with an oracular curse, and cursebound always includes a value. Your specific oracular curse imposes unique negative effects depending on your cursebound value. You can remove the cursebound condition only by Refocusing.

**Source:** `= this.source` (`= this.source-type`)
