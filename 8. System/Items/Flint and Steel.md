---
type: item
source-type: "Remaster"
level: "0"
price: "{'cp': 5}"
usage: "held-in-two-hands"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Flint and steel are useful in creating a fire if you have the time to catch a spark, though using them is typically too time-consuming to be practical during an encounter. Even in ideal conditions, using flint and steel to light a flame requires using at least 3 actions, and often significantly longer.

**Source:** `= this.source` (`= this.source-type`)
