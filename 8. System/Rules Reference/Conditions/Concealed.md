---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

You are difficult for one or more creatures to see due to thick fog or some other obscuring feature. You can be concealed to some creatures but not others. While concealed, you can still be [[Observed]], but you're tougher to target. A creature that you're concealed from must succeed at a flat check when targeting you with an attack, spell, or other effect. If the check fails, you aren't affected. Area effects aren't subject to this flat check.

**Source:** `= this.source` (`= this.source-type`)
