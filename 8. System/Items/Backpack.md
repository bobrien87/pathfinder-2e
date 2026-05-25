---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 1}"
usage: "wornbackpack"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A backpack holds up to 4 Bulk of items and the first 2 Bulk of these items don't count against your Bulk limits. If you're carrying or stowing the pack rather than wearing it on your back, its Bulk is light instead of negligible

**Source:** `= this.source` (`= this.source-type`)
