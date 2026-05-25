---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A cane is a straight cane with a curved handle, shaped like the tip of a hook. Its simple design helps with balance and only slightly assists with taking weight off the affected opposite leg. The cane is typically 2 to 3 feet long but can be lengthened or shortened as needed.

**Source:** `= this.source` (`= this.source-type`)
