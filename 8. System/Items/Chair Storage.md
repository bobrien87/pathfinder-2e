---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 1}"
usage: "worn"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Chair storage can be purchased and applied to any wheelchair. This reduces the amount of Bulk the items weigh when stored within the chair, much like a backpack. The first 2 Bulk of items stowed in your chair don't count against your Bulk limit. If you use both chair storage and a backpack at the same time, only 2 Bulk total isn't counted against your limit, much like if you used multiple backpacks or similar items at the same time.

**Source:** `= this.source` (`= this.source-type`)
