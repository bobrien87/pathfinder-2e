---
type: item
source-type: "Remaster"
level: "4"
price: "{'gp': 80}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A typical spyglass lets you see eight times farther than normal. A fine spyglass adds a +1 item bonus to Perception checks to notice details at a distance.

**Source:** `= this.source` (`= this.source-type`)
