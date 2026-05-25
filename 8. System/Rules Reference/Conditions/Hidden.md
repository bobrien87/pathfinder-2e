---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

While you're hidden from a creature, that creature knows the space you're in but can't tell precisely where you are. You typically become hidden by using Stealth to [[Hide]]. When [[Seeking]] a creature using only imprecise senses, it remains hidden, rather than [[Observed]]. A creature you're hidden from is [[Off Guard]] to you, and it must succeed at a flat check when targeting you with an attack, spell, or other effect or it fails to affect you. Area effects aren't subject to this flat check.

A creature might be able to use the seek action to try to observe you.

**Source:** `= this.source` (`= this.source-type`)
