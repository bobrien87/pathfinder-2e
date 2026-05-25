---
type: item
source-type: "Remaster"
level: "0"
price: "{'cp': 1}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These small spikes can be used as anchors to make climbing easier. To affix a piton, you must hold it in one hand and use a hammer to drive it in with your other hand. You can attach a rope to the hammered piton so that you don't fall all the way to the ground on a critical failure while Climbing.

**Source:** `= this.source` (`= this.source-type`)
