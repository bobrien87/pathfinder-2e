---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Trip]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This curved sickle sword has a pointed tip, allowing it to be swung in wide arcs or thrust vertically around enemy defenses. The tip of a khopesh is hooked and can be used to trip an opponent.

**Source:** `= this.source` (`= this.source-type`)
