---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Acid]]", "[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Infused]]", "[[Splash]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tiny glass flask contains volatile chemicals that can be used offensively in a pinch. The bomb deals acid damage and acid splash damage.

**Source:** `= this.source` (`= this.source-type`)
