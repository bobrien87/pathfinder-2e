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

You affix a trip line or other trigger to a group of either stones or wooden stakes to strike a creature that enters the snare's square. The creature must attempt a [[Reflex]] save saving throw. If you choose stones, the snare deals 9d8 bludgeoning damage; if you choose spikes, it deals 9d8 piercing damage.

**Source:** `= this.source` (`= this.source-type`)
