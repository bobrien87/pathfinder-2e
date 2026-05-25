---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

You have been commanded, magically dominated, or otherwise had your will subverted. The controller dictates how you act and can make you use any of your actions, including attacks, reactions, or even [[Delay]]. The controller usually doesn't have to spend their own actions when controlling you.

**Source:** `= this.source` (`= this.source-type`)
