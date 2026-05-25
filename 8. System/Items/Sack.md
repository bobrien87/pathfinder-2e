---
type: item
source-type: "Remaster"
level: "0"
price: "{'cp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A sack can hold up to 8 Bulk worth of items. A sack containing 2 Bulk or less can be worn on the body, usually tucked into a belt. You can carry a sack with one hand, but must use two hands to transfer items in and out.

**Source:** `= this.source` (`= this.source-type`)
