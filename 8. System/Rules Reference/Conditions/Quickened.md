---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

You're able to act more quickly. You gain 1 additional action at the start of your turn each round. Many effects that make you quickened require you use this extra action only in certain ways. If you become quickened from multiple sources, you can use the extra action you've been granted for any single action allowed by any of the effects that made you quickened. Because quickened has its effect at the start of your turn, you don't immediately gain actions if you become quickened during your turn.

**Source:** `= this.source` (`= this.source-type`)
