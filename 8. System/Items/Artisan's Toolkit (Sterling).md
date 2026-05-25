---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 50}"
usage: "other"
bulk: "2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You need these tools to create items from raw materials with the Craft skill. Sterling artisan's tools give you a +1 item bonus to the check.

Different sets are needed for different work, as determined by the GM; for example, a blacksmith's toolkit differs from a woodworker's toolkit. If you wear your artisan's toolkit, you can draw and replace it as part of the action that uses it.

**Source:** `= this.source` (`= this.source-type`)
