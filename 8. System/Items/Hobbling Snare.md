---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You rig vines, ropes, or wires to cinch tight around a creature that triggers this snare. The first creature to enter the square must attempt a [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes a –5-foot status penalty to its Speed for 1 minute or until it Escapes.
- **Failure** As success, but the penalty is -10 feet.
- **Critical Failure** As success, but the penalty is -20 feet.

> [!danger] Effect: Hobbling Snare

**Source:** `= this.source` (`= this.source-type`)
