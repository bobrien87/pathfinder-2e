---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You arrange a spiky cage of bones, particularly tough vegetation, or other material to spring up when disturbed. The snare deals 10d8 piercing damage to the first creature to enter this square; that creature must attempt a [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is knocked aside by the snare's deployment, takes half damage, and is [[Off Guard]] until the end of its next turn.
- **Failure** The creature is captured by the cage, taking full damage and falling [[Prone]]. It's [[Immobilized]] while it remains within the cage. It can get free by Escaping or by destroying the cage (AC 30, Fort +18, Ref +24, Hardness 5, HP 30, object immunities).
- **Critical Failure** As failure, but the creature takes double damage.

**Source:** `= this.source` (`= this.source-type`)
