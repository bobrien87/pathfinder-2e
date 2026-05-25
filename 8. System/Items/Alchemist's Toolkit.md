---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 3}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This mobile collection of vials and chemicals can be used for simple alchemical tasks. If you wear your alchemist's toolkit, you can draw and replace it as part of the action that uses it.

**Source:** `= this.source` (`= this.source-type`)
