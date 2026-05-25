---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Halfling]]", "[[Propulsive]]"]
price: "{'gp': 5}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This staff ends in a Y-shaped split that cradles a sling. The length of the staff provides excellent leverage when used two-handed to fling rocks or bullets from the sling.

**Source:** `= this.source` (`= this.source-type`)
