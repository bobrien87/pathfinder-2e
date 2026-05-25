---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

You're frozen in place. You have the [[Off Guard]] condition and can't act except to [[Recall Knowledge]] and use actions that require only your mind (as determined by the GM). Your senses still function, but only in the areas you can perceive without moving, so you can't [[Seek]].

**Source:** `= this.source` (`= this.source-type`)
