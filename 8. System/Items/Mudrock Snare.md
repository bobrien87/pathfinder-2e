---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Kobold]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 170}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Fired clay covers a shallow pit of thin mud interspersed with fragile vials of a quick-drying agent. The first creature to step into the square breaks through the clay and sinks into the pit, fracturing the vials and releasing the chemicals that harden the mud. That creature must attempt a [[Fortitude]] save as the mud solidifies over its legs.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes a –5-foot circumstance penalty to its Speed for 1 minute or until it Escapes.
- **Failure** The creature is [[Stunned]] 2, and it takes a –10-foot circumstance penalty to its Speed for 1 minute or until it Escapes (DC 27).
- **Critical Failure** The creature is [[Stunned]] 3, and it's [[Immobilized]] for 1 minute or until it Escapes (DC 27).

> [!danger] Effect: Mudrock Snare

**Source:** `= this.source` (`= this.source-type`)
