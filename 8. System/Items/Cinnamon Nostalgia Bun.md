---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Processed]]"]
price: "{'gp': 11}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Adventures: Troubles in Grayce"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A swirl of cinnamon, sugar, and butter is baked into this fluffy bun. Pulling apart and eating the bun evokes comforting memories of happier times, reducing the value of your frightened condition by 1. You can also attempt an immediate flat check to recover from a single source of persistent mental damage, with the DC reduction from appropriate assistance.

**Source:** `= this.source` (`= this.source-type`)
