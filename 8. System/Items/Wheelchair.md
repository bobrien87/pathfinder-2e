---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 5}"
usage: "worn"
bulk: "2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A common wheelchair is ideal for everyday use but isn't designed for strenuous activity. These wheelchairs are most common among nonadventurers. Wheelchairs come in a variety of sizes to suit every person regardless of height or body type.

**Source:** `= this.source` (`= this.source-type`)
