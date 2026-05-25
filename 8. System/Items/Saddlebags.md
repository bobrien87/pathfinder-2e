---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 2}"
usage: "worn"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Saddlebags come in a pair. Each can hold up to 3 Bulk of items, and the first 1 Bulk of items in each doesn't count against your mount's Bulk limit. The Bulk value given is for saddlebags worn by a mount. If you are carrying or stowing saddlebags, they count as 1 Bulk instead of light Bulk.

**Source:** `= this.source` (`= this.source-type`)
