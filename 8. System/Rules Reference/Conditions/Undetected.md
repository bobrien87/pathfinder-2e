---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

When you are undetected by a creature, that creature can't see you at all, has no idea what space you occupy, and can't target you, though you still can be affected by abilities that target an area. When you're undetected by a creature, that creature is [[Off Guard]] to you.

A creature you're undetected by can guess which square you're in to try targeting you. It must pick a square and attempt an attack. This works like targeting a [[Hidden]] creature (requiring a flat check), but the flat check and attack roll are rolled in secret by the GM, who doesn't reveal whether the attack missed due to failing the flat check, failing the attack roll, or choosing the wrong square. They can [[Seek]] to try to find you.

**Source:** `= this.source` (`= this.source-type`)
