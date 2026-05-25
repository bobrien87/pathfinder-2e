---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 4}"
usage: "other"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This entry is a catchall for basic hand tools that don't have a specific adventuring purpose. A hoe, shovel, or sledgehammer is a long tool, and a hand drill, ice hook, or trowel is a short tool. A tool can usually be used as an improvised weapon, dealing 1d4 damage. The GM determines the damage type that's appropriate or adjusts the damage if needed.

**Source:** `= this.source` (`= this.source-type`)
