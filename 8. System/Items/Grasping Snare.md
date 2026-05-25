---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 75}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You rig vines and ropes to hold a creature in place. The first creature to enter the square must attempt a [[Reflex]] save with the following effects.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes a –5-foot status penalty to its Speed for 1 minute or until it Escapes.
- **Failure** The creature is [[Immobilized]] for 1 round, then takes a –5-foot status penalty to its Speed for 1 minute. Both effects end early if it Escapes (DC 26).
- **Critical Failure** The creature is immobilized for 1 minute or until it Escapes (DC 26).

> [!danger] Effect: Grasping Snare

**Source:** `= this.source` (`= this.source-type`)
