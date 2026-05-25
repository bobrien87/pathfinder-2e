---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

Anything in plain view is observed by you. If a creature takes measures to avoid detection, such as by using Stealth to [[Hide]], it can become [[Hidden]] or [[Undetected]] instead of observed. If you have another precise sense besides sight, you might be able to observe a creature or object using that sense instead. You can observe a creature with only your precise senses. When [[Seeking]] a creature using only imprecise senses, it remains hidden, rather than observed.

**Source:** `= this.source` (`= this.source-type`)
