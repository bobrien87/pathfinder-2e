---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Attached to shield]]"]
price: "{'sp': 5}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Typically a round, convex, or conical piece of thick metal attached to the center of a shield, a shield boss increases the bludgeoning damage of a shield bash.

**Source:** `= this.source` (`= this.source-type`)
