---
type: item
source-type: "Remaster"
level: "1"
price: "{'cp': 0, 'gp': 0, 'pp': 0, 'sp': 15}"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This item is the starter kit for an adventurer, containing the essential items for exploration and survival. The Bulk value is for the entire pack together, but see the descriptions of individual items as necessary.

The pack contains the following items: a backpack, a bedroll, 10 pieces of chalk, flint and steel, 50 feet of rope, 2 weeks' rations, soap, 5 torches, and a waterskin.

**Source:** `= this.source` (`= this.source-type`)
