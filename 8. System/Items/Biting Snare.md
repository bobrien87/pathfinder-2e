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

This snare closes shut on the leg of a creature. The snare deals 5d6 piercing damage to the first creature that enters its square; that creature must attempt a [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage.
- **Critical Failure** The creature takes double damage and takes a –10-foot status penalty to its Speed until it recovers at least 1 Hit Point.

**Source:** `= this.source` (`= this.source-type`)
