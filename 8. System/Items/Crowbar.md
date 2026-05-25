---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 5}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When Forcing Open an object that doesn't have an easy grip, a crowbar makes it easier to gain the necessary leverage. Without a crowbar, prying something open takes a -2 item penalty to the Athletics check to Force Open.

**Source:** `= this.source` (`= this.source-type`)
