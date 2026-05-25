---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Disarm]]", "[[Sweep]]", "[[Trip]]"]
price: "{'sp': 8}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon consists of a wooden handle attached to a spiked ball or cylinder by a chain, rope, or strap of leather.

**Source:** `= this.source` (`= this.source-type`)
