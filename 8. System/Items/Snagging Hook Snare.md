---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 180}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This snare snags a creature with its wicked metal hooks. The first creature to enter the square takes @Damage[5d8[piercing],5d8[slashing]]{5d8 piercing damage and 5d8 slashing damage}, with a [[Reflex]] save.

On a critical failure, the hooks piercing its flesh make the creature [[Immobilized]] until it successfully Escapes.

**Source:** `= this.source` (`= this.source-type`)
